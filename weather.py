#import necessary python module requests
from requests import get

#set up the API url using my unique key and the city I want weather for
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "London"
API_KEY = "788256d53bfc0ad38ad27910fff619c7"

URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

#get weather report json, convert to readable dictionary format and extract the temperature value
def get_weather():
    data = get(URL).json()
    main = data['main']
    kelvin = main['temp']

    #temperature must be converted from kelvin to celsius
    temp = kelvin - 273.15

    return(temp)