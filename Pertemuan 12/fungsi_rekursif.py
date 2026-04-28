'''
sumber = https://www.geeksforgeeks.org/dsa/recursion-algorithms/ 
'''
def sum(n):
    
    # base condition
    if n == 1:
        return 1
    
    return n + sum(n - 1)

if __name__ == "__main__":
    n = 5
    print(sum(n))

#

#PALINDORME
# Helper recursive function
def isPalindromeRec(s, left, right):
        
    # Base case
    if left >= right:
        return True
        
    # If mismatch found
    if s[left] != s[right]:
        return False
        
    # Recursive call with narrowed range
    return isPalindromeRec(s, left + 1, right - 1)
    
def isPalindrome(s):
    return isPalindromeRec(s, 0, len(s) - 1)


if __name__ == "__main__":
    s = "abba"
    
    if isPalindrome(s):
        print("true")
    else:
        print("false")

#TOWER OF HANOI 
def TowerOfHanoi(n, fromRod, toRod, auxRod):
    if n == 0:
        return
    TowerOfHanoi(n-1, fromRod, auxRod, toRod)
    print("Disk", n, " moved from ", fromRod, " to ", toRod)
    TowerOfHanoi(n-1, auxRod, toRod, fromRod)

if __name__ == "__main__":
    n = 3
    
    # A, C, B are the name of rods
    TowerOfHanoi(n, 'A', 'C', 'B')