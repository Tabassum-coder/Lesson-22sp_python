#Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not.
#  If it's a palindrome, then it is the same after being reversed.

def palindrome(t):
    e=len(t)-1
    s=0
    while(s<e):
        if (t[s]!=t[e]):
            return False
        s+=1
        e-=1
    return True

tup=(1,2,3,3,2,1)

if palindrome(tup):
    print(tup, " is palindrome")
else:
    print(tup," is not palindrome")