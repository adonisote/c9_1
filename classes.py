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

class User:
    def __init__(self, first_name, last_name, age = None, alias =None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.alias = alias
    def describe_user(self):
        print(f'\nUser information. \nFirst Name: {self.first_name.title()}'
            f'\nLast Name: {self.last_name.title()}'
            f'\nAge: {self.age}'
            f'\nAlias: {self.alias}')
    def greet_user(self):
        print(f'Hello, {self.first_name.title()}!')



user0 = User('Pili', 'Maus')
user1 = User('Jack', 'Johnson', 39, 'Jacky')
user2 = User('Adonis', 'Almagro', 28, 'adonisote')

users = [user0, user1, user2]

for x in users:
    x.describe_user()
    x.greet_user()