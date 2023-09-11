import tkinter as tk
import requests

class APIClientModel:
    def __init__(self):
        self.base_url = ""

    def set_base_url(self, url):
        self.base_url = url

    def send_get_request(self, endpoint):
        try:
            response = requests.get(self.base_url + endpoint)
            return response.text
        except Exception as e:
            return str(e)

    def send_post_request(self, endpoint, data):
        try:
            response = requests.post(self.base_url + endpoint, data=data)
            return response.text
        except Exception as e:
            return str(e)

class APIClientView:
    def __init__(self, root):
        self.root = root
        self.root.title("POSTMateRest")

        self.url_label = tk.Label(root, text="URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(root)
        self.url_entry.pack()

        self.get_button = tk.Button(root, text="GET")
        self.get_button.pack()

        self.post_button = tk.Button(root, text="POST")
        self.post_button.pack()

        self.response_label = tk.Label(root, text="Response:")
        self.response_label.pack()

        self.response_text = tk.Text(root, height=10, width=40)
        self.response_text.pack()

class APIClientController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.get_button.config(command=self.send_get_request)
        self.view.post_button.config(command=self.send_post_request)

    def send_get_request(self):
        url = self.view.url_entry.get()
        response = self.model.send_get_request(url)
        self.view.response_text.delete("1.0", tk.END)
        self.view.response_text.insert(tk.END, response)

    def send_post_request(self):
        url = self.view.url_entry.get()
        data = {"key": "value"}  # Replace with your POST data
        response = self.model.send_post_request(url, data)
        self.view.response_text.delete("1.0", tk.END)
        self.view.response_text.insert(tk.END, response)

if __name__ == "__main__":
    root = tk.Tk()
    model = APIClientModel()
    view = APIClientView(root)
    controller = APIClientController(model, view)
    root.mainloop()
