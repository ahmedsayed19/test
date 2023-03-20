# print("Ahmed Sayed Ahmed")

def greating(name):
    return f"Hello, {name}"

def thanking(name):
    return f"Thank you, {name}"

name = input('Enter your name: ')

print(greating(name), thanking(name), sep='\n')