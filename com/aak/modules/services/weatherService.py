import openweathermapy.core as owm
from com.aak.modules.db.personalDA import Personalcurd
import traceback

conditions = {200: 'thunderstorm with light rain',
201: 'thunderstorm with rain',
202: 'thunderstorm with heavy rain',
210: 'light thunderstorm',
211: 'thunderstorm',
212: 'heavy thunderstorm',
221: 'ragged thunderstorm',
230: 'thunderstorm with light drizzle',
231: 'thunderstorm with drizzle',
232: 'thunderstorm with heavy drizzle',
300: 'light intensity drizzle',
301: 'drizzle',
302: 'heavy intensity drizzle',
310: 'light intensity drizzle rain',
311: 'drizzle rain',
312: 'heavy intensity drizzle rain',
313: 'shower rain and drizzle',
314: 'heavy shower rain and drizzle',
321: 'shower drizzle',
500: 'light rain',
501: 'moderate rain',
502: 'heavy intensity rain',
503: 'very heavy rain',
504: 'extreme rain',
511: 'freezing rain',
520: 'light intensity shower rain',
521: 'shower rain',
522: 'heavy intensity shower rain',
531: 'ragged shower rain',
600: 'light snow',
601: 'snow',
602: 'heavy snow',
611: 'sleet',
612: 'shower sleet',
615: 'light rain and snow',
616: 'rain and snow',
620: 'light shower snow',
621: 'shower snow',
622: 'heavy shower snow',
701: 'mist',
804: 'overcast clouds',
901: 'tropical storm',
902: 'hurricane',
906: 'hail',
960: 'storm',
961: 'violent storm',
962: 'hurricane'}

class Weatherservice(object):

    def __init__(self):
          self.getconfig = Personalcurd()
          self.name, self.email, self.zip, self.country, self.owm_appid = self.getconfig.getPersonaldetails()
          self.location = self.zip + "," + str(self.country).lower()
          self.settings = {"units": "imperial", "lang": "US", "APPID": self.owm_appid}


    def getRainStatus(self):
          data = owm.get_current(zip=self.location,**self.settings)
          if not data('weather')[0]['id'] in conditions:
                self.jobstatus="False"
          else:
                print("skipping the job")
                self.jobstatus="True"
          return self.jobstatus


    def weatherDetails(self):
            data = owm.get_current(zip=self.location,**self.settings)
            self.wsdetails ={}
            self.wsdetails = {"Condition":data('weather')[0]['main'],"Description":data('weather')[0]['description'],"temp":data('main.temp'),"temp_min":data('main.temp_min'),"temp_max":data('main.temp_max')}
            return self.wsdetails