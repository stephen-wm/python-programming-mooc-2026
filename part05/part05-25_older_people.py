def older_people(people: list, year: int) -> list:
    oldest = []

    for person in people:
        if person[1] < year:
            oldest.append(person[0])

    return oldest
