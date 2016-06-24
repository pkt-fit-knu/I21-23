import re


def process_document(text="", document_name=""):
    """Process document

    Build data info about document: count words, etc.

    Params:
        text {str} -- text of document to be processed
        document_name {str} -- name of document to be processed
    Note: one of listed must be entered, not both!

    Returns:
        {dict} -- list of words with their count
    """
    if text and document_name:
        raise Exception("`text` and `document_name` were passed! Pass only one of them")
    if text:
        return process_text(text)
    elif document_name:
        with open(document_name, "r") as data:
            text = data.read()
        return process_text(text)
    else:
        raise Exception("None params were passed! Pass some of them!")


def process_text(text):
    words = re.split(r"\W+", text.upper())
    word_counts = {}
    for word in words:
        if word:
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1
    return {
        "class": None,
        "words": word_counts,
    }

