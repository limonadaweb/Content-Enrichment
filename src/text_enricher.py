
import requests


class TextEnricher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.textcortex.com/v1/texts/expansions"

    def enrich_text(self, text):
        """
        Envía el texto a la API de TextCortex AI para enriquecerlo.

        Args:
            text (str): El texto que se va a enriquecer.

        Returns:
            str: El texto enriquecido o el texto original en caso de error.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "text": text
        }

        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            response.raise_for_status()
            enriched_data = response.json()
            outputs = enriched_data.get('data', {}).get('outputs', [])
            if outputs and isinstance(outputs[0], dict):
                return outputs[0].get('text', text)
            return text
        except requests.RequestException as e:
            print(f"Error al enriquecer el texto: {e}")
            return text
