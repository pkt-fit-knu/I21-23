import json 

CONFIG = {}

def load_config():
    with open("config.json", "r") as conf_file:
        CONFIG = conf_file.read()
    CONFIG = json.loads(conf_file)


if __name__ = "__main__":
    load_config()

