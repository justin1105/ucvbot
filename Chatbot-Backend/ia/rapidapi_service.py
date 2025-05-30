import requests

RAPIDAPI_URL = "https://chatgpt-42.p.rapidapi.com/conversationgpt4"
RAPIDAPI_KEY = "5dd49fa873msha7a3bcac00a9e15p1c26eejsn40605ee97076"

HEADERS = {
    "content-type": "application/json",
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com"
}

def get_bot_response(message, history=None):
    payload = {
        "messages": history if history else [
            {"role": "user", "content": message}
        ]
    }
    response = requests.post(RAPIDAPI_URL, json=payload, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return data["result"]
    else:
        return f"Error: {response.status_code} - {response.text}" 