import os
import sys
import socket
import urllib
import pandas as pd

DIR_FRANCE_DATA = os.path.join('./data',"france")

DATA_URL = dict(
    hospitaliere = ("https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7","hospitaliere.csv"),
    hospitaliere_new = ("https://www.data.gouv.fr/fr/datasets/r/6fadff46-9efd-4c53-942a-54aca783c30c","hospitaliere_new.csv"),
    hospitaliere_classe_age = ("https://www.data.gouv.fr/fr/datasets/r/08c18e08-6780-452d-9b8c-ae244ad529b3","hospitaliere_classe_age.csv"),
    hospitaliere_etablissements = ("https://www.data.gouv.fr/fr/datasets/r/41b9bd2a-b5b6-4271-8878-e45a8902ef00","hospitaliere_etabli.csv"),
    tests_daily = ("https://www.data.gouv.fr/fr/datasets/r/b4ea7b4b-b7d1-4885-a099-71852291ff20","tests_daily.csv"),
    meta_hospitaliere = ("https://www.data.gouv.fr/fr/datasets/r/3f0f1885-25f4-4102-bbab-edec5a58e34a","meta_hospitaliere.csv"),
    meta_hospitaliere_new = ("https://www.data.gouv.fr/fr/datasets/r/4900f53f-750d-4c5a-9df7-2d4ceb018acf","meta_hospitaliere_new.csv"),
    meta_hospitaliere_classe_age = ("https://www.data.gouv.fr/fr/datasets/r/929dff1b-b07c-4637-9690-fb7219ad3eb8","meta_hospitaliere_classe_age.csv"),
    meta_hospitaliere_etablissements = ("https://www.data.gouv.fr/fr/datasets/r/415c852b-7898-40f8-8f71-b9171faf4516","meta_hospitaliere_etablissements.csv"),
    meta_tests = ("https://www.data.gouv.fr/fr/datasets/r/971c5cbd-cd80-4492-b2b3-c3deff8c1f5e","meta_tests.csv"),
    tranches_age = ("https://www.data.gouv.fr/fr/datasets/r/db378f2a-83a1-40fd-a16c-06c4c8c3535d","age.csv")
)

def download(url, path):
    socket.setdefaulttimeout(30)
    if not os.path.exists(path):
        try:
            print("Download job begin.")
            urllib.request.urlretrieve(url, path)
            print("Download job finished.")
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    urllib.urlretrieve(url, path)
                    break
                except socket.timeout:
                    err_info = 'Reloading for %d time'%count if count ==1 else 'Reload for %d times'%count
                    print(err_info)
                    count += 1
            if count > 5:
                    print("download job failed")

def load_data(url, fichier):
    # Détection du répertoire
    os.makedirs(DIR_FRANCE_DATA, exist_ok=True)
    filepath=os.path.join(DIR_FRANCE_DATA,fichier)
    # M-a-j les données 
    download(url, filepath)
    # Lire les données
    df = pd.read_csv(filepath,encoding='utf8',sep=';')
    return df

def load_hospitaliere():
    url,fichier=DATA_URL["hospitaliere"]
    data = load_data(url,fichier)
    return data

def load_hospitaliere_new():
    url,fichier=DATA_URL["hospitaliere_new"]
    data = load_data(url,fichier)
    return data

def load_hospitaliere_classe_age():
    url,fichier=DATA_URL["hospitaliere_classe_age"]
    data = load_data(url,fichier)
    return data

def load_hospitaliere_etablissements():
    url,fichier=DATA_URL["hospitaliere_etablissements"]
    data = load_data(url,fichier)
    return data

def load_tests_daily():
    url,fichier=DATA_URL["tests_daily"]
    data = load_data(url,fichier)
    return data

def load_meta_hospitaliere():
    url,fichier=DATA_URL["meta_hospitaliere"]
    data = load_data(url,fichier)
    return data

def load_meta_hospitaliere_new():
    url,fichier=DATA_URL["meta_hospitaliere_new"]
    data = load_data(url,fichier)
    return data

def load_meta_hospitaliere_classe_age():
    url,fichier=DATA_URL["meta_hospitaliere_classe_age"]
    data = load_data(url,fichier)
    return data

def load_meta_hospitaliere_etablissements():
    url,fichier=DATA_URL["meta_hospitaliere_etablissements"]
    data = load_data(url,fichier)
    return data

def load_meta_tests():
    url,fichier=DATA_URL["meta_tests"]
    data = load_data(url,fichier)
    return data

def load_tranches_age():
    url,fichier=DATA_URL["tranches_age"]
    data = load_data(url,fichier)
    return data