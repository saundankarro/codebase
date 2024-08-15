def print_formatted(number):
    # your code goes here
    spc_len = len(bin(number))-1
    print(spc_len)
    return [print(f"{str(i).rjust(spc_len)}{oct(i)[2:].rjust(spc_len)}{hex(i)[2:].upper().rjust(spc_len)}{bin(i)[2:].rjust(spc_len)}") for i in range(1,number+1)]


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)