# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import gc
from xml.etree.ElementInclude import include
import csv
import urllib.request
import ssl
import json
import os
import html
import random
import pathlib
from typing import Any, Text, Dict, List, overload
from rasa_sdk.events import FollowupAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import random

DATABASE = ["bún đậu mắm tôm",
            "bún đậu nước mắm",
            "bún cá",
            "bún hải sản",
            "cơm văn phòng",
            "cơm sườn",
            "xôi",
            "bún ốc",
            "mì vằn thắn",
            "hủ tiếu",
            "bún chả",
            "bún ngan",
            "ngan xào tỏi",
            "bún bò huế",
            "mì tôm hải sản",
            "bánh mì trứng xúc xích rắc thêm ít ngải cứu",
            "bánh mì trứng",
            "bánh mì xúc xích",
            "bánh mì pate"]


class act_food(Action):

    def name(self) -> Text:
        return "act_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food = []
        for i in range(2):
            food_number = random.randrange(len(DATABASE))
            food.append(DATABASE[food_number])

        dispatcher.utter_message(
            text="Em nghĩ hôm nay anh chị có thể thử món '{}' hoặc bên cạnh đó cũng có thể là món '{}' ạ".format(food[0], food[1]))

        return []
#---------------------------------------- actions Gia Lai Travel------------------------

class Act_hotline(Action):

    def name(self) -> Text:
        return "act_hotline"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file

        dispatcher.utter_message(
            text="Hotline : 19009999, 02691022")
        return []

class Act_cost_food(Action):

    def name(self) -> Text:
        return "act_cost_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Đây là Act_cost_food ạ")

        return []

class Act_hotel(Action):
    def name(self) -> Text:
        return "act_hotel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="đây là act_hotel ạ")

        return []

class Act_cost_hotel(Action):

    def name(self) -> Text:
        return "act_cost_hotel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="đây là act_cost_hotel ạ")

        return []

class Act_coffee(Action):

    def name(self) -> Text:
        return "act_coffee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="đây là act_coffee ạ")

        return []

class Act_hotline(Action):

    def name(self) -> Text:
        return "act_hotline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="đây là act_hotline ạ")

        return []

class Act_festival(Action):

    def name(self) -> Text:
        return "act_festival"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="đây là act_festival ạ")

        return []

class Act_congchieng(Action):

    def name(self) -> Text:
        return "act_congchieng"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="đây là act_congchieng ạ")

        return []

class Act_daquy(Action):

    def name(self) -> Text:
        return "act_daquy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="đây là act_daquy ạ")

        return []

class Act_trips(Action):

    def name(self) -> Text:
        return "act_trips"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="đây là act_trips ạ")

        return []