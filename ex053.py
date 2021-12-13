#Python Exercise 53: Create a program that reads any sentence and says if it is a palindrome, disregarding spaces.
#Examples of palindromes:
#redivider, deified, civic, radar, level, rotor, kayak, reviver, racecar, madam, and refer.
string = input('Enter a word and know if it is a string: ') #enter the string
string_without_space = string.replace(' ', '') #remove the spaces of the phrase
string_lower = string_without_space.lower()#configure out the phrase to lower case
invert_string = string_lower[::-1] #invert the number index of the string
if invert_string == string_lower:
    print('The word \033[33m{}\033[m is a palindrome!'.format(string))
else:
    print("The word \033[36m{}\033[m isn't a palindrome".format(string))
print('The word in reverse is \033[35m{}\033[m'.format(string[::-1]))