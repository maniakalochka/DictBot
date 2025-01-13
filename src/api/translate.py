from .iam_token import get_cached_iam_token, oauth_token
import requests
from core.config import settings


def get_translation(iam_token, random_word, source_lang="en", target_lang="ru"):
    iam_token = get_cached_iam_token(oauth_token)
    url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
    headers = {
        "Authorization": f"Bearer {iam_token}",
        "Content-Type": "application/json",
    }
    data = {
        "folderId": settings.FOLDER_ID,
        "texts": [random_word],
        "sourceLanguageCode": source_lang,
        "targetLanguageCode": target_lang,
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["translations"][0]["text"]
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")
