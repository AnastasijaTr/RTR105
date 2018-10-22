'''
n = 5
while n > 0:
    print(n)
    n = n - 1
print('blastoff')
print(n)
'''
'''
while True:
    line = raw_input('> ')
    if line == 'done':
        break
    print(line)
print('Done')
'''

'''
while True:
    line = raw_input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done')
'''

'''
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')
'''


'''
friends = ['Joseph','Gleen', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
'''

'''
print('before')
for thing in [9, 41, 12, 3, 74, 14]:
    print(thing)
print('afther')
'''



'''
largest_so_far = -1
print('before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('after', largest_so_far)
'''



'''
zork = 0
print('before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('after', zork)
'''


count = 0
sum = 0
print('before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('after', count, sum, sum / count)


      
      
























