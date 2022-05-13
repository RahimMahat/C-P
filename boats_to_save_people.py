'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
'''

def numRescueBoats(people, limit) -> int:
        people.sort()                               # sort the array
        left, right, boats = 0, len(people)-1, 0    # make a starting and ending pointer and boats counter
        
        while left <= right:                        # run the loop till left is less than equal to right
            if left == right:                       # if both come at same position increase boats count and break
                boats += 1
                break
                
            if people[left] + people[right] <= limit:   # if left and right side weight is less than equal to limit move pointers and increase boat count else just move right pointer to left and increase boats count
                left += 1
            
            right -= 1
            boats += 1
                
        return boats

people = [3, 2, 2, 1]
limit = 3
res = numRescueBoats(people, limit)
print(res)