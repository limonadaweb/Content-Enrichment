# Content-Enrichment

   Hemos desarrollado una herramienta que consulte un tema en Wikipedia
   y permita enriquecer el contenido, lo traduzca y genere un informe 
   final en el formato .txt.

## Contexto

   Como ejercicio de responsabilidad ante el creciente uso de la 
   inteligencia artificial y el Chat GPT, presentamos un proyecto que
   tiene como objetivo principal permitir permitir que el usuario 
   extraiga información de Wikipedia y pueda mejorar su contenido y
   traducirlo a otros idiomas.

## Funcionalidades

   Se ha realizado un scraping de wikipedia para permitir al usuario
   realizar una búsqueda que le devuelva el título y los primeros 5
   párrafos del artículo.
   El sistema muestra el resultado de la búsqueda antes de preguntar
   si el usuario quiere información adicional.
   Nuestra herramienta está integrada al Chat GPT, de manera que envía
   el contenido a la Api de Open AI para enriquecer el texto.
   Si el usuario no quiere hacer uso de la Api de Open AI, entonces le 
   da la opción al usuario de decidir el idioma del contenido y enviarlo
   a la Api de Deep Translate.
   El contenido traducido se mostrará al usuario en la terminal y además
   podrá guardarlo ampliado en formato .txt o .pdf y elegir el nombre 
   del archivo.
   Las funcionalidades han sido testeadas.

## Herramientas

   - Api TextCortex
   - Api Deep Translate
   - Git/Github
   - Python 3.12
   - Python Requests
   - BeautifulSoap
   - Pytest

## Instalación

      git clone del repositorio [https://github.com/limonadaweb/Content-Enrichment

      cd <nombre de la carpeta>

      pip install -r requirements.txt

Recuerda abrir tu entorno virtual antes de la instalación

#  Colaboradores

- Valentina: [https://github.com/ItalianCookieMonster]

- Lara: [https://github.com/laradrb]

- Leire: [https://github.com/Erieltxu]

- Noemi: [https://github.com/noemipeteilh]

- Pilar: [https://github.com/pilimuino]

- Adriana: https://github.com/limonadaweb
