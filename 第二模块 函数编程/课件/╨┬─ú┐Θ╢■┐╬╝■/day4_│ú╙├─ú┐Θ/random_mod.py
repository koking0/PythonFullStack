
import random

import string

print(random.randint(10,100))
print(random.randrange(1,10,2))
print(random.random())
print(random.choice('abcsdfsfsfsde3#$@1'))
print(random.sample('abcdefghij',3)  )

print("".join(random.sample(string.digits+string.ascii_lowercase,5)))

s = string.digits+string.ascii_lowercase
print(s)

a = list(range(100))
random.shuffle(a)

print(a)