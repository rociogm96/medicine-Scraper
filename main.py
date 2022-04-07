from src.cima.crawler import Crawler
import src.cima.medicament as medicament

# Ejemplos crawler y searcher
scraping = Crawler("Codeina")

lista = scraping.get_list_references()

# Ventaja tarda menos no tiene que comprobar todos los elementos con este método
numero = scraping.get_amount_results()

print(numero)
print(lista)
print(len(lista))

#Ejemplo módulo medicament
medicamentoA = medicament.Medicament('84781')
print(medicamentoA.name)
print(medicamentoA.characteristics)
print(medicamentoA.atc_codes)
print(medicamentoA.company)

