aprint('*** Numbers ***')
numbers = [1,2,3,4,5]

[x*2 for x in numbers]

print(numbers)
print([x*2 for x in numbers])

print('*** Names ***')
myName = 'noel'
print(myName)
print([char.upper() for char in myName])


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


print('*** Vowels ***')
with_vowels = 'This is too much fun!'
''.join(char for char in with_vowels if char not in "aeiou")
print(with_vowels)
print(''.join(char for char in with_vowels if char not in "aeiou"))
# 'Ths s s mch fn!'

print('*** In - Number Lists ***')
list1 = [1,2,3,4]
list2 = [3,4,5,6]
answerNumListIn = [num for num in list1 if num in list2]
print(answerNumListIn)
## [3,4] 

print('*** Reverse + lower() - Name Lists ***')
names = ['Elie', 'Tim', 'Matt']
print(names)
answerNameList = [name[::-1].lower() for name in names]
print(answerNameList)

print('*** Mod - Number Lists ***')
numbersMod = list(range(1,101))
# print(numbersMod) # [1,2,3,...99,100]
answerNumbersMod = [num for num in numbersMod if num%12==0]
print(answerNumbersMod)
# [12, 24, 36, 48, 60, 72, 84, 96]

print('*** ''.join - String ***')
amaze = 'amazing'
answerJoin =  [''.join(char) for char in amaze if char not in 'aeiou']
# answerJoin = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]
print(answerJoin)
# ['m', 'z', 'n', 'g']

print('*** Nested Number List ***')
nested_number_list = [[1,2,3],[4,5,6],[7,8,9]]
[[print(val) for val in l] for l in nested_number_list]
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9