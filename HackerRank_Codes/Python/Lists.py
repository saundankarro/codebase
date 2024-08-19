

if __name__ == '__main__':
    N = int(input())
    res = []

def insert(args):
    res.insert(int(args[0]), int(args[1]))

def append(args):
    res.append(int(args[0]))

def remove(args):
    res.remove(int(args[0]))

def sort(args):
    res.sort()

def pop(args):
    res.pop()

def reverse(args):
    res.reverse()

def print_list(args):
    print(res)

# Create a dictionary to act as a switch-case
commands = {
    "insert": insert,
    "append": append,
    "remove": remove,
    "sort": sort,
    "pop": pop,
    "reverse": reverse,
    "print": print_list
}

# Process each command
for _ in range(N):
    command, *args = input().split()
    # Use the command dictionary to call the appropriate function
    commands[command](args)