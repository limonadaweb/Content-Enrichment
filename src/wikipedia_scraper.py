import requests
from bs4 import BeautifulSoup


class Wikipedia_scraper:
    def __init__(self, url, input):
        self.url = url
        self.input = input

    def scraper(self):
        try:
            response = requests.get(f"{self.url}{self.input}")
            if response.status_code != 200:
                raise requests.HTTPError("Error en la llamada HTTP")
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find("h1").text
            mw_content = soup.find(id="mw-content-text")
            if mw_content.find(id="noarticletext"):
                raise Exception("No se ha encontrado el árticulo seleccionado")

            elif mw_content.find("div", class_="mw-disambig-page"):

                raise Exception("Se ha encontrado una página de desambiguación")

            else:
                texts = mw_content.find_all("p", limit=5)
                text = ""
            for p in texts:
                t = p.get_text()
                text = text + t

            return title, text
        except Exception as e:
            print(e)
