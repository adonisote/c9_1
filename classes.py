# class Dog():
#     def __init__(self, name, age):
#         self.random1 = name
#         self.random2 = age
#     def sit(self):
#         print(self.random1.title() + "is sitting now!")

# my_dog = Dog("pilatus", 3)
# my_dog.sit()

# x= 5
# if not x <= 4 or x > :
#    raise AssertionError('Oh no')

class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def describe_restaurant(self):
        print(f'{self.name.title()}, {self.type()}')
    def describe_restaurant(self):
        print(f'{self.name.title()} is open now!')


restaurant0 = Restaurant('felis\'', 'vegan specialities') 
restaurant1 = Restaurant('pilatus\'', 'rabbit specialities')
restaurant2 = Restaurant('adonis\'', 'all you can eat')


restaurants = [restaurant0, restaurant1, restaurant2]

for x in restaurants:
    x.describe_restaurant()

print(restaurants)