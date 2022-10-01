import json
from abc import ABC  ### is this needed ?

import requests

from rest_object_models.rest_object_interface import RestObjectInterface


class SampleModel(RestObjectInterface, ABC):

    def __init__(self):
        RestObjectInterface.__init__(self)
        self.URL = ""

        self.age = None
        self.last_name = None
        self.first_name = None

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
    def get(self, get_to_model=True):
        response = requests.get(self.URL, auth=('user', 'pass'))
        # get to SampleModel object
        if get_to_model:
            pass #dodać jsona i rozbić

        return response

    def post(self):
        return requests.post(self.URL, json=self.get_request_body, auth=('user', 'pass'))

    def put(self):
        return requests.put(self.URL, json=self.get_request_body, auth=('user', 'pass'))

    def patch(self):
        return requests.patch(self.URL, json=self.get_request_body, auth=('user', 'pass'))

    def delete(self):
        return requests.patch(self.URL, json=self.get_request_body, auth=('user', 'pass'))
