import requests

class NetworkSender:
    def __init__(self, api_url):
        self.api_url = api_url

    def send_frame(self, image_bytes):

        try:
            files = {'file': ('image.jpg', image_bytes, 'image/jpeg')}
            response = requests.post(self.api_url, files=files, timeout=5)

            if response.status_code == 200:
                print(f"[Sent] Server response: {response.json()}")
                return True
            else:
                print(f"Server error : Status {response.status_code}")
                return False

        except requests.exceptions.RequestException as e:
            # Task 1.5: Error Handling & Reconnection logic
            print(f"Connection error with the server. Retrying...... ({e})")
            return False