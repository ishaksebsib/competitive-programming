
# NUMBER OF GOOD PAIRS LEETCODE PROBLEM SOLUTION 

'''
1. create a fucniton that accept list of integers
2. create a variable with value of 0 to add number of pairs later on
3. create a loop with length of list of numbers that accepted from user 
4. create another loop to loop through the list by increasing 1 index forward 
5. compare the values of first loop and the second then add 1 to the variable if it true else pass 

'''
def numIdenticalPairs(nums):
    pairs = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                pairs+=1
    return pairs
  
  
  
# example list
nums = [1,2,3,1,1,3]

