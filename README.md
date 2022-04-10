# Práctica 1: Medicine Scraper

### Descripción

Este proyecto forma parte de la asignatura *Tipología y Ciclo de vida de los Datos*, dentro del plan de estudios del Máster de Ciencia de Datos de la Universitat Oberta de Catalunya.

En él, se trabaja el concepto del Web Scraping mediante librerías de Python como Selenium y Beautiful Soup. En concreto, el objetivo de este proyecto es el de obtener datos de la web Cima de medicamentos para descargarlos y guardar el dataset en un csv final.

### Autores

Este proyecto ha sido realizado por **Juan Luis González Rodríguez** y **Rocío González Martínez**, alumnos del Máster de Ciencia de Datos de la UOC.  

### Estructura del proyecto

* **src/cima/searcher.py**: configura la clase *CimaWebConfigurator* con los parámetros y funciones de la web del medicamento.
* **src/cima/crawler.py**: configuración de la clase *Crawler*, que representa el "rastreador" del medicamento por la Web de Cima.
* **src/cima/medicament.py**: configuración de las clases *WebMedicament* y *Medicament*. La primera hace referencia a la página web en la que se describe el medicamento y la segunda, a toda la información del medicamento en sí.
* **src/file_csv.py**: fichero que guarda el código para crear el CSV con la información recolectada en las clases anteriores.
* **./main.py**: fichero principal del programa. En este punto se debe definir el medicamento a buscar y se obtendrá el CSV buscado.
* **test/testing.py**: fichero de pruebas y ejemplos de las clases y funciones anteriores.
* **results/**: directorio para guardar los CSV del programa.

### Nota

Los datos obtenidos mediante el presente proyecto tienen una fecha de actualización de abril de 2022. Sin embargo, hay que tener en cuenta que la fecha de actualización de datos de los próximos conjuntos de datos obtenidos, dependerán del usuario y la fecha de extracción de datos.
