#Main function to find the type of object
def find_type(value):
    #Check for integer
    if value.isdigit():
        return "Integer"
    #Check for real number (float)
    #Try-except is used because float() will raise a ValueError if the value is not a number
    try:
        float_value = float(value)
        if '.' in value:
            return "Real Number"
        
    except ValueError:
        pass

    #Check for alphanumeric
    if any(char.isdigit() for char in value) and any(char.isdigit() for char in value):
        return "Alphanumeric"
    #If not any of the above, it is an alphabetical string
    return "Alphabetical String"

#Open file and read line by line
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