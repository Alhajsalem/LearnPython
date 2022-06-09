# string concatenation
# demonstration on the example of Mad Libs

from random import randbytes

# some random string generator


def random_string_gen(m):
    random_string = ""
    for n in range(m):
        random_string += str(randbytes(10))[-2:-1]
#    print("This is a randomly composed string of length " +
#          str(m) + ": '" + random_string + "'")
#    print("This is a randomly composed string of length '{}': '{}'".format(
#        m, random_string))
    print(f"This is a randomly composed string of length {m}: {random_string}")

    return random_string


#rand_string = random_string_gen(5)
#rand_string_length = len(rand_string)
# print(
#    f"The length of the randomly composed string is equal to {rand_string_length}")
