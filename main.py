from src.wikipedia_scraper import Wikipedia_scraper
url = "https://es.wikipedia.org/wiki/"
input = "Java"

wikipedia_scraper = Wikipedia_scraper(url, input)
print(wikipedia_scraper.scraper())