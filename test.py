import numpy as np
import pandas as pd
import csv
import spacy
from spacy import displacy

# Loading spanish word-vecotr model
nlp_es = spacy.load('es_core_news_md')

# Creating jobs dict
jobs_dict = {
    '1': "Lanzar standalone", 
    '2': "Lanzar online"
}

SIMILARITY_THRESHOLD = 0.9

references = []
references.append(nlp_es("Quiero ejecutar el job framework online 2 en Jenkins"))
references.append(nlp_es("Me gustaría compilar el job de standalone 2"))

def compute_similarity(doc):
    
    for reference in references:    
        if doc.similarity(reference) > SIMILARITY_THRESHOLD:
            return True
    return False

def load_jobs_list(filename):
    """Save the content of a csv file into a dictionaty.

    Args:
        filename (str): Name of the CSV to convert to a dictionary.

    Returns:
        jobs_list (dict): Dictionary with all the csv entries in it.
    
    """
    jobs_list = {}
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip the header
        jobs_list = {rows[0]: rows[1] for rows in reader}
        return jobs_list

def process_input(nlp, jobs_list):
    print("Bienvenido al servicio de interacción con Jenkins.")
    text = input("Por favor, escribe qué función deseas realizar: ")

    # Feed the input text to the model
    doc = nlp(text)

    # # Compare the input to base sentences to know if the context is correct
    # if doc.similarity(reference1) < 0.9:
    #     print("Lo siento, no entiendo exactamente la orden")
    #     process_input(nlp, jobs_list)

    # # Register the processed input for a job ID
    # for token in doc:
    #     if str(token) in jobs_list:
    #         print("ID: {0}\nHead: {1}".format(token, token.head))

    # Alternative version
    if compute_similarity(doc):
        print("Hola")
        for token in doc:
            if str(token) in jobs_list:
                print("ID: {0}\nHead: {1}".format(token, token.head))
    else:
        print("Lo siento, no entiendo exactamente la orden")
        process_input(nlp, jobs_list)


def main():
    jobs_list = load_jobs_list('jobs_list.csv')
    process_input(nlp_es,jobs_list)


if __name__ == "__main__":
    main()
