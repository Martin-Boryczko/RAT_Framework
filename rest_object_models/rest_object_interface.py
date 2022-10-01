class RestObjectInterface:
    def __init__(self):
        self.USED = True
        self.NOT_USED = False

        # ex. {"item_one": USED, "item_two": USED, "item_three": NOT_USED}
        self.used_required_items = {}
        self.used_optional_items = {}

        # ex. {"key_one": "value_one", "key_two": "value_two"}
        self.fake_items = {}

        self.body_request: str

    ##
    # BUILD REQUEST BODY METHODS
    ##
    def set_request_body_keys_as_used(self, keys):
        raise NotImplementedError("RestObjectInterface set_request_body_keys_as_used - method not implemented.")

    def set_request_body_keys_as_not_used(self, keys):
        raise NotImplementedError("RestObjectInterface set_request_body_keys_as_not_used - method not implemented.")

    def get_request_body(self):
        raise NotImplementedError("RestObjectInterface get_request_body() - method not implemented.")

    def add_fake_node_to_request_body(self, dictionary):
        raise NotImplementedError("RestObjectInterface add_fake_node_to_request_body() - method not implemented.")

    def remove_fake_node_to_request_body(self, dictionary):
        raise NotImplementedError("RestObjectInterface remove_fake_node_to_request_body() - method not implemented.")

    def get_used_items(self):
        required_items = [key for (key, value) in self.used_required_items.items() if value == self.USED]
        optional_items = [key for (key, value) in self.used_required_items.items() if value == self.USED]

        return required_items + optional_items

    ##
    # REST API QUERIES
    ##
    def get(self, get_to_model=True):
        raise NotImplementedError("RestObjectInterface get() - method not implemented.")

    def post(self):
        raise NotImplementedError("RestObjectInterface post() - method not implemented.")

    def put(self):
        raise NotImplementedError("RestObjectInterface put() - method not implemented.")

    def patch(self):
        raise NotImplementedError("RestObjectInterface patch() - method not implemented.")

    def delete(self):
        raise NotImplementedError("RestObjectInterface delete() - method not implemented.")

    def head(self):
        raise NotImplementedError("RestObjectInterface head() - method not implemented.")

    def options(self):
        raise NotImplementedError("RestObjectInterface options() - method not implemented.")

    def trace(self):
        raise NotImplementedError("RestObjectInterface trace() - method not implemented.")

    def connect(self):
        raise NotImplementedError("RestObjectInterface connect() - method not implemented.")
