#Weather skill for AI
#Author: Vhuhwavho Mokoma

from pyowm import OWM
from pyowm.utils import timestamps
from geopy import Nominatim 
from datetime import datetime

class Weather():

    __location = "Soweto, ZA"

    api_key = "90be93527babd2a823f16c364325e6d1"
    def __init__(self):
        self.ow = OWM(self.api_key)
        self.mgr = self.ow.weather_manager()
        locator = Nominatim(user_agent="myGeocoder")
        city = "Soweto"
        country = "ZA"
        self.__location = city + ", " + country
        loc = locator.geocode(self.__location)
        self.lat = loc.latitude
        self.long = loc.longitude
   
    def forecast(self):
        """unpacks the weather object"""
        forecast = self.mgr.one_call(lat=self.lat, lon=self.long)
        #three_h_forecaster = self.mgr.forecast_at_place(self.__location, '3h')
        detail = forecast.forecast_daily[0].detailed_status
        sunrise = datetime.utcfromtimestamp(forecast.forecast_daily[0].sunrise_time()).strftime("%I:%M %p")
        sunset = datetime.utcfromtimestamp(forecast.forecast_daily[0].sunset_time()).strftime("%I:%M %p")
        #period = timestamps.next_hour() # datetime object for next hour
        #response = three_h_forecaster.will_be_rainy_at(period) 
        #rain = "There will be no rain in the next hour."
        #if(response):
           #rain = "There will be rain in the next hour."
        temp = str(forecast.forecast_daily[0].temperature('celsius').get('day'))
        message = "Here is the weather forecast: Today will be " + detail + ". Sunrise was at " + sunrise + " Sunset is at " + sunset + ". The temperature is " + temp + ". "
        return message

