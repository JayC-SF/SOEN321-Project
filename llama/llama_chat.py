import requests
from IPython.display import Markdown, display
from urllib.parse import urljoin

class LlamaChat:
    def __init__(self, base_api_url: str, model: str):
        # define if the class object will retain history of chat
        self.__url = urljoin(base_api_url, "api/chat")
        self.__history = []
        self.__model = model
        
    def chat(self, prompt: str, seed:int | None = None): 
        self.__history.append({"role": "user","content": prompt})
        
        jsonPayload = {
            "model": self.__model,
            "messages": self.__history,
            "stream":False
        }
        # if seed add it to payload
        if seed != None:
            jsonPayload['options'] = {"seed":seed}
            
        # request to llama
        res = requests.post(
            self.__url,
            json=jsonPayload
        )
        response = res.json()
        # extend the chat history
        model_response = response['message']
        self.__history.append(model_response)
        return model_response['content']
    
    # chats and display to output
    def chatAndDisplay(self, prompt: str, seed:int | None = None):
        answer = self.chat(prompt, seed)
        display(Markdown(answer))
        
    
