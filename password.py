import random
import string

length = 11

str_characters = "!@#$%^&*£?/" + string.ascii_lowercase + string.digits
generated_string = "".join(random.choice(str_characters)
                           for x in range(length))

password = generated_string
print(password)
