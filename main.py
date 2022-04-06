from src.cima.crawler import Crawler

scraping = Crawler("Codeina")

lista = scraping.get_list_references()

# Ventaja tarda menos no tiene que comprobar todos los elementos con este método
numero = scraping.get_amount_results()

print(numero)
print(lista)
print(len(lista))
