#!/bin/bash

# Start the backend server
uvicorn backend.app:app --reload &

# Open the frontend in a web browser
xdg-open frontend/index.html
