#1.Python program to add two numbers
str1 = input("Enter the value of str1 : ")
str2 = input("Enter the value of str2 : ")
a = len(str1)
b = len(str2)
if a==b:
    if sorted(str1)==sorted(str2):
        print("anagram")
    else:
        print("not an anagram")
