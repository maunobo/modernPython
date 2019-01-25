print('*** Numbers ***')
numbers = [1,2,3,4,5]

[x*2 for x in numbers]

print(numbers)
print([x*2 for x in numbers])

print('*** Names ***')
name = 'noel'
print(name)
print([char.upper() for char in name])


print('*** Friends ***')
friends = ['jybai', 'felix', 'maylis']
print(friends)

# Return the first letter of each name in Uppercase
friends_v2 = [friend[0].upper() for friend in friends]

# Print every 2nd character of each name in Uppercase
print([friend[0:len(friend):2].upper() for friend in friends])
print(friends_v2)

# Capitalise the first letter of each name
print([friend.capitalize() for friend in friends])

print('*** Bools ***')
# Boolean checker
print([bool(val) for val in [0, [], '']])

print('*** Ints -> Strings ***')
nums = [1,2,3,4,5]
string_list_nums = [str(num) for num in nums]
print(string_list_nums)
type(string_list_nums) # --> List
type(string_list_nums[0]) # --> String

print('*** Colours ***')
colors = ['purple', 'teal', 'magenta', 'crimson', 'emerald']

print('*** Numbers Conditionals ***')
nums_conditionals = [1,2,3,4,5,6]

evens = [num for num in nums_conditionals if num % 2 == 0]
odds = [num for num in nums_conditionals if num % 2 != 0]

print('Evens: ', evens) # [2,4,6]
print('Odds: ', odds) # [1,3,5]

evenOdd = [num*2 if num % 2 == 0 else num/2 for num in numbers] # [0.5, 4, 1.5, 8, 2.5, 12]
print('Even numbers multiplied by 2, odd numbers divided by 2:',evenOdd)