import json 
import click
import os

from pymongo import MongoClient

from index import build_index
from index import calc_index, calc_distance
from docproc import process_document


def load_config(conf_file):
    with open(conf_file, "r") as conf_file:
        CONFIG = conf_file.read()
    return json.loads(CONFIG)

@click.command()
@click.option("--data", default=None, help="Specify file")
@click.option("--config", default="config.json", help="Config file")
def open_file(config, data):

    CONFIG = {}
    MONGO_CONN = None
    DB_CONN = None
    COLL_CONN = None
    if not os.path.exists(config):
        print("Error: invalid config file specified")
        exit(1)
    CONFIG = load_config(config)
    MONGO_CONN = MongoClient(
        CONFIG["mongo_host"], CONFIG["mongo_port"])
    DB_CONN = MONGO_CONN.knn_test
    COLL_CONN = DB_CONN.knn_collection

    index = build_index(COLL_CONN) 
    print(index)
    
    if not os.path.exists(data):
        print("Error: file does not exist")
    doc = process_document(document_name=data)

    mutated_doc = {
        "class": None,
        "words": dict((
            (word, calc_index(COLL_CONN, doc, word, count))
            for word, count in doc["words"].items()
        ))
    } 
    distance = [
        (node["class"], calc_distance(node, mutated_doc))
        for node in index
    ]

    sorted_distance = sorted(
        distance, 
        key=lambda x: x[1]
    )
    
    resulting_class = {}
    for item in sorted_distance:
        if item[0] not in resulting_class:
            resulting_class[item[0]] = 0
        resulting_class[item[0]] += 1
        if resulting_class[item[0]] >= CONFIG["K"]:
            print("Resulting class found, it's {}".format(item[0]))
            doc["class"] = item[0]
            COLL_CONN.insert_one(doc)
            exit(0)
    print(doc)
    print("Could not determine class, please enter it")
    doc["class"] = input()
    COLL_CONN.insert_one(doc)

if __name__ == "__main__":
    open_file()
