import requests
from bs4 import BeautifulSoup

VLC_URL = "https://www.videolan.org/vlc/"

def get_latest_vlc_version():
    try:
        response = requests.get(VLC_URL, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes

        soup = BeautifulSoup(response.text, "html.parser")
        version_span = soup.find("span", {"id": "downloadVersion"})
        if version_span and version_span.text:
            version = version_span.text.strip()
            return version
        else:
            print("Fant ikke versjonsnummer på siden.")
            return None
    except requests.RequestException as e:
        print("Nettverksfeil:", e)
        return None
    except Exception as e:
        print("Uventet feil:", e)
        return None
