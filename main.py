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

# function after pressed button
def selected():
    pass


# information obtained
countries = []
timezones = []
populations = []
regions = []
maps = []
flags = []
flags_text = []

for x in range(0, len(data)):
    countries.append(data[x]["name"]["official"])
    timezones.append(data[x]["timezones"])
    populations.append(data[x]["population"])
    regions.append(data[x]["region"])
    maps.append(data[x]["maps"]["googleMaps"])
    flags.append(data[x]["flags"]["png"])

# dropdown menu
clicked = StringVar()
clicked.set("choose a country")
drop = OptionMenu(window, clicked, *countries).pack()

# confirmation button
my_btn = Button(window, text='select from list', command=selected).pack()


# main loop
window.mainloop()

