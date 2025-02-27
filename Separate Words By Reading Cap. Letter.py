#example 'HelloWorld' will output Hello World
def test(word):
    result = " "
    for i in word:
        if i.isupper():
            result = result + " " + i.upper()
        else:
            result = result + i
    return result[1:]


string = input("Enter a string: ")
print(test(string))
