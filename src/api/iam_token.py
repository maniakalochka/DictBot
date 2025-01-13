import requests
import time
from core.config import settings

iam_token = None
token_timestamp = None


def get_iam_token(oauth_token):
    url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
    headers = {"Content-Type": "application/json"}
    data = {"yandexPassportOauthToken": oauth_token}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["iamToken"]
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


def get_cached_iam_token(oauth_token):
    global iam_token, token_timestamp

    # Проверяем, если токен существует и не истек (дается 1 час)
    if iam_token and token_timestamp and (time.time() - token_timestamp < 3600):
        return iam_token

    # Генерируем новый токен
    iam_token = get_iam_token(oauth_token)
    token_timestamp = time.time()  # Обновляем время получения токена
    return iam_token


oauth_token = settings.YC_API_KEY

try:
    iam_token = get_iam_token(oauth_token)
    print("IAM Token:", iam_token)
except Exception as e:
    print(e)
