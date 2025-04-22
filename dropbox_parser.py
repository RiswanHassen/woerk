
import requests
from bs4 import BeautifulSoup

def get_dropbox_folder_files(dropbox_url):
    try:
        if '?dl=0' in dropbox_url:
            dropbox_url = dropbox_url.replace('?dl=0', '?dl=1')
        elif '?dl=1' not in dropbox_url:
            dropbox_url += '?dl=1'

        headers = {
            'User-Agent': 'Mozilla/5.0'
        }

        response = requests.get(dropbox_url, headers=headers)
        if response.status_code != 200:
            return ["[Fehler] Dropbox-Link nicht erreichbar (Status {})".format(response.status_code)]

        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('span', {'class': 'filename-text'})
        if not items:
            items = soup.find_all('div', {'class': 'file-name'})

        files = [item.get_text(strip=True) for item in items]
        return files if files else ["[Hinweis] Keine Dateien gefunden oder Layout unerwartet."]
    except Exception as e:
        return [f"[Fehler beim Parsen] {str(e)}"]
