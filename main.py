#!/usr/bin/env python3
"""
Main entry point for Railway deployment
"""
import os
import sys
import uvicorn

# Import the FastAPI app from the backup file
try:
    # Add the app directory to the path
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))
    
    # Import the app from the backup file
    import main_backup
    app = main_backup.app
    print("✓ Successfully imported FastAPI app from main_backup.py")
except Exception as e:
    print(f"✗ Error importing FastAPI app: {e}")
    sys.exit(1)

if __name__ == "__main__":
    # Get port from environment variable with fallback
    port_str = os.getenv("PORT", "3000")
    try:
        port = int(port_str)
    except ValueError:
        print(f"Invalid PORT value: {port_str}, using default 3000")
        port = 3000
    
    print(f"Starting FastAPI server on port {port}")
    print(f"Environment variables: PORT={os.getenv('PORT', 'NOT_SET')}")
    
    # Start the server
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info") 