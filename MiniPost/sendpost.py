import requests

APP_HOST_PROTOCOL = "HTTP"
APP_HOST_IP = "localhost"
APP_HOST_PORT = 5001

url = f"{APP_HOST_PROTOCOL}://{APP_HOST_IP}:{APP_HOST_PORT}/submit"

payload = {"data": "hello world!"}

try:
    r = requests.post(url, json=payload)
    if r.status_code == 200:
        print(f"SUCCESS! POST to {APP_HOST_PROTOCOL}://{APP_HOST_IP}:{APP_HOST_PORT} OK!")
    else:
        print(f"ERROR! POST to {APP_HOST_PROTOCOL}://{APP_HOST_IP}:{APP_HOST_PORT} NOT OK!")
except Exception as error:
    print(f"Failed to POST! {str(error)}")
