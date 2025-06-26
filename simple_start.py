#!/usr/bin/env python3
import uvicorn
from test_app import app

if __name__ == "__main__":
    print("Starting server on port 8000")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info") 