'''@ author
Gianni M. Javier'''

local_val = "magical unicorns" # local variable

def square(x):      # functon
    return x * x

class User:     # Class
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

# in the same file, add the following below the User class
print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())

print(__name__)
# prints the value of key name found in 
# locals() dictionary

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)

# We can use this conditional to prevent blocks 
# of code from executing unless the file is being
# run directly.

'''if __name__ == "__main__":
    product = Product([args])
    print(product)
    print(product.add_tax(0.18))
'''





