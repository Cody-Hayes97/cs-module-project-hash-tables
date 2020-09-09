# write a function that will take a string and return a number

# use encode to store code of string
def UTF8_hash(str):
    total = 0
    str_bytes = str.encode()
    for byte in str_bytes:
        total += byte
    return total


print(UTF8_hash('hello'))
print(UTF8_hash('bello'))
# but this way, we will still have collisions

#  a hash function is any function that takes a string, and gives back a number
# operate on the bytes that make up the string usually
# fast
# deterministic: always give back the same thing we put in


# Hash function + array!
# how to map the output of our hash function to an index of an array?
# modulo the hash with len(array)

# modulo return from 0 to len(list) - 1
# 1 % 20 -> 1
# 15 % 20 -> 15
# 20 % 20 -> 0
# 39 % 20 -> 19
# 40 % 20 -> 0

# never higher than 19 above


# use modulo with hash (output of hashing funct.) to get usable idx

# we can now combine our hash function and array

# 'put' into our array
my_arr2 = [None] * 20

our_hash = UTF8_hash('supercalifragilisticexpialidocious')  # 3643
idx = our_hash % len(my_arr2)

my_arr2[idx] = 'Mary Poppins'

print(my_arr2)

# 'get' into our array
our_hash = UTF8_hash('supercalifragilisticexpialidocious')
idx = our_hash % len(my_arr2)

val = my_arr2[idx]
print(val)

# key value pair
# 'supercalifragilisticexpialidocious' is the key
# 'Mary Poppins' is the value

# hash table examples in programming languages?
# Python : dictionaries
# JS: objects
# Hash maps


# psuedocode for put
# 1. Hash the key
# 2. Take the hash and mod it with len of array
# 3. Go to index and put in value

# psuedocode for get
# 1. Hash the key
# 2. Take the hash and mod it with len again
# 3. Go to that idx and get out the value

# Time Complexity
# Same for get and put
# Linear in length of string/key
# Constant time in length of array <------- This is what we pay attention to
# 0(1)

# Collision
key1 = 'dad'
key2 = 'add'

# put 1
hash1 = UTF8_hash(key1)
idx1 = hash1 % len(my_arr2)
my_arr2[idx1] = 'howdy'

# put 2
hash2 = UTF8_hash(key2)
idx2 = hash2 % len(my_arr2)
my_arr2[idx2] = 'Wassup'

# Get
get_hash = UTF8_hash(key1)
idx3 = get_hash % len(my_arr2)
print(my_arr2[idx3])


# even when we use our hash funtionc with mod, we get collisions
# to be solved later


# we wrote our own hash function, what about Pythons hash()?
# Many different hash functions! Can also hash()
