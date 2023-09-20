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

    def send_post_request(self, endpoint, data = None):
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
            if data != None:
                response = requests.post(self.base_url + endpoint, data=data)
                return response.text
            else:
                response = requests.post(self.base_url + endpoint)
                return response.text
        except Exception as e:
            return str(e)


    def send_put_request(self, endpoint, data):
        """ 
        Realiza una solicitud PUT a la API.
        Args:
            endpoint(str): Endpoint de la API al que se requiere la solicitud.
            data: Los datos que se enviarán en la solicitudo PUT.
        Returns:
            str: La respuesta de la solicitud PUT como texto.
        Raises:
            Exception: Si ocurre algún error durante la solicitud.
        """
        try:
            if data:
                response = requests.put(self.base_url + endpoint, data=data)
                return response.text
            else:
                response = requests.put(self.base_url + endpoint)
            return response.text
        except Exception as e:
            return str(e)
