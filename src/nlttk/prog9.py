def display9():
    code = '''punctuation = "!@#$%^&*()_[]{}\\\\?/.,<>"

text = input("Enter the string: ")
no_punc = ""

for char in text:
    if char not in punctuation:
        no_punc = no_punc + char

print("String without punctuation:", no_punc)

str=input("enter a string:")
words=str.split()
words.sort()
for word in words:
    print(word)'''
    print(code)
