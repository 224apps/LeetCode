def isPalindrome(self, x):
    if x< 0 or (x % 10 == 0 and x != 0):
        return false
    reverseNumber = 0
    while x > reverseNumber :
        reverseNumber = reverseNumber * 10 + x % 10
        x/= 10
    return x == reverseNumber or x = reverseNumber / 10



def isPalindrome(n):
    num = n
    d = 0
    rev =0
    while n > 0 :
        d = n % 10
        n = n/10
        rev = rev * 10 + d
    if ( num == rev):
        return True
    else:
        return false

