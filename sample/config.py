from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class _Config(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")

    API_KEY: SecretStr = Field(default=None)


config = _Config()
