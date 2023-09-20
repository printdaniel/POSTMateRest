import requests
import tkinter as tk
from tkinter import ttk

class APIClientModel:
    def __init__(self):
        """ 
        Constructor de la clase APIClientModel
        Inicializa el objeto APIClientModel con una URL base vacía.
        """
        self.base_url = ""

    def set_base_url(self, url):
        """ 
        Establece la URL base para las solicitudes a la API.
        Args:
            urls (str): La URL para la API.
        """
        self.base_url = url

    def send_get_request(self, endpoint):
        """ 
        Realiza una solicitudo GET a la API.
        Args:
            endpoint (str): Endpoint de la API que se requiere
        Returns:
            str: La respuesta de la solicitud GET como texto.
        Raises:
            Exception: Si ocurre algún error durante la solicitud.
        """
        try:
            response = requests.get(self.base_url + endpoint)
            return response.text
        except Exception as e:
            return str(e)

    def send_post_request(self, endpoint, data):
        """ 
        Realiza una solicitud POST a la API.
        Args:
            endpoint(str): Endpoint de la API al que se requiere la solicitud.
            data: Los datos que se enviarán en la solicitudo POST.
        Returns:
            str: La respuesta de la solicitud POST como texto.
        Raises:
            Exception: Si ocurre algún error durante la solicitud.
        """
        try:
            response = requests.post(self.base_url + endpoint, data=data)
            return response.text
        except Exception as e:
            return str(e)


class APIClientView:
    def __init__(self, root):
        """ 
        Constructor de clase APIClientView.
        Args:
            root: La ventana principal de Tkinter.
        """
        self.root = root
        self.root.title("POSTMateRest")
        self.mensaje = tk.StringVar()
        self.mensaje.set("Bienvenido a POSTMateRest v 1.0")
        self.root.configure(bg="#458588")

        # Info Label
        self.info_label = tk.Label(
            self.root, textvariable=self.mensaje, bg="#458588", fg="#d79921"
        )
        self.info_label.pack()

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

        self.url_get_entry = tk.Entry(tab_get, bg="#8ec07c", width=110)
        self.url_get_entry.pack()

        # Boton GET
        # self.image_get = PhotoImage(file="get_img.gif")
        # self.get_button = tk.Button(tab_get, image=self.image_get)
        self.get_button = tk.Button(tab_get, text="GET")
        self.get_button.pack()

        # POST section
        self.url_label = tk.Label(tab_post, text="URL:", bg="#3c3836", fg="#cc241d")
        self.url_label.pack()

        self.url_post_entry = tk.Entry(tab_post, bg="#8ec07c", width=110)
        self.url_post_entry.pack()

        # DATA Entry
        self.data_label = tk.Label(
            tab_post, text="Parametros", bg="#3c3836", fg="#cc241d"
        )
        self.data_label.pack()

        self.data_text = tk.Text(tab_post, width=50, height=10, bg="#8ec07c")
        self.data_text.pack()

        self.post_button = tk.Button(tab_post, text="POST")
        self.post_button.pack()

        # RESPONSE Section
        self.response_label = tk.Label(
            root, text="Response:", bg="#458588", fg="#cc241d"
        )
        self.response_label.pack()

        self.response_text = tk.Text(root, height=20, width=50, bg="#d79921")
        self.response_text.pack()


