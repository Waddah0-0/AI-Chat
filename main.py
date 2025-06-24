from davia import Davia
import google.generativeai as genai

API_KEY = "AIzaSyATLRA10J6HAH0em0ShmAHWYsK7qC6SdJ0"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

app = Davia()

@app.task
def waddah_chat(user_input: str) -> str:
    chat = model.start_chat()
    response = chat.send_message(user_input)
    return response.text

if __name__ == "__main__":
    app.run()