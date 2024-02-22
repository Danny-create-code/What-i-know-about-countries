from tkinter import *
import requests

# imported data
url = "https://restcountries.com/v3.1/all"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
data = response.json()

# window setting
window = Tk()
window.minsize(640, 480)
window.resizable(False, False)
window.title('countries')

# main loop
window.mainloop()