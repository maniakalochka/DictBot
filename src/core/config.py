from pathlib import Path
from typing import Literal, Optional
from pydantic import ConfigDict, model_validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    # --- app settings --- #
    APP_NAME: str = "DictionaryBot"
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    MODE: Literal["PROD", "DEV", "TEST"] = "TEST"

    # --- database settings --- #
    DB_URL: Optional[str] = "sqlite+aiosqlite:///./database.db"
    TEST_DB_URL: Optional[str] = "sqlite+aiosqlite:///./test_database.db"

    DB_NAME: str
    TEST_DB_NAME: str

    # --- telegram settings --- #
    TELEGRAM_TOKEN: str

    model_config = ConfigDict(env_file=str(env_path))


settings = Settings()
