def linearsearch(nums, N, target):
    for i in range(N):
        if (nums[i] == target):
            return i
    return -1
 
 
# Driver Code

nums = list(map(int,input().split()))
target = int(input())
N = len(nums)
 
# Function call
ans = linearsearch(nums, N, target)
if(ans == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", ans)