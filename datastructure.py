import random
from flask import jsonify

class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return random.randint(0, 99999999)

    def add_member(self, member):
        for memb in self._members:
            if member["id"] == memb["id"]:
                return {"data": None, "status": 400}  
        member["id"] == self._generateId
        self._members.append(member)
        return {"data": None, "status": 200}

    def delete_member(self, id):
        for member in self._members:
                if member["id"] == id:
                    self._members.remove(member)
                    return {"data": None, "status": 200}
        return {"data": None, "status": 404}
        
            

    def update_member(self, id, member):
        member.update({"id": id})
        for memb in self._members:
            if memb["id"] == id:
                memb = member
                return {"data": None, "status": 200}
        return {"data": None, "status": 404}
      

    def get_member(self, id):
        print("hello member")
        for memb in self._members:
            if memb["id"] == id:
                return {"data": memb, "status": 200}
        return {"data": None, "status": 400}
        

    def get_all_members(self):
        print('hello get all')
        if len(self._members) > 0:
            return {"data": self._members, "status": 200}
        else:
            return {"data": None, "status": 404}
        