def oldest_person(people: list) -> str: 
    oldest = people[0][1]
    name = people[0][0]
    
    for person in people: 
        age = person[1] 
        if age < oldest:
            oldest = age
            name = person[0] 
            
    return name 
