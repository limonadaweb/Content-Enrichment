import requests


def get_enriched_content(content):
    GEMINIAI_API_URL = "https://api.geminiai.com/enrich"
    GEMINIAI_API_KEY = "AIzaSyDHVXDRTFuWHAASr1tmuv4Oh7Jnn5GplFA"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GEMINIAI_API_KEY}"
    }

    payload = {
        "text": content
    }

    try:
        response = requests.post(GEMINIAI_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        enriched_content = response.json().get("enriched_text", "")
        return enriched_content

    except requests.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # Example
    content = 'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.'

    enriched_content = get_enriched_content(content)
    if enriched_content:
        print(f"Contenido Enriquecido: {enriched_content}")


