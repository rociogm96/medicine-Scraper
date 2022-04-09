import src.cima.medicament as medicament
from src.cima.crawler import Crawler
import pandas as pd


def make_csv(med):

    scraping = Crawler(med)

    lista = scraping.get_list_references()

    lista_med = []

    for ref in lista:
        medicamento = medicament.Medicament(ref)
        info_medicamento = medicamento.get_all_info
        lista_med.append(info_medicamento)

    result = pd.DataFrame.from_dict(lista_med)
    route = f"../results/{med}.csv"

    result.to_csv(route, index=False)








