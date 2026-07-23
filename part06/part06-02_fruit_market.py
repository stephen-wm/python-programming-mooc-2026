def read_fruits() -> dict:
    fruits = {}

    with open("./fruits.csv") as file:
        for line in file:
            parts = line.split(';')
            name = parts[0]
            price = float(parts[1])
            
            fruits[name] = price
            
    return fruits