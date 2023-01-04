def countingValleys(steps, path):
    # Write your code here
    count = 0
    result = 0
    for i in range(steps):
        if path[i] == 'U':
            count += 1
        else:
            count -= 1
        if count == 0 and path[i]=='U':
            result += 1
            
    return result
