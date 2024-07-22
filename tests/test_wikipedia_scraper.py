import unittest
from bs4 import BeautifulSoup
import pytest
import unittest.mock as mock
import requests
from src.wikipedia_scraper import WikipediaScraper


class TestWikipediaScraper(unittest.TestCase):

    @mock.patch('requests.get')
    def test_fetch_page_success(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.text = '<html><h1>Title</h1><div id="mw-content-text"><p>Content</p></div></html>'
        mock_get.return_value = mock_response
        scraper = WikipediaScraper('test')
        soup = scraper.fetch_page()

        mock_get.assert_called_once_with('https://es.wikipedia.org/wiki/test')
        self.assertEqual(soup.find("h1").text, "Title")
        self.assertIsInstance(soup, BeautifulSoup)

    @mock.patch('requests.get')
    def test_fetch_page_failure(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        scraper = WikipediaScraper('test')
        soup = scraper.fetch_page()

        mock_get.assert_called_once_with('https://es.wikipedia.org/wiki/test')
        self.assertIsNone(soup)

    def test_extract_content_success(self):
        html_content = "<html><h1>Title</h1><div id=\"mw-content-text\"><p>Content</p></div></html>"
        scraper = WikipediaScraper('test')
        title, text = scraper.extract_content(BeautifulSoup(html_content, 'html.parser'))
        self.assertEqual(title, "Title")
        self.assertEqual(text, "Content")

    def test_extract_content_failure(self):
        html_content = "<html><h1>Title</h1><div id=\"noarticletext\"><p>Content</p></div></html>"
        scraper = WikipediaScraper('test')
        result = scraper.extract_content(BeautifulSoup(html_content, 'html.parser'))
        self.assertIsNone(result)

    @mock.patch.object(WikipediaScraper, 'fetch_page')
    def test_scrape_success(self, mock_fetch_page):
        mock_fetch_page.return_value = BeautifulSoup(
            '<html><h1>Title</h1><div id="mw-content-text"><p>Content</p></div></html>', 'html.parser')
        scraper = WikipediaScraper('test')
        title, text = scraper.scrape()
        self.assertEqual(title, "Title")
        self.assertEqual(text, "Content")
