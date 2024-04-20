from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(verbose=True)

class Settings(BaseSettings):
  model_config = SettingsConfigDict(env_file=".env")
  
  OPENAI_KEY: str
  DATABASE_URL: str
  EMBEDDING_MODEL: str
  LLM : str
  VECTOR_URI: str

# global instance
settings = Settings()