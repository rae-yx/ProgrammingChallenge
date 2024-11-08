import random
import string

#Generate random alphabetical string
def generate_string():
    length = random.randint(5,20)
    return ''.join(random.choices(string.ascii_letters,k=length))

#Generate random real number
def generate_real_number():
    return f"{random.uniform(1,100):.2f}"

#Generate random integer
def generate_integer():
    return str(random.randint(1,1000))

#Generate random alphanumeric string
def generate_alphanumeric():
    length = random.randint(5,20)

    #Make sure there is at least a letter and a number
    letter = random.choice(string.ascii_letters)
    digit = random.choice(string.digits)

    #Generate the remaining characters
    remaining_length = length - 2
    remaining_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=remaining_length))
    alphanumeric = letter + digit + remaining_chars
    #Shuffle the letter and digit
    alphanumeric = ''.join(random.sample(alphanumeric, len(alphanumeric)))
    #Add spaces
    spaces_before = ' ' * random.randint(0,10)
    spaces_after = ' ' * random.randint(0,10)

    return f"{spaces_before}{alphanumeric}{spaces_after}"

#File size is 10MB and convert to bytes
target_file_size = 10 * 1024 * 1024

#Create and write data to file
with open("programming_challenge.txt", "w") as file:
    file_size = 0

    while file_size < target_file_size:
        alphabetical = generate_string()
        real_number = generate_real_number()
        integer = generate_integer()
        alphanumeric = generate_alphanumeric()

        #Separate data with commas and add newline character
        data = f"{alphabetical},{real_number},{integer},{alphanumeric}\n"

        file.write(data)

        #Update file size
        file_size += len(data)

print("File created successfully.")        