import random
import string

def generate_string():
    length = random.randint(5,20)
    return ''.join(random.choices(string.ascii_letters,k=length))

def generate_real_number():
    return f"{random.uniform(1,100):.2f}"

def generate_integer():
    return str(random.randint(1,1000))

def generate_alphanumeric():
    length = random.randint(5,20)
    alphanumeric = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    spaces_before = ' ' * random.randint(0,10)
    spaces_after = ' ' * random.randint(0,10)

    return f"{spaces_before}{alphanumeric}{spaces_after}"

target_file_size = 10 * 1024 * 1024

with open("programming_challenge.txt", "w") as file:
    file_size = 0

    while file_size < target_file_size:
        alphabetical = generate_string()
        real_number = generate_real_number()
        integer = generate_integer()
        alphanumeric = generate_alphanumeric()

        data = f"{alphabetical},{real_number},{integer},{alphanumeric}\n"

        file.write(data)

        file_size += len(data)

print("File created successfully.")        