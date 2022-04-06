from src.cima.crawler import Crawler

scraping = Crawler("Codeina")
lista = scraping.get_list_references()

#Ventaja tarda menos no tiene que comprobar todos los resultados con este metodo
#numero = scraping.get_amount_results()

#print(numero)
print(lista)
