from collections import UserList
from random import choice, randint


class Products(UserList):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    data = []
    for i in range(10):
        word = []
        for j in range(randint(4, 6)):
            word.append(choice(consonants))
            word.append(choice(vowels))
        data.append(''.join(word))

    def __init__(self):
        self.data = Products.data
