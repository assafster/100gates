from fastapi import FastAPI
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Test App",
    description="Simple test application",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Root endpoint"""
    logger.info("Root endpoint called")
    return {"message": "Test app is running!", "port": os.getenv("PORT", "8000")}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    logger.info("Health check called")
    return {"status": "healthy", "port": os.getenv("PORT", "8000")}

@app.get("/debug")
async def debug():
    """Debug endpoint to check environment"""
    logger.info("Debug endpoint called")
    return {
        "port": os.getenv("PORT", "8000"),
        "environment": dict(os.environ),
        "status": "running"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    logger.info(f"Starting server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port) 