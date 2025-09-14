#!/bin/bash
echo "Starting AI Research Agent Backend..."
uvicorn main:app --reload --host 0.0.0.0 --port 8000
