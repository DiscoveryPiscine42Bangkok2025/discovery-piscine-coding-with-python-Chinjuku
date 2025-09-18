#!/usr/bin/python3

def find_the_redheads(family):
    arrays = []
    for i in range(len(list(family))):
        if list(family.values())[i] == "red":
            arrays.append(list(family.keys())[i])
            
    return arrays

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))