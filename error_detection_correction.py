import spacy

nlp = spacy.load("en_core_web_sm")

def check_errors(text):
    doc = nlp(text)
    errors = []
    for token in doc:
        if token.is_alpha and not token.is_stop and token.is_oov:  # Use `token.is_oov` directly
            errors.append(f"Possible error at '{token.text}'")
    return {"text": text, "corrections": errors}
