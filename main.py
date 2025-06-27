#!/usr/bin/env python3
"""
Minimal test to see if Railway uses our configuration
"""
import os
import time

print("=== MINIMAL TEST ===")
print("This is our custom main.py running!")
print(f"Current directory: {os.getcwd()}")
print(f"Environment variables:")
for key, value in os.environ.items():
    if 'PORT' in key or 'RAILWAY' in key:
        print(f"  {key}={value}")

print("If you see this message, Railway is using our configuration!")
print("Starting minimal server...")

# Just keep the process running
while True:
    time.sleep(10)
    print("Still running...") 