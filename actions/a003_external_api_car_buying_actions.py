from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
url = "https://serpapi.com/search.json?"
querystring = {"num":"5","engine":"google","q":"some_text","api_key":"0091bd950efa58d8d706dae654dfd1ceb63972a5d3ed376d654d72389519b336",
"location":"Arlington, Texas, United States"}

class ActionAskGoogleCars(Action):
    def name(self) -> Text:
        return "action_ask_car_dealers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        querystring['q'] = "i want to buy a car, show me the nearest car dealership, please"
        response = requests.request("GET", url, params=querystring)
        result = " Here are few options you might want to explore      "

        json_data = response.json()
        print(json_data)
        json_data = json_data['local_results']['places']
        for values in json_data:
            result = result  + values['title'] + ' with user rating of ' + str(values['rating']) + ' Address: '+values['address'] + '   '
        print(json_data)
        dispatcher.utter_message(text=result)

        return []

