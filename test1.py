import random

def get_random_str(main_str, substr_len):
    idx = random.randrange(0, len(main_str) - substr_len + 1)    # Randomly select an "idx" such that "idx + substr_len <= len(main_str)".
    ans = []
    i = 0
    print(main_str)
    while i <= 100000:
        print(f"inside loop")
        print(f"i = {i}")
        l = list(main_str)
        print(f"l = {l}")
        random.shuffle(l)
        result = ''.join(l)
        print(f"result = {result}")
        fin_str = result[idx : (idx+substr_len)]
        print(f"fin_str = {fin_str}")
        if 'AE' in fin_str and 'DB' in fin_str:
            ans.append(fin_str)
        i+=1
    print(len(set(ans)))


main_str='ABCDE'
get_random_str(main_str,5)
