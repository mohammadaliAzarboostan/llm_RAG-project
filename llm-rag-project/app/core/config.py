from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):

    METIS_API_KEY: str
    METIS_BASE_URL: str
    METIS_MODEL: str

    CHROMA_PATH: str = "./data/chroma"

    EMBEDDING_MODEL:str = "sentence-transformers/all-MiniLM-L6-v2"

    CHUNK_SIZE:int = 800
    CHUNK_OVERLAP: int = 150

    TOP_K:int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()
