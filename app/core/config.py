from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "RAGConnect"
    app_version: str = "0.1.0"

    rag_provider: str = "ragflow"

    ragflow_base_url: str = "http://localhost:9380"
    ragflow_api_key: str = ""
    ragflow_chat_id: str = ""
    ragflow_dataset_id: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()