from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import Field
import os

DB_USER: str = os.getenv("DB_USER", "postgres")
DB_PORT: int = int(os.getenv("DB_PORT", 5432))
DB_HOST: str = os.getenv("DB_HOST", 'localhost')
DB_PASSWORD: str = 'postgres'#os.getenv("DB_PASSWORD", 'postgres')
DB_NAME: str = os.getenv("DB_NAME", 'beauty_saloon')
NUMBER_OF_INLINE_BUTTONS: int = int(os.getenv("NUMBER_OF_INLINE_BUTTONS", 2))


class EnvSettings(BaseSettings):
    PYTHON_PATH: str = Field("PYTHON_PATH")
    DB_USER: str = Field("DB_USER")
    DB_PORT: int = Field("DB_PORT")
    DB_HOST: str = Field("DB_HOST")
    DB_PASSWORD: str = Field("DB_PASSWORD")


@lru_cache
def get_env_settings() -> EnvSettings:
    return EnvSettings()
