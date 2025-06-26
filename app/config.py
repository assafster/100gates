import os
from typing import List
from pydantic import BaseSettings


class Settings(BaseSettings):
    # Telegram Bot Configuration
    telegram_bot_token: str
    webhook_url: str
    
    # Database Configuration
    database_url: str
    
    # Redis Configuration
    redis_url: str = "redis://localhost:6379"
    
    # Security
    secret_key: str
    
    # Monitoring
    sentry_dsn: str = ""
    
    # Game Configuration
    question_timeout: int = 30
    total_gates: int = 100
    prize_pool_percentage: int = 69
    
    # Admin Configuration
    admin_telegram_ids: List[int] = []
    
    class Config:
        env_file = ".env"
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Parse admin IDs from comma-separated string
        if isinstance(self.admin_telegram_ids, str):
            self.admin_telegram_ids = [
                int(x.strip()) for x in self.admin_telegram_ids.split(",") 
                if x.strip().isdigit()
            ]


# Global settings instance
settings = Settings() 