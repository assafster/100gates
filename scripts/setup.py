#!/usr/bin/env python3
"""
Setup script for 100 Gates to Freedom Bot
Initializes database and seeds questions
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import engine, SessionLocal
from app.models import Base
from alembic.config import Config
from alembic import command
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_database():
    """Setup database tables"""
    try:
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Database tables created successfully!")
    except Exception as e:
        logger.error(f"❌ Error creating database tables: {e}")
        return False
    return True

def run_migrations():
    """Run database migrations"""
    try:
        logger.info("Running database migrations...")
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")
        logger.info("✅ Database migrations completed!")
    except Exception as e:
        logger.error(f"❌ Error running migrations: {e}")
        return False
    return True

def main():
    """Main setup function"""
    logger.info("🚀 Setting up 100 Gates to Freedom Bot...")
    
    # Setup database
    if not setup_database():
        logger.error("Failed to setup database")
        sys.exit(1)
    
    # Run migrations
    if not run_migrations():
        logger.error("Failed to run migrations")
        sys.exit(1)
    
    # Seed questions
    try:
        logger.info("Seeding questions...")
        from scripts.seed_questions import seed_questions
        seed_questions()
    except Exception as e:
        logger.error(f"❌ Error seeding questions: {e}")
        sys.exit(1)
    
    logger.info("🎉 Setup completed successfully!")
    logger.info("Next steps:")
    logger.info("1. Set up your environment variables in .env file")
    logger.info("2. Get your Telegram bot token from @BotFather")
    logger.info("3. Deploy to Render/Railway or run locally with: uvicorn app.main:app --reload")

if __name__ == "__main__":
    main() 