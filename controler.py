import tkinter as tk
from tkinter import ttk

class APIClientController:
    def __init__(self, model, view):
        """
        Maneja la solicitud POST al hacer clic en el botón correspondiente.

        Obtiene la URL y los datos JSON desde la vista, realiza la solicitud POST
        a través del modelo, actualiza la vista con la respuesta y establece un
        mensaje de estado.
        """
        self.model = model  # instancia del modelo
        self.view = view  # instancia de la vista

        self.view.get_button.config(command=self.send_get_request)
        self.view.post_button.config(command=self.send_post_request)

    def send_get_request(self):
        """
        Maneja la solicitud GET al hacer clic en el botón correspondiente.

        Obtiene la URL desde la vista, realiza la solicitud GET a través del modelo,
        actualiza la vista con la respuesta y establece un mensaje de estado.
        """
        url = self.view.url_get_entry.get()
        response = self.model.send_get_request(url)

        # Actualizar el mensaje de estado en la vista
        self.view.mensaje.set("GET Exitoso")

        # Borra la respuesta y muestra para dejar la nueva
        self.view.response_text.delete("1.0", tk.END)
        self.view.response_text.insert(tk.END, response)

    def send_post_request(self):
        """
        Maneja la solicitud POST al hacer clic en el botón correspondiente.

        Obtiene la URL y los datos JSON desde la vista, realiza la solicitud POST
        a través del modelo, actualiza la vista con la respuesta y establece
        un mensaje de estado.
        """
        url = self.view.url_post_entry.get()
        data = self.view.data_text.get("1.0", "end-1c")

        # Convertir la cadena JSON en un diccionario de Python
        parametros = json.loads(data)
        response = self.model.send_post_request(url, parametros)
        self.view.response_text.delete("1.0", tk.END)
        self.view.response_text.insert(tk.END, response)

        # Mensaje
        self.view.mensaje.set("POST realizado")


