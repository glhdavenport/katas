from typing import List

# Input: a = 2, b = [3]
# Output: 8
# Example 2:

def super_power(a:int, b:List) -> int:    
    exponent = 0
    if not (1 <= a and a <= 2**31 - 1) or not (1 <= len(b) and len(b) <= 6):
        raise ValueError('a is too large.  Must be less than 2^31-1')
    for index, value in enumerate(b):
        exponent += value*10**(len(b)-(index+1))
    return a**exponent % 1337
    


"""
1234

0
+ b[index]*10^(length-index+1) 
+ b[index]*10^(length-index+1) 
+ b[index]*10^(length-index+1) 
+ b[index]*10^(length-index+1) 
"""

if __name__ == "__main__":
    super_power(2, [1,0])