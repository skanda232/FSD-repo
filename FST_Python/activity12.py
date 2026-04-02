def recusive(sum):
    if sum == 0:
        return 0
    else:
        return sum + recusive(sum - 1)
    
result = recusive (5)
print(result)