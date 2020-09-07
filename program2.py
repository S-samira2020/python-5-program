# slicing a list
actors = ['shilpa', 'ranvir', 'shahir', 'karan', 'adha', 'santosh']
print(actors[0:3])
print()
print(actors[1:4])
print()
print(actors[:4])
print()
print(actors[2:])
print()
print(actors[-3:])
print()
for actor in actors[:3]:
    print(actor)
print()
for actor in actors[-3:]:
    print(actor)
print()

#copying a list
my_food = ['rice', 'chicken', 'vegetable']
my_ffood = my_food[0:]
print('My favourite food is here: ')
print(my_food)
print()
print('my friend favourite food: ')
print(my_ffood)
print()
my_food.append('drink')
my_ffood.append('ice cream')
print('my favorite food is: ')
print(my_food)
print()
print('my friends favourite food is: ')
print(my_ffood)
print()
