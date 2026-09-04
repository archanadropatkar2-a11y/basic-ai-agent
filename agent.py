# My first GitHub update
import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": input("You: ")}
    ]
)

print(response["message"]["content"])
# AI Agent project - GitHub test