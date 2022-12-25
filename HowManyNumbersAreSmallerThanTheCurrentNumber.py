'''
1 : create fuction that resive list of numbers 
2 : loop to the list using for loop 
3 : it picks the first value from loop then loop again to the list and compare the first number to all others and return value
'''


def smallerNumbersThanCurrent(nums):
        result = []
        for i in nums:
            value = 0
            for k in nums:
                if i > k:
                    value += 1
            result.append(value)
        return result
        

#sample list
nums = [8,1,2,2,3]
