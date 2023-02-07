import json
from abc import ABC

import requests

from rest_object_models.rest_object_interface import RestObjectInterface


class SampleModel(RestObjectInterface, ABC):

    def __init__(self, first_name=None, last_name=None, age=None):
        RestObjectInterface.__init__(self)
        self.URL = ""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        self.used_required_items = {"first_name": self.USED, "last_name": self.USED}
        self.used_optional_items = {"age": self.USED}

    ##
    # BUILD REQUEST BODY METHODS
    ##

    def get_request_body(self):
        used_items = self.get_used_items()
        request_body_dict = {}.update(self.fake_items)

        if "first_name" in used_items:
            request_body_dict["first_name"] = self.first_name

        if "last_name" in used_items:
            request_body_dict["last_name"] = self.last_name

        if "age" in used_items:
            request_body_dict["age"] = self.age

        return json.dumps(request_body_dict)

    ##
    # USED REST API QUERIES
    ##
    def get(self, get_to_model=False):
        response = requests.get(self.URL)
        # get to SampleModel object
        if get_to_model:
            # TODO: set SampleModel object data from json response
            pass
        return response

    def post(self):
        return requests.post(self.URL, json=self.get_request_body)

    def put(self):
        return requests.put(self.URL, json=self.get_request_body)

    def patch(self):
        return requests.patch(self.URL, json=self.get_request_body)

    def delete(self):
        return requests.delete(self.URL, json=self.get_request_body)

    ##
    # Eq operator overloading for objects assertion
    ##
    def __eq__(self, other):
        if not isinstance(other, SampleModel):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.first_name == other.first_name and \
               self.last_name == other.last_name and \
               self.age == other.age
