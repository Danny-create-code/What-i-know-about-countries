from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

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
    for x in range(0, len(data)):
        if clicked.get() == countries[x]:
            # country
            countries_label["text"] = countries[x]
            # timezones
            region_label["text"] = f"Region: {regions[x]}"
            timezones_str = str(timezones[x]) 
            timezones_result = timezones_str[2:-2]
            
            timezone_label["text"] = timezones_result
            # populations
            populations_int = int(populations[x])
            populations_result = format(populations_int, " ,")
            populations_label["text"] = f"Population: {populations_result}"
            # image
            url_png = flags[x]
            response = requests.get(url_png)
            image = Image.open(BytesIO(response.content))
            photo = ImageTk.PhotoImage(image)
            flag_label.config(image=photo)
            flag_label.photo = photo
            
                

# information obtained
countries = []
timezones = []
populations = []
regions = []
maps = []
flags = []

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

# labels
countries_label = Label(text=" ", font=("Helverica",20, "bold"))
countries_label.pack(pady=5)
region_label = Label(text=" ", font=("Helvetica", 20))
region_label.pack(pady=2)
timezone_label = Label(text=" ", font=("Helvetica", 20))
timezone_label.pack(pady=2)
populations_label = Label(text=" ", font=("Helvetica", 20))
populations_label.pack(pady=2)

flag_label = Label(window)
flag_label.pack(pady=10)





# main loop
window.mainloop()

