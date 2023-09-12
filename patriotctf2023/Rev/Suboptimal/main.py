import sys

def complex(a1, a2):
    if a1 <= 64 or a1 > 125:
        print("Suboptimal")
        sys.exit(1)
    
    v3 = (a2 + 65) % 122
    if v3 <= 64:
        v3 += 61
    
    return v3

def complex2(a1, a2):
    v3 = (a2 + 65) % 122
    if v3 <= 64:
        v3 += 61
    return v3

def path_explode(a1, a2):
    for i in range(50):  # Loop from 0 to 49
        result = a1
        if a1 == a2:
            result = print("\n", end="")
    return result

def check_equals(a1, a2):
    aXkNfQuxzwkgzgw = "xk|nF{quxzwkgzgwx|quitH"
    
    for i in range(a2):
        if chr(a1[i]) != aXkNfQuxzwkgzgw[i]:
            print(chr(a1[i]), end="")
            sys.exit(1)
    
    return 0

def main():
    s = ['\0'] * 24
    print("Key: ")
    s_input = input()[:23]  # Read up to 23 characters from the user

    for i in range(len(s_input)):
        s[i] = complex(ord(s_input[i]), ord(s_input[i]))
        s[i] = complex2(ord(s[i]), ord(s_input[i]))

    path_explode(ord(s[0]), ord(s[1]))
    check_equals(s, len(s))
    print("Optimal")

if __name__ == "__main__":
    main()
