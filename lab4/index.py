import math


def build_index(coll_conn):
    """Build TF-IDF index for all documents"""
    if not coll_conn:
        raise Exception("No collection provided")
    documents = coll_conn.find()
    
    if not documents:
        return []
    result = []
    for document in documents:
        result.append({
            "class": document["class"],
            "words": dict((
                (word, calc_index(coll_conn, document, word, count))
                for word, count in document["words"].items()
            ))
        })

    return result


def calc_index(coll_conn, document, word, count):
    """Calculates TD-IDF index.

    For more information look at https://wikipedia.org/wiki/TF-IDF

    Params:
        coll_conn -- connection to mongo database
        document {dict} -- dict with document information
        word {str} -- word
        count {number} -- count of entries of word in document
    """
    words_count = len(document['words'])
    word_def = "words.{}".format(word)
    doc_w_word_count = coll_conn.find({
        word_def: {"$exists": True}
    }).count()
    docs_count = coll_conn.find().count()

    TF = count / words_count
    try:
        IDF = math.log(docs_count / doc_w_word_count)
    except ZeroDivisionError:
        IDF = 1
    return TF * IDF
    

def calc_distance(index_node, document):
    """Calculate Euclidean distance

    Calculate Euclidean distance between index_node
    and document.
    """
    document_words = document["words"]
    index_words = index_node["words"]
    sm = 0
    processed_words = set() 
    for word in index_words:
        if word in document_words:
            diff = index_words[word] - document_words[word]
        else: 
            diff = index_words[word]
        processed_words.add(word)
        sm += diff * diff
    for word in document_words:
        if word not in processed_words:
            processed_words.add(word)
            diff = document_words[word]
            sm += diff * diff
    return math.sqrt(sm)
