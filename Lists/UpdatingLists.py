castOfOceans = ['Brad', 'George', 'Casey', 'Matt', 'Julia', 'Samantha']
print(castOfOceans)
#Oops! There is no one named Samantha in the Oceans trilogy. Let's change her name to the correct female 2nd lead.
castOfOceans[5] = 'Catherine' 
print(castOfOceans[-1])
print(castOfOceans)

#Oops! I forgot a cast member. Let's add him to the end of the list.
castOfOceans.append('Don')
print(castOfOceans[-1])
print(castOfOceans)

#Now, I want to remove the female leads from the list. I can use the del statement to remove an item at a specific index.
del castOfOceans[4]
#Or I could use the remove() method to remove an item by value.
castOfOceans.remove('Catherine')
print(castOfOceans)

#What if there are two cast members with the same name? Let's add another Brad to the list and then remove him.
castOfOceans.append('Brad')
print(castOfOceans)
#Now, let's remove the first Brad from the list.
castOfOceans.remove('Brad')
print(castOfOceans)
#When you have two values with the same name, the remove() method will only remove the first instance of that value. 
#If you want to remove a specific instance of a value, you can always use the del statement.

#If you want to remove all instances of a value, you can use a while loop.
#Let's add two Alan to the list and then remove both of them.
castOfOceans.append('Alan')
castOfOceans.append('Alan')
print(castOfOceans)

while 'Alan' in castOfOceans:
    castOfOceans.remove('Alan')
print(castOfOceans)

#Let's add three Al Pacino to the list and then remove only two of them.
castOfOceans.append('Al Pacino')
castOfOceans.append('Al Pacino')
castOfOceans.append('Al Pacino')
print(castOfOceans)

count = 0
for actor in castOfOceans:
    if actor == 'Al Pacino':
        count += 1

# Remove only two instances of 'Al Pacino'
for x in range(min(2, count)): #min() is used to ensure we don't try to remove more instances than exist in the list.
    castOfOceans.remove('Al Pacino')
print(castOfOceans)