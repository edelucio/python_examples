import random
import string

letters = string.ascii_lowercase

vowels = 'aeiouy'

consonants = 'bcdfghjklmnpqrstvwxz'


def generator():

    letter_1 = random.choice(vowels)

    letter_2 = random.choice(consonants)

    letter_3 = random.choice(vowels)

    letter_4 = random.choice(consonants)

    letter_5 = random.choice(vowels)

    letter_6 = random.choice(consonants)

    letter_7 = random.choice(vowels)

    letter_8 = random.choice(consonants)

    letter_9 = random.choice(vowels)

    letter_10 = random.choice(consonants)

    letter_11 = random.choice(vowels)

    letter_12 = random.choice(consonants)

    letter_13 = random.choice(vowels)

    letter_14 = random.choice(consonants)

    letter_15 = random.choice(vowels)

    letter_16 = random.choice(consonants)

    letter_17 = random.choice(vowels)

    letter_18 = random.choice(consonants)

    name = letter_1 + letter_2 + letter_3 + letter_4 + letter_5 + letter_6 + letter_7 + letter_8 + letter_9 + \
        letter_10 + letter_11 + letter_12 + letter_13 + \
        letter_14 + letter_15 + letter_16 + letter_17 + letter_18

    return name


for i in range(15):

    print(generator())
