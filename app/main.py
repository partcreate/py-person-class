from __future__ import annotations
from typing import Union, TypedDict, List
from typing import Optional


class Person:

    people: dict[str, Person] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def set_wife(self, wife_instance: Person) -> None:
        self.wife: Person = wife_instance

    def set_husband(self, husband_instance: Person) -> None:
        self.husband: Person = husband_instance


class BasePersonData(TypedDict):
    name: str
    age: int


class PersonDataWithWife(BasePersonData):

    wife: Optional[str]


class PersonDataWithHusband(BasePersonData):

    husband: Optional[str]


PersonData = Union[
    PersonDataWithWife,
    PersonDataWithHusband
]


def create_person_list(people: List[PersonData]) -> List[Person]:

    res_list: list["Person"] = []

    for person_obj in people:
        people_instance = Person(
            name=person_obj["name"],
            age=person_obj["age"])

        Person.people[person_obj["name"]] = people_instance

        res_list.append(people_instance)

    for i, value in enumerate(res_list):

        has_wife_key = "wife" in people[i]

        has_husband_key = "husband" in people[i]

        if has_wife_key and people[i]["wife"] is not None:
            Person.people[people[i]["wife"]].set_husband(value)

        if has_husband_key and people[i]["husband"] is not None:
            Person.people[people[i]["husband"]].set_wife(value)

    return res_list
