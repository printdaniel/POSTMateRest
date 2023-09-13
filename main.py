import tkinter as tk
from tkinter import ttk, PhotoImage
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
        self.root.configure(bg="#458588")

        tab_control = ttk.Notebook(root)
        style = ttk.Style()
        style.configure("Tab.TFrame", background="#3c3836", foreground="red")

        tab_get = ttk.Frame(tab_control, style="Tab.TFrame")
        tab_post = ttk.Frame(tab_control, style="Tab.TFrame")
        tab_get.pack_propagate(False)
        tab_post.pack_propagate(False)

        tab_control.add(tab_get, text="GET")
        tab_control.add(tab_post, text="POST")
        tab_control.pack(expand=1, fill="both")
        
        self.url_label = tk.Label(tab_get, text="URL:", bg="#3c3836", fg="#cc241d")
        self.url_label.pack()

        self.url_get_entry = tk.Entry(tab_get, bg="#8ec07c",width=110)
        self.url_get_entry.pack()

        # Boton GET
        self.image_get = PhotoImage(file="get_img.gif")
        self.get_button = tk.Button(tab_get, image=self.image_get)
        #self.get_button = tk.Button(tab_get, text="GET")
        self.get_button.pack()

        # POST section
        self.url_label = tk.Label(tab_post, text="URL:", bg="#3c3836", fg="#cc241d")
        self.url_label.pack()

        self.url_post_entry = tk.Entry(tab_post)
        self.url_post_entry.pack()

        self.post_button = tk.Button(tab_post, text="POST")
        self.post_button.pack()

        # RESPONSE Section
        self.response_label = tk.Label(root, text="Response:", bg="#458588", fg="#cc241d")
        self.response_label.pack()

        self.response_text = tk.Text(root, height=20, width=50)
        self.response_text.pack()

class APIClientController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.get_button.config(command=self.send_get_request)
        self.view.post_button.config(command=self.send_post_request)

    def send_get_request(self):
        url = self.view.url_get_entry.get()        
        response = self.model.send_get_request(url)
        print(response)
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
