import tkinter as tk
from tkinter import ttk
import requests
import json

from model import APIClientModel
from view import APIClientView
from controler import APIClientController


if __name__ == "__main__":
    root = tk.Tk()
    model = APIClientModel()
    view = APIClientView(root)
    controller = APIClientController(model, view)
    root.mainloop()
