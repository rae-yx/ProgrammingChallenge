def find_type(value):
    if value.isdigit():
        return "Integer"
    
    try:
        float_value = float(value)
        if '.' in value:
            return "Real Number"
        
    except ValueError:
        pass

    if any(char.isdigit() for char in value) and any(char.isdigit() for char in value):
        return "Alphanumeric"
    
    return "Alphabetical String"

with open("programming_challenge.txt", "r") as file:
    for line in file:
        objects = line.split(',')

        if len(objects) == 4:
            alphabetical = objects[0]
            real_number = objects[1]
            integer = objects[2]
            alphanumeric = objects[3].strip()

            print(f"Object: {alphabetical} Type: {find_type(alphabetical)}")
            print(f"Object: {real_number} Type: {find_type(real_number)}")
            print(f"Object: {integer} Type: {find_type(integer)}")
            print(f"Object: {alphanumeric} Type: {find_type(alphanumeric)}\n")