import os

#Paths inside the container
input_file_path = '/app/programming_challenge.txt'
output_file_path = '/app/challenge_b_output/processed_output.txt'

#Make sure the output directory exists in the container
os.makedirs('/app/challenge_b_output', exist_ok=True)

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
    if any(char.isalpha() for char in value) and any(char.isdigit() for char in value):
        return "Alphanumeric"
    
    #If not any of the above, it is an alphabetical string
    return "Alphabetical String"

#Open the input file from container
with open(input_file_path, 'r') as file:
    lines = file.readlines()

#Open and write the output file
with open(output_file_path, "w") as output_file:
    for line in lines:
        objects = line.strip().split(',')

        if len(objects) == 4:
            alphabetical = objects[0]
            real_number = objects[1]
            integer = objects[2]
            alphanumeric = objects[3].strip()

            #Print to console in the container
            print(f"Object: {alphabetical} Type: {find_type(alphabetical)}")
            print(f"Object: {real_number} Type: {find_type(real_number)}")
            print(f"Object: {integer} Type: {find_type(integer)}")
            print(f"Object: {alphanumeric} Type: {find_type(alphanumeric)}\n")

            #Write to output file
            output_file.write(f"Object: {alphabetical} Type: {find_type(alphabetical)}\n")
            output_file.write(f"Object: {real_number} Type: {find_type(real_number)}\n")
            output_file.write(f"Object: {integer} Type: {find_type(integer)}\n")
            output_file.write(f"Object: {alphanumeric} Type: {find_type(alphanumeric)}\n\n")

print("Output file created successfully.")