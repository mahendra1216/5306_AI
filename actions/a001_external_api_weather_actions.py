from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

weather_dict = {0: "Unknown",1000: "Clear",
1001: "Cloudy",1100: "Mostly Clear",1101: "Partly Cloudy",1102: "Mostly Cloudy",2000: "Fog",
2100: "Light Fog",3000: "Light Wind",3001: "Wind",3002: "Strong Wind",4000: "Drizzle",4001: "Rain",
4200: "Light Rain",4201: "Heavy Rain",5000: "Snow",5001: "Flurries",5100: "Light Snow",5101: "Heavy Snow",
6000: "Freezing Drizzle",6001: "Freezing Rain",6200: "Light Freezing Rain",6201: "Heavy Freezing Rain",7000: "Ice Pellets",7101: "Heavy Ice Pellets",
7102: "Light Ice Pellets",8000: "Thunderstorm"}
url = "https://api.tomorrow.io/v4/timelines"
querystring = {"location": "32.7301317,-97.1251804","apikey":"bcCv7Ur12oGuRczwrcn92GFin0qcwmNa","fields":"weatherCode,temperature,humidity","timesteps":"1h","units":"metric"}

class ActionAskWeather(Action):
    def name(self) -> Text:
        return "action_ask_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.request("GET", url, params=querystring)
        result = ""

        json_data = response.json()
        json_data = json_data['data']['timelines'][0]['intervals'][0]['values']
        print(json_data)
        print(json_data)
        if(json_data['weatherCode'] in weather_dict):
            result = weather_dict[json_data['weatherCode']] + ' '

        result += 'Average temperature is %s Celsius while the humidity is about %s percentage' % (json_data['temperature'], json_data['humidity'])
        dispatcher.utter_message(text=result)

        return []

