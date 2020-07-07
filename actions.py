# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json
from database import DataUpdate
    
    

class ActionHr(Action):
	def name(self):
		print('in self method')
		return 'action_leave'

	def run (self, dispatcher, tracker, domain):
		print('in run method')
		i = tracker.get_slot('name')
		print(i)
		with open('data1.txt') as json_file:
			data = json.loads(json_file.read())
			
			for result in data['current']:
				print('name'+ result['name'])
				if result['name'].lower() == i.lower():
					print('Name Found')
					name = result['name']
					ID = result['ID']
					SickLeave = result['Sick Leaves']
					CasualLeave = result['Casual Leaves']
					TotalLeave = result['Total Leaves']
					LeavesLeft = result['Leaves Left']
		response ="""The Leaves left for ID {} is {} . You took {} casual leaves and {} sick leaves.""".format(ID,LeavesLeft,SickLeave,CasualLeave)
		print(response)
						
		dispatcher.utter_message(response)
		return [SlotSet('name',i)]
    
    
    
class ActionId(Action):

     def name(self) -> Text:
        return "action_days"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_days")
        return [SlotSet('ids',tracker.latest_message['text'])]

        return []

    
    
class ActionDays(Action):

     def name(self) -> Text:
        return "action_leaves_submit"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_submit")
        
        return [SlotSet('days',tracker.latest_message['text'])]

        return []
    
class ActionSub(Action):

     def name(self) -> Text:
        return "action_submit"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            
        DataUpdate(tracker.get_slot("ids"),tracker.get_slot("days"))
        dispatcher.utter_message("Your leave application has been submitted successfully.")

        

        return []
    
