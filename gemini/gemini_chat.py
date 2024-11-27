import requests
from IPython.display import Markdown, display

class GeminiChat:
    def __init__(self, key: str, model: str):
        self.__url=f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        self.__key = key
        self.__history = []
        
    def chat(self, prompt:str, seed: int | None = None):
        # add new prompt in the chat history
        self.__history.append(
            {
                "role": "user",
                "parts": [ { "text": prompt } ] 
            }
        )
        # request to gemini
        res = requests.post(
            self.__url, 
            params={"key":self.__key}, 
            json={
                "contents": self.__history,
                "generationConfig": {
                    "seed": seed
                }
            }
        )
        response = res.json()
        # extend the chat history
        model_response = response['candidates'][0]['content']
        self.__history.append(model_response)
        return model_response['parts'][0]['text']

    def chatAndDisplay(self, prompt: str, seed:int | None):
        answer = self.chat(prompt, seed)
        display(Markdown(answer))
        