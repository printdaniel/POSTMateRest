import tkinter as tk
from tkinter import ttk
import requests
import json

from model import APIClientModel
from view import APIClientView
from controler import APIClientController

PostMateErest = """ 
d8888b.  .d88b.  .d8888. d888888b .88b  d88.  .d8b.  d888888b d88888b d8888b. d88888b .d8888. d888888b 
88  `8D .8P  Y8. 88'  YP `~~88~~' 88'YbdP`88 d8' `8b `~~88~~' 88'     88  `8D 88'     88'  YP `~~88~~' 
88oodD' 88    88 `8bo.      88    88  88  88 88ooo88    88    88ooooo 88oobY' 88ooooo `8bo.      88    
88~~~   88    88   `Y8b.    88    88  88  88 88~~~88    88    88~~~~~ 88`8b   88~~~~~   `Y8b.    88    
88      `8b  d8' db   8D    88    88  88  88 88   88    88    88.     88 `88. 88.     db   8D    88    
88       `Y88P'  `8888Y'    YP    YP  YP  YP YP   YP    YP    Y88888P 88   YD Y88888P `8888Y'    YP    
                                                                                                       
                                                                                                       
"""
print(PostMateErest)


if __name__ == "__main__":
    root = tk.Tk()
    model = APIClientModel()
    view = APIClientView(root)
    controller = APIClientController(model, view)
    root.mainloop()
