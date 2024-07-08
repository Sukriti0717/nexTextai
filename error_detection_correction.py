import spacy

nlp = spacy.load("en_core_web_sm")

def check_errors(text):
    doc = nlp(text)
    corrections = []
    for token in doc:
        if token._.is_oov:
            corrections.append((token.text, token._.suggestions))
    return corrections
