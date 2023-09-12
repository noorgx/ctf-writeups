def complex(a2):
    #vaild=ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}    
    v3 = (a2 + 65) % 122
    if v3 <= 64:
        v3 += 61
    
    return v3   


def complex2(a2):
    v3 = (a2 + 65) % 122
    if v3 <= 64:
        v3 += 61
    return v3 



def check_equals(a1, a2):
    aXkNfQuxzwkgzgw = "xk|nF{quxzwkgzgwx|quitH"
    
    for i in range(a2):
        if chr(a1[i]) != aXkNfQuxzwkgzgw[i]:
            return False
    return True


def check(flag,a):
    s = [0] * 24  # Use integers instead of characters
    s_input = flag+a  # Read up to 23 characters from the user

    for i in range(len(s_input)):
        s[i] = complex(ord(s_input[i])) 
        s[i] = complex2(s[i])  # Pass ord(s_input[i]) - 1 instead of ord(s_input[i])

    #path_explode(s[0], s[1])  # Pass integers, not characters
    return check_equals(s, len(s_input))
    
def main():
    flag=""
    lis="ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}"
    while len(flag) != 23:
        for i in lis:
            if check(flag,i):
                flag=flag+i
                print(flag)
            
    
main()