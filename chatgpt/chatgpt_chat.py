from IPython.core.display import Markdown
from IPython.core.display_functions import display
from openai import OpenAI


class ChatGPT:
    def __init__(self, key: str, model: str):
        self.__client = OpenAI(api_key=key)
        self.__model = model
        self.__messages = []

    def chat(self, prompt: str, seed: int | None = None):
        self.__messages.append({"role": "user", "content": prompt})

        response = self.__client.chat.completions.create(
            model=self.__model,
            messages=self.__messages,
            seed=seed,
            temperature=0
        )
        answer = response.choices[0].message.content
        self.__messages.append({"role": "assistant", "content": answer})
        return answer

    def chatAndDisplay(self, prompt: str, seed: int | None = None):
        answer = self.chat(prompt, seed)
        display(Markdown(answer))

    def clearHistory(self):
        self.__messages = []
        display(Markdown("**History Cleared!**"))