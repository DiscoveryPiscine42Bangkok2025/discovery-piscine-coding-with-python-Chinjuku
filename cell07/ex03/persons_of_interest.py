#!/usr/bin/python3

def famous_births(persons):
    return [print(f"{value['name']} is a great scientist born in {value['date_of_birth']}.") for key, value in persons.items()]

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)