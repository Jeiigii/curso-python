
#Bibliotecas que se van a utilizar en el scrapping
import sqlite3
import requests
from bs4 import BeautifulSoup

#Establecer conexion con la bese datos
conn = sqlite3.connect("Datos.db")
