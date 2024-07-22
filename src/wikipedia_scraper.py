import requests
from bs4 import BeautifulSoup


class WikipediaScraper:
    def __init__(self, search_input):
        self.url = f"https://es.wikipedia.org/wiki/{search_input}"

    def fetch_page(self):
        try:
            response = requests.get(self.url)
            if response.status_code != 200 and response.status_code != 404:
                raise requests.HTTPError("Error en la llamada HTTP")
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Error al recuperar la página de Wikipedia: {e}")
            return None

    @staticmethod
    def extract_content(soup):
        try:
            title = soup.find("h1").text
            mw_content = soup.find(id="mw-content-text")
            if mw_content.find(id="noarticletext"):
                raise Exception("No se ha encontrado el árticulo seleccionado")
            elif mw_content.find("div", class_="mw-disambig-page"):
                raise Exception("Se ha encontrado una página de desambiguación")
            else:
                texts = mw_content.find_all("p", limit=5)
                text = "".join(p.get_text() for p in texts)
                return title, text
        except Exception as e:
            print(f"Error al extraer el contenido: {e}")
            return None

    def scrape(self):
        soup = self.fetch_page()
        if soup is not None:
            return self.extract_content(soup)
        return None
