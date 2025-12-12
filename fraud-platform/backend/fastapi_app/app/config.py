from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Fraud Detection API"
    kafka_bootstrap_servers: str = "localhost:9092"
    kafka_topic: str = "fraud-transactions"
    
    class Config:
        env_file = ".env"


settings = Settings()
