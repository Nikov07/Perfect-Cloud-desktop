#!/bin/bash

echo "🚀 Starting Perfect Cloud Desktop..."
echo "====================================="

# Install Python dependencies
echo "📦 Installing Flask..."
pip3 install flask

# Setup Ngrok
echo "🔑 Setting up Ngrok..."
ngrok config add-authtoken $NGROK_AUTH_TOKEN

# Start Ngrok
echo "🌐 Starting Ngrok tunnel..."
ngrok http 8080 > /dev/null &

# Wait for Ngrok
sleep 5

# Get public URL
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o 'https://[^"]*\.ngrok\.io' | head -1)

echo "✅ PUBLIC URL: $NGROK_URL"
echo "📱 Open this in any browser!"
echo "💡 Press Ctrl+C to stop"

# Start server
python3 app.py
