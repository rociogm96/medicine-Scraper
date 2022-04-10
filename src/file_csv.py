import src.cima.medicament as medicament
from src.cima.crawler import Crawler
import pandas as pd
from time import sleep
from random import uniform


def make_csv(med):

    med = med.upper()

    scraping = Crawler(med)

    lista = scraping.get_list_references()

    lista_med = []

    for ref in lista:
        sleep(uniform(1, 3))  # Wait between 1 and 3 seconds for each medicament
        medicamento = medicament.Medicament(ref)
        info_medicamento = medicamento.get_all_info
        lista_med.append(info_medicamento)

    result = pd.DataFrame(lista_med)

    route = f"./results/{med}.csv"

    result.to_csv(route, index=False)
