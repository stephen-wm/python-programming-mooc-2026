def invert(dictionary: dict):
    inverted = {}

    for key in dictionary:
        inverted[dictionary[key]] = key
    
    dictionary.clear()

    for key in inverted:
        dictionary[key] = inverted[key]
