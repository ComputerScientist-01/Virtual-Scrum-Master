import chatgpt

class ChatGPTAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.chatgpt_instance = chatgpt.ChatGPT(api_key)

    def ask(self, prompt):
        response = self.chatgpt_instance.ask(prompt)
        return response