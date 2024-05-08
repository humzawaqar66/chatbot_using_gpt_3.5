import openai
import re

openai.api_key = 'your API key'

context = "You are an helpful assisant. Your name is Humza"
Messages = [
        {"role": "system", "content": context},

]
def generate_response(user_input, chat_completion_model):
    
    Messages.append({"role": "user", "content": user_input})

    response = chat_completion_model.create(
        model="gpt-3.5-turbo",
        messages = Messages
            
    )
    analysis = response.choices[0].message.content.strip()
    Messages.append({"role": "assistant", "content": analysis})
    # print(Messages)
    
    return analysis

def main():
    chat_completion_model = openai.ChatCompletion()

    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            print("Chatbot exits.")
            break
        #user_input = re.sub(r"[^a-zA-Z0-9\s]", " ", user_input.lower())
        response = generate_response(user_input, chat_completion_model)
        print("Bot:", response)

if __name__ == "__main__":
    main()
