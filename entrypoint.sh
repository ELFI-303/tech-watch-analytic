/bin/ollama serve &

pid=$!

sleep 5

echo "🔴 Retrieve llama3.2:3b model..."
ollama pull llama3.2:3b
echo "🟢 Done!"

wait $pid