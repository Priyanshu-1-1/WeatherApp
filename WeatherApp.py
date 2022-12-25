from tkinter import *
from tkinter import messagebox
import requests
from PIL import Image,ImageTk



class WeatherApp():
    def __init__(self):
        self.api="ed548398a5a1bd009de541410e85652e5c"
        self.count=0
        self.load_gui()
        self.root.mainloop()
        
    
    def load_gui(self):
        self.root=Tk()
        self.root.title("WeatherApp")
        self.root.geometry('300x400')
        self.root.resizable(0,0)
        self.p1 = PhotoImage(file = 'Images\Weather.png')
        self.root.iconphoto(False, self.p1)
        self.root.configure(background='skyblue')
        
        #Weather App Title
        self.title=Label(self.root,text="WeatherApp", font=('Arial',25,'bold'),width=15,foreground='yellow',background='green')
        self.title.grid(row = 0, column = 0, pady = 5,columnspan=3)
        
        #City Label for Search
        self.CityLabel= Label(self.root,text="City:",font=('Arial',15,'bold'),background='skyblue')
        self.CityLabel.grid(row = 1, column = 0, pady = (15,0))
        
        #Entry For City
        self.CityEntry= Entry(self.root,width=15,font=('Arial',13))
        self.CityEntry.grid(row = 1, column = 1,sticky=W,pady = (15,0))
        
        #Submit Button
        self.SubmitButton= Button(self.root,text="Search",width=8,command=self.submit)
        self.SubmitButton.grid(row=1,column=2,sticky=W,pady = (15,0))
        
        
    def submit(self):
        if self.count==1:
            self.destroy()
        self.city=self.CityEntry.get()
        self.CityEntry.delete(0,END)
        self.data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&units=metric&appid={self.api}").json()
        self.get_data()
        
    def get_data(self):
        try:
            self.cityapi=self.data['name']
            self.Country=self.data['sys']['country']
            self.Temp=str(int(self.data['main']['temp']))+"°C"
            self.main=self.data['weather'][0]['main']
            self.icon=str(self.data['weather'][0]['icon'])+"@2x.png"
            self.description="Today-   "+self.data['weather'][0]['description'].title()
            self.humidity=str(self.data['main']['humidity'])+"%"
            self.feels_like=str(self.data['main']['feels_like'])+"°C"
            self.pressure=str(self.data['main']['pressure'])+"mbar"
            self.windspeed=self.data['wind']['speed']*18/5
            self.windspeed="{:.1f}km/h".format(self.windspeed)
            self.load_data_gui()
        except:
            message=self.data['message']
            if message=='Nothing to geocode':
                messagebox.showerror("WeatherApp","Please Enter Something!!👀")
            elif message=="city not found":
                messagebox.showerror("WeatherApp","Please Enter A Valid City Name!!")
            else:
                messagebox.showerror("WeatherApp","We Will Be Back Soon✌️")
    
    def load_data_gui(self):
        self.name=Label(self.root,text=f"{self.cityapi},{self.Country}",font=("Arial",13,"bold"),background="skyblue")
        self.name.grid(row=2,column=1,pady = (8,0))  
        
        self.templabel=Label(self.root,text=self.Temp,font=("Arial",40,"bold"),background="skyblue",foreground="white")  
        self.templabel.grid(row=3,column=1,pady = (8,0))
        
        self.mainlabel=Label(self.root,text=self.main,font=("arial",15),background="skyblue")        
        self.mainlabel.grid(row=4,column=1,pady=(0,0))
        
           
        self.mage=Image.open(f"Images\{self.icon}").resize((30,30))
        self.photo = ImageTk.PhotoImage(self.mage)
        self.imagelabel=Label(image=self.photo)
        self.imagelabel.grid(row=5,column=0)
    
        self.description_label=Label(self.root,text=self.description,font=("arial",15,"bold"),background="skyblue")
        self.description_label.grid(row=5,column=1,columnspan=2,sticky=W)
        
        self.feelslike_humidity_label=Label(self.root,text=f"Feels Like \t Humidity\n{self.feels_like} \t\t {self.humidity}",font=("arial",13,"bold"),background="skyblue")
        self.feelslike_humidity_label.grid(row=6,column=0,columnspan=3)
        
        self.pressure_windspeed_label=Label(self.root,text=f"    Pressure \t Wind speed\n{self.pressure} \t {self.windspeed}",font=("arial",13,"bold"),background="skyblue")
        self.pressure_windspeed_label.grid(row=7,column=0,columnspan=3)
        self.count=1
        
    def destroy(self):
        self.name.destroy()
        self.templabel.destroy()
        self.mainlabel.destroy()
        self.description_label.destroy()
        self.imagelabel.destroy()
        self.feelslike_humidity_label.destroy()
        self.pressure_windspeed_label.destroy()
        

if __name__=='__main__':
    A=WeatherApp()
        

