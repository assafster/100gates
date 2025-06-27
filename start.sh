#!/bin/bash

echo "=== START.SH ==="
echo "This is our custom start script!"
echo "Current directory: $(pwd)"
echo "Environment variables:"
env | grep -E "(PORT|RAILWAY)" || echo "No PORT or RAILWAY variables found"

echo "Starting our custom main.py..."
exec python main.py 