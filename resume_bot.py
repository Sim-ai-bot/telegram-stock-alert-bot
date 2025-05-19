import requests

API_KEY = "rnd_..."  # <- вставь свой Render API ключ
SERVICE_ID = "srv-..."  # <- вставь ID сервиса

headers = {
    "Authorization": f"Bearer {API_KEY}"
}
url = f"https://api.render.com/v1/services/{SERVICE_ID}/resume"

r = requests.post(url, headers=headers)
print("▶️ Облачный бот снова активен!" if r.status_code == 200 else "Ошибка активации:", r.text)
