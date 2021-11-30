import json
from pathlib import Path
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class ActionCheckExistence(Action):
    knowledge = Path("C:/Users/GangineniMahendraBab/Desktop/newProject/data/course_name.txt").read_text().split("\n")
    print(knowledge)
    def name(self) -> Text:
        return "action_check_existence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for blob in tracker.latest_message['entities']:
            print(blob)
            print(tracker.latest_message['text'])
            if blob['entity'] == 'course_name':
                name = blob['value']
                if name in self.knowledge:
                    dispatcher.utter_message(text=f"Yes, {name} is offered by UTA")
                else:
                    dispatcher.utter_message(
                        text=f"I do not recognize {name}, are you sure it is correctly spelled?")
        return []
