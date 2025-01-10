import requests
from core.config import settings


def get_iam_token(oauth_token):
    url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
    headers = {"Content-Type": "application/json"}
    data = {"yandexPassportOauthToken": oauth_token}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["iamToken"]
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


oauth_token = settings.YC_API_KEY

try:
    iam_token = get_iam_token(oauth_token)
    print("IAM Token:", iam_token)
except Exception as e:
    print(e)

print(get_iam_token(oauth_token))
