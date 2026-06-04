# Given two lowercase English letters separated by a space,
# convert each letter to its alphabetical position (a=1 to z=26)
# and print the sum of the two positions.

char1 = input()
char2 = input()
char1 = char1.lower()
char2 =char2.lower()
sum1 = ord(char1) - ord('a')+1
sum2 = ord(char2) - ord('a')+1
total = sum1 + sum2
print(total)