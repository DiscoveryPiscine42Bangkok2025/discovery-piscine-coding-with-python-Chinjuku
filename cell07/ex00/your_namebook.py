#!/usr/bin/python3

def array_of_names(persons):
    firstnames = list(persons.keys())
    lastnames = list(persons.values())
    arrays = []
    for i in range(len(list(persons))):
        arrays.append(f"{firstnames[i].capitalize()} {lastnames[i].capitalize()}")

    return arrays

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))