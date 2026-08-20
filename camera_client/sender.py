import requests

class NetworkSender:
    def __init__(self, api_url):
        self.api_url = api_url

    def send_frame(self, image_bytes):
        """Task 1.4 & 1.5: Ուղարկում է նկարը HTTP POST-ով և մշակում սխալները"""
        try:
            files = {'file': ('image.jpg', image_bytes, 'image/jpeg')}
            response = requests.post(self.api_url, files=files, timeout=5)

            if response.status_code == 200:
                print(f"✅ [Sent] Սերվերի պատասխանը: {response.json()}")
                return True
            else:
                print(f"⚠️ Սերվերի սխալ: Status {response.status_code}")
                return False

        except requests.exceptions.RequestException as e:
            # Task 1.5: Error Handling & Reconnection logic
            print(f"🔌 Կապի սխալ սերվերի հետ: Փորձում ենք կրկին... ({e})")
            return False