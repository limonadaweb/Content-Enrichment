import pytest
import requests
from unittest.mock import patch
from src.text_enricher import TextEnricher


def test_enrich_text_success():
    api_key = "fake_api_key"
    input_text = "Hola"
    enriched_text = "Hola a todas las coders"

    mock_response = {
        "data": {
            "outputs": [
                {"text": enriched_text}
            ]
        }
    }

    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response

        enricher = TextEnricher(api_key)
        result = enricher.enrich_text(input_text)

        assert result == enriched_text
        mock_post.assert_called_once_with(
            "https://api.textcortex.com/v1/texts/expansions",
            json={"text": input_text},
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
        )


def test_enrich_text_failure():
    api_key = "fake_api_key"
    input_text = "Hola"

    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 400

        enricher = TextEnricher(api_key)
        result = enricher.enrich_text(input_text)

        assert result == input_text
        mock_post.assert_called_once_with(
            "https://api.textcortex.com/v1/texts/expansions",
            json={"text": input_text},
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
        )