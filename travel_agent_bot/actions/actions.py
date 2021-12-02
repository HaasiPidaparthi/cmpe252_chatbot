from typing import Text, List, Any, Dict
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet, EventType

class ValidateTripForm(FormValidationAction):
    validation_events = []
    def name(self) -> Text:
        return "validate_trip_form"

    def invalid_item(self,slot_name: Any,slot_value: Any,dispatcher: CollectingDispatcher):
    	print('we dont have')
    	dispatcher.utter_message(template="utter_not_available", not_available_option=slot_value)
    	self.validation_events.append(SlotSet(slot_name, None))

    @staticmethod
    def package_db() -> List[Text]:
        return [
            "special", 
            "vacation", 
            "honeymoon", 
            "family",
            "cruise",
            "adventure",
            "festivals and events",
            "wedding",
            "luxury",
        ]

    def validate_a_package(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict,) -> Dict[Text, Any]:
        print("Running is valid: package")
        if not isinstance(slot_value, str):
            seperator = " "
            slot_value = seperator.join(slot_value)
        print(slot_value)

        if slot_value.lower() in self.package_db():
            # validation succeeded, set the value of the "package" slot to value
             self.validation_events.append(SlotSet("a_package", slot_value))
             return {"a_package": slot_value}
        else:
            # validation failed, set this slot to None so that the user will be asked for the slot again
            self.invalid_item("a_package", slot_value, dispatcher)
            return {"a_package": None}

    @staticmethod
    def island_db() -> List[Text]:
        return [
            "bora bora",
            "tahiti",
            "moorea",
            "huahine",
            "raiatea",
        ]

    def validate_b_island(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print("Running is valid: island")
        if not isinstance(slot_value, str):
            seperator = " "
            slot_value = seperator.join(slot_value)
        print(slot_value)

        if slot_value.lower() in self.island_db():
            self.validation_events.append(SlotSet("b_island", slot_value))
            return {"b_island": slot_value}
        else:
            self.invalid_item("b_island", slot_value, dispatcher)
            return {"b_island": None}

    @staticmethod
    def count_db() -> List[Text]:
        return [
            "1",
            "2",
            "3",
            "4",
            "5+",
        ]

    def validate_count(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print("Running is valid: people count")
        if not isinstance(slot_value, str):
            seperator = " "
            slot_value = seperator.join(slot_value)
        print(slot_value)

        if slot_value.lower() in self.count_db():
            self.validation_events.append(SlotSet("c_count", slot_value))
            return {"c_count": slot_value}
        else:
            self.invalid_item("c_count", slot_value, dispatcher)
            return {"c_count": None}

    @staticmethod
    def nights_db() -> List[Text]:
        return [
        "no limit",
        "two days",
        "five days",
        "one week",
        "two weeks",
        ]

    def validate_d_nights(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print("Running is valid: total nights")
        if not isinstance(slot_value, str):
            seperator = " "
            slot_value = seperator.join(slot_value)
        print(slot_value)

        if slot_value.lower() in self.nights_db():
            self.validation_events.append(SlotSet("d_nights", slot_value))
            return {"d_nights": slot_value}
        else:
            self.invalid_item("d_nights", slot_value, dispatcher)
            return {"d_nights": None}    

    @staticmethod
    def budget_db() -> List[Text]:
        return [
        "any",
        "under $3000",
        "$3000 - $5000",
        "over $5000",
        ]
    
    def validate_e_budget(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print("Running is valid: Budget per Person")
        if not isinstance(slot_value, str):
            seperator = " "
            slot_value = seperator.join(slot_value)
        print(slot_value)

        if slot_value.lower() in self.budget_db():
            self.validation_events.append(SlotSet("e_budget", slot_value))
            return {"e_budget": slot_value}
        else:
            self.invalid_item("e_budget", slot_value, dispatcher)
            return {"e_budget": None}   

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        dispatcher.utter_message("Thank you so much for showing your interest in traveling with us!")    
        return []    


# class AboutBoraBora(Action):
#     def name(self):
#          return "action_about_bora_bora"  

#     def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         gt = {
#         	"attachment": {
#         		"type": "template",
#         		"payload": {
#         			"template_type": "generic",
#         			"elements": [
#         				{
#         					"title": "Bora Bora is a small South Pacific island northwest of Tahiti in Polynesia.",
#         					"image_url":"https://www.mole.my/wp-content/uploads/2015/03/pacificmap.gif"
#         				},
#         				{
#         					"title": "Surrounded by sand-fringed motus (islets) and a turquoise lagoon protected by a coral reef, it’s known for its scuba diving.",
#         					"image_url":"https://topdive.com/wp-content/uploads/2017/11/borabora07.jpg"
#         				},
#         				{
#         					"title": "It's also a popular luxury resort destination where some guest bungalows are perched over the water on stilts.",
#         					"image_url":"https://www.conradboraboranuiresort.com/wp-content/uploads/2019/04/resort-exterior-1920x1200-1-1024x640.jpg"
#         				},
#         			]
#         		}
#         	}
#         }
#         dispatcher.utter_custom_json(gt)
#         return []
