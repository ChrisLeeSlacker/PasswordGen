import string
import random

pw_file = 'pw_gen.txt'


def pw_gen(size, chars=string.punctuation + string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))


x = pw_gen(int(input('How many characters do you want in your password?\n')))

with open(pw_file, 'w') as f:
    f.write(x)

password_gen = 'In the file {}\nYour password is: {}'.format(pw_file, x)
print(password_gen)
