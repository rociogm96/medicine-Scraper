import src.cima.medicament as medicament
from src.cima.crawler import Crawler
from src.file_csv import make_csv

# Ejemplos crawler y searcher
scraping = Crawler("Codeina")

lista = scraping.get_list_references()

# Ventaja tarda menos no tiene que comprobar todos los elementos con este método
numero = scraping.get_amount_results()

print(numero)
print(lista)
print(len(lista))

# Ejemplo módulo medicament
medicamentoA = medicament.Medicament("84781")
print(medicamentoA.name)
print(medicamentoA.characteristics)
print(medicamentoA.atc_codes)

medicamentoA = medicament.Medicament("84781")
info_medicamento = medicamentoA.get_all_info

for k, v in info_medicamento.items():
    print(k, "\n\t", v)

# Ejemplo módulo file_csv
make_csv("CINARIZINA")