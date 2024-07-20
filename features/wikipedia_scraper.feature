Feature: Wikipedia Scraper Fetch Page

  Scenario: Fetching lo scraper de Wikipedia con exsito
    Given un WikipediaScraper se inicializa con "test"
    When  se llama el metodo fetch_page
    Then se hace un HTTP a "https://es.wikipedia.org/wiki/test"
    And el titulo tiene que ser "Title"
    And el resultado tiene que ser un instancia de Beautiful Soup


