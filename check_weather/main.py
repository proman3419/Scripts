from tkinter import *
import tkinter.messagebox as messagebox
import requests
import json

class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    self._frame = None
    self.switch_frame(StartPage)
    self.title('Check Weather')

  def switch_frame(self, frame_class, values=None):
    self.geometry('')

    if values is None:
      new_frame = frame_class(self)
    else:
      new_frame = frame_class(self, values)

    if self._frame is not None:
      self._frame.destroy()

    self._frame = new_frame
    self._frame.pack()


class StartPage(Frame):
  def __init__(self, master):
    Frame.__init__(self, master)

    city = Label(self, text='City')
    country = Label(self, text='Country')

    city_e = Entry(self)
    country_e = Entry(self)

    apply_b = Button(self, text='Apply', command=lambda: self.get_weather(master, city_e.get(), country_e.get()))

    city.grid(row=0, padx=(10, 5), pady=(10, 5), sticky=E)
    city_e.grid(row=0, column=1, padx=(5, 10), pady=(10, 5))
    country.grid(row=1, padx=(10, 5), pady=(5, 5), sticky=E)
    country_e.grid(row=1, column=1, padx=(5, 10), pady=(5, 5))
    apply_b.grid(row=2, columnspan=2, pady=(5, 10))

  def get_weather(self, master, city, country):
    link = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&id=524901&APPID=b904f237ed7877fd94764cbbe375ff87'.format(city, country)
    r = requests.get(link)
    c = json.loads(r.text)

    if r.status_code == 200:
      values = []
      values.append(c['name'])
      values.append(c['sys']['country'])
      values.append(str(c['main']['temp']) + ' °C')
      values.append(str(c['main']['pressure']) + ' hPa')
      values.append(str(c['main']['humidity']) + ' %')
      values.append(str(c['wind']['speed']) + ' m/s')
      values.append(str(c['clouds']['all']) + ' %')

      master.switch_frame(WeatherPage, values)
    else:
      messagebox.showerror('Error', 'Couldn\'t find a city matching the passed criteria')


class WeatherPage(Frame):
  def __init__(self, master, values):
    Frame.__init__(self, master)

    city = Label(self, text='City')
    country = Label(self, text='Country')
    temperature = Label(self, text='Temperature')
    pressure = Label(self, text='Pressure')
    humidity = Label(self, text='Humidity')
    wind_speed = Label(self, text='Wind speed')
    clouds = Label(self, text='Clouds')

    city_v = Label(self, text=values[0])
    country_v = Label(self, text=values[1])
    temperature_v = Label(self, text=values[2])
    pressure_v = Label(self, text=values[3])
    humidity_v = Label(self, text=values[4])
    wind_speed_v = Label(self, text=values[5])
    clouds_v = Label(self, text=values[6])

    return_b = Button(self, text='Return', command=lambda: master.switch_frame(StartPage))

    city.grid(row=0, padx=(10, 5), pady=(10, 5), sticky=E)
    city_v.grid(row=0, column=1, padx=(5, 10), pady=(10, 5), sticky=W)
    country.grid(row=1, padx=(10, 5), pady=(5, 5), sticky=E)
    country_v.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky=W)
    temperature.grid(row=2, padx=(10, 5), pady=(5, 5), sticky=E)
    temperature_v.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky=W)
    pressure.grid(row=3, padx=(10, 5), pady=(5, 5), sticky=E)
    pressure_v.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky=W)
    humidity.grid(row=4, padx=(10, 5), pady=(5, 5), sticky=E)
    humidity_v.grid(row=4, column=1, padx=(5, 10), pady=(5, 5), sticky=W)
    wind_speed.grid(row=5, padx=(10, 5), pady=(5, 5), sticky=E)
    wind_speed_v.grid(row=5, column=1, padx=(5, 10), pady=(5, 5), sticky=W)
    clouds.grid(row=6, padx=(10, 5), pady=(5, 5), sticky=E)
    clouds_v.grid(row=6, column=1, padx=(5, 10), pady=(5, 5), sticky=W)

    return_b.grid(row=9, columnspan=2, padx=(10, 5), pady=(5, 10))


if __name__ == '__main__':
  app = App()
  app.mainloop()