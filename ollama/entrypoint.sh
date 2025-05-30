#!/bin/bash
set -e

ollama serve &

OLLAMA_PID=$!

echo "Waiting for Ollama to start..."
while ! nc -z localhost 11434; do
  sleep 1
done

echo "Ollama started, checking for llama3 model..."

if ! curl -s http://localhost:11434/api/tags | grep -q '"name":"llama3:latest"'; then
  echo "llama3 model not found, pulling..."
  curl -X POST -H "Content-Type: application/json" -d '{"name":"llama3"}' http://localhost:11434/api/pull
fi

timeout=300
elapsed=0
while true; do
  response=$(curl -s http://localhost:11434/api/tags)
  echo "$response" | grep -q '"name":"llama3:latest"' && break

  if [ $elapsed -ge $timeout ]; then
    echo "Timeout reached, llama3 model not ready."
    exit 1
  fi

  echo "llama3 not ready yet, waiting 2 seconds..."
  sleep 2
  elapsed=$((elapsed + 2))
done

echo "llama3 model is ready."

wait $OLLAMA_PID
