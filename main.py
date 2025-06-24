import os
import google.generativeai as genai
from davia import Davia
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Davia()
API_KEY = "AIzaSyATLRA10J6HAH0em0ShmAHWYsK7qC6SdJ0"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

@app.task
def chat_with_waddah():
    try:
        chat = model.start_chat()
        print("Chat with Waddah AI, type 'exit' to end the chat")
        
        while True:
            try:
                user_input = input("You: ").strip()
                if user_input.lower() == "exit":
                    print("Goodbye!")
                    break
                
                if not user_input:
                    print("Please enter a message.")
                    continue
                
                response = chat.send_message(user_input)
                print(f"Waddah: {response.text}")
                
            except KeyboardInterrupt:
                print("\nChat interrupted by user. Goodbye!")
                break
            except Exception as e:
                print(f"Error during chat: {e}")
                print("You can continue chatting or type 'exit' to quit.")
                
    except Exception as e:
        print(f"Failed to initialize chat: {e}")
        return {'error': 'Failed to start chat'}

if __name__ == "__main__":
    app.run()