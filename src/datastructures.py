
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name


        # example list of members
        self._members = [{"id": self._generateId(),
                          "first_name": "Mariona",
                          "last_name": last_name,
                          "age": 23,
                          "lucky_numbers": [7, 11, 3]},
                         {"id": self._generateId(),
                          "first_name": "Pol",
                          "last_name": last_name,
                          "age": 26,
                          "lucky_numbers": [4, 5, 12]},
                         {"id": self._generateId(),
                          "first_name": "Maria",
                          "last_name": last_name,
                          "age": 59,
                          "lucky_numbers": [18, 3, 9]}]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["last_name"] = self.last_name
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        members = []
        for member in self._members:
            if member["id"] != id:
                members.append(member)
        self._members = members
        return self._members

    def get_member(self, id):
        members = []
        for member in self._members:
            if member["id"] == id:
                members.append(member)
        return members

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
