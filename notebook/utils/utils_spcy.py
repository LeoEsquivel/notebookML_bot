import spacy
from spacy.matcher import Matcher

npl = spacy.load("en_core_web_sm")


def find_entities_key_terms(text:str) -> dict:
    doc = npl(text)

    entities = {}

    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = []
        entities[ent.label_].append(ent.text)

    # print("Entidades detectadas:")
    # for categoria, valores in entities.items():
    #     print(f"{categoria}: {', '.join(valores)}")

    # key_terms = [token.text for token in doc if token.is_alpha and not token.is_stop]

    # print("Tokens (palabras):")
    # for token in doc:
    #     print(token.text)

    # print("\nOraciones:")
    # for sent in doc.sents:
    #     print(sent.text)

    # print("\nEntidades nombradas (NER):")
    # for ent in doc.ents:
    #     print(f"{ent.text} ({ent.label_})")

    # print("\nLematización (formas base):")
    # for token in doc:
    #     print(f"{token.text} -> {token.lemma_}")

    # print("\nPartes del discurso:")
    # for token in doc:
    #     print(f"{token.text}: {token.pos_}")

    return {
        "entities": { k: list(set(v)) for k, v in entities.items() },
    }
