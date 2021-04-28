class Parrot:
    # class attribute
    species = 'Bird'

    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#instantiating the Parrot class
blu = Parrot('blu', 10)
woo = Parrot('Woo', 15)

#Accessing instance and class attributes
print('{} is a {}'.format(blu.name, blu.__class__.species))
print('{} is a {}'.format( woo.name, woo.__class__.species))