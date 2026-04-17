
from transformers import pipeline

chatbot = pipeline(
    "text2text-generation",
    model="google/flan-t5-large"
)

print("AI Chatbot Started (type 'exit' to stop)")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    prompt = "Answer the question: " + user

    response = chatbot(prompt, max_length=100)

    print("Bot:", response[0]['generated_text'])

