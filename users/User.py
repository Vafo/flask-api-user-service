

class User:

    def __init__(self):
        self.id = -1
        self.name = ""
        self.email = ""
        self.password = ""

    def from_dict(self, dict):
        if "id" in dict:
            self.id = dict["id"]
        self.name = dict["name"]
        self.email = dict["email"]
        self.password = dict["password"]

        return self

    def to_dict(self):
        res = {}
        res["id"] = self.id
        res["name"] = self.name
        res["email"] = self.email
        res["password"] = self.password

        return res

