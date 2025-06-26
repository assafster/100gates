#!/usr/bin/env python3
import os
import uvicorn
from test_app import app

if __name__ == "__main__":
    # Get port from environment variable with fallback
    port_str = os.getenv("PORT", "8000")
    try:
        port = int(port_str)
    except ValueError:
        print(f"Invalid PORT value: {port_str}, using default 8000")
        port = 8000
    
    print(f"Starting server on port {port}")
    print(f"Environment variables: PORT={os.getenv('PORT', 'NOT_SET')}")
    
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info") 