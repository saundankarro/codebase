# Object Oriented Programming

class employee:
    def __init__(self,firstname,lastname,salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = self.firstname + "." + self.lastname + "@kite.com"
        
    def giveRaise(self,salary):
        self.salary = salary
        
class developer(employee):
    def __init__(self,firstname,lastname,salary,programming_languages):
        super().__init__(firstname,lastname,salary)
        self.prog_lang = programming_languages
        
    def addLanguage(self,lang):
        self.prog_lang += [lang]
        
employee1 = employee("Jon","Smith",80000)
print(employee1.salary)

employee1.giveRaise(100000)
print(employee1.salary)

dev1 = developer("Joe","Montana",100000,["Python","C"])

print(dev1.salary)

dev1.giveRaise(125000)

dev1.addLanguage("Java")

print(dev1.prog_lang)

# Formatting Strings for Printing

name = "Bob"
age = 25

string = "Hi my name is %s and I am %i years old." %(name,age)

# %s for string
# %i for integers
# %x for hexadecimals
# %f for floating point numbers

print(string)

# formatted string literals (f strings)

name = "Bob"

string1 = f"Hello, { name }"

print(string1)

string2 = f"1 + 1 = { 1 + 1 }"
print(string2)

# Leveraging Python's Data Structures (List vs Dict vs Set)

# Using lists as a stack
stack = []

stack.append(1)
stack.append(2)

pop_elem = stack.pop()

print(stack,pop_elem)

# Using lists as a queue
queue = []

queue.append(1)
queue.append(2)

pop_elem = queue.pop(0)

print(queue,pop_elem)
