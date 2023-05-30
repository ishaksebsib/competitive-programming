class Solution:
    # create a methond that accept argument 
    def fizzBuzz(self, n: int) -> List[str]:

        # an empty list to add result later on
        result = []
        
        # a for loop that runs for range of N given number so that we see each number individually 

        for i in range(1,n+1):
            # checking the number wather divided by 3 and 5 
            if i%3==0 and i%5==0:
                # if it's divided  then add "FizzBuzz" on the list variable called result
                result.append("FizzBuzz")
            elif i%3==0:
                result.append("Fizz")
            elif i%5==0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result