a = [-2,4,-3,2,3,-1,2,-4,-3,5]

#O(n^2)
length = len(a)
start=0
end=0
result=0
for i in range(length):
    sum=0
    for j in range(i,length):
        sum+=a[j]
        if sum > result:
            result = sum
            start=i
            end=j
print(start,end,result)

#O(n)
sum=a[0]
result=a[0]
start=0
end=0
for i in range(1,len(a)):
    sum+=a[i]
    if sum < a[i]:
        sum = a[i]
        start = i
    if sum > result:
        result = sum
        end = i
print(start,end,result)


#O(n*logn)
def max_subarray_sum(a, start, end):
    if start == end:
        return a[start]
    mid = (start + end) // 2
    left_max = max_subarray_sum(a, start, mid)
    right_max = max_subarray_sum(a, mid + 1, end)
    cross_max = max_crossing_sum(a, start, mid, end)
    return max(left_max, right_max, cross_max)

def max_crossing_sum(a, start, mid, end):
    left_sum = float('-inf')#negative infinity
    sum = 0
    for i in range(mid, start - 1, -1):#reversing searching
        sum += a[i]
        if sum > left_sum:
            left_sum = sum
    right_sum = float('-inf')
    sum = 0
    for i in range(mid + 1, end + 1):
        sum += a[i]
        if sum > right_sum:
            right_sum = sum
    return left_sum + right_sum

a = [-2, 4, -3, 2, 3, -1, 2, -4, -3, 5]
result = max_subarray_sum(a, 0, len(a) - 1)
print("Maximum subarray sum:", result)