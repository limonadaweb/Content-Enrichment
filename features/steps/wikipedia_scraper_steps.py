from behave import given, when, then
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup
from src.wikipedia_scraper import WikipediaScraper


@given('un WikipediaScraper se inicializa con"{search_input}"')
def step_given_initialize_scraper(context, search_input):
    context.scraper = WikipediaScraper(search_input)


@when(' se llama el metodo fetch_page')
def step_when_fetch_page_called(context):
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '<html><h1>Title</h1><div id="mw-content-text"><p>Content</p></div></html>'
        mock_get.return_value = mock_response
        context.soup = context.scraper.fetch_page()
        context.mock_get = mock_get


@then('se hace un HTTP a "https://es.wikipedia.org/wiki/{search_input}"')
def step_then_http_request_made(context, search_input):
    context.mock_get.assert_called_once_with(f"https://es.wikipedia.org/wiki/{search_input}")


@then('el titulo tiene que ser "Title"')
def step_then_title_should_be(context):
    assert context.soup.find("h1").text == "Title"


@then('el resultado tiene que ser un instancia de Beautiful Soup')
def step_then_result_instance_of_bs(context):
    assert isinstance(context.soup, BeautifulSoup)
