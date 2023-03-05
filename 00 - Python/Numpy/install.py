from transformers import pipeline

chatbot = pipeline("text-generation", model="gpt2")

while True:
    user_input = input("Anda: ")
    if user_input.lower() == "stop":
        break
    response = chatbot(user_input)
    print("Chatbot:", response[0]['generated_text'])