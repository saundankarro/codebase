if __name__ == '__main__':
    s = input()
    func_list = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    for func in func_list:
        print(any(func(char) for char in s))
