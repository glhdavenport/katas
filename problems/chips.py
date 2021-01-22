""" 
position =  [1,2,3]
            [1,3,3]
            [3,3,3]
Output: 1
First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.


Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at poistion 3 to position 2. 
Each move has cost = 1. 
The total cost = 2.

[2, 2, 2, 3, 3]
{
    position: num_tokens
    2: 3
    3: 2
}

[1, 3, 5]
{   
    1:1,
    3:1,
    5:1
}

(3-1) % 2 == 0 --> free

{
    1: [(3:0, 5:0),],
    3: [(1:0, 5:0),],
    5: [(1:0, 3:0),]
}

# if all costs are zero, output zero

[1, 3, 6, 6]


counters = {
    1:1, 
    3:1,
    6:3
}

6-1 = 5 %2 == 1 --> cost 1

{   end_pos: [(start_pos, cost_to_move_there)]
    1: [(3, 0), (6, 1*3)],
    3: [(1, 0), (6, 1*3)],
    6: [(1, 1), (3, 1)]
}

{
    1: [(3, 0)],
    3: [(1, 0)],
    6: []
}

Input: position = [1, 1_000_000_000]
Output: 1

[1, 3, 6, 6]
even = 3
odd = 2

    for(int chip : chips)
    {
        if(chip % 2 == 0)
        {
            even++; 
        }
        else
        {
            odd++;
        }
    }
    
    return Math.min(even, odd);
}

n%2 == 0 # even - free
n%2 == 1 # odd - cost 1
"""
from typing import List
def minCostToMoveChips(position: List[int]) -> int:
    even: int = 0
    odd: int = 0

    for chip in position:
        if (chip % 2 == 0):
            even += 1
        else:
            odd += 1

    return min(even, odd)

print(minCostToMoveChips([2,2,2,3,3,4,5,6,7,7,7,8,8,8,8]))
