import heapq

file = open("input.txt","r")

list1 = []
list2 = []

for line in file:
    nums = line.split("   ")
    heapq.heappush(list1, int(nums[0]))
    heapq.heappush(list2, int(nums[1]))

sum = 0
while(len(list1) > 0):
    elem1 = heapq.heappop(list1)
    elem2 = heapq.heappop(list2)
    sum += abs(elem1 - elem2)

print(sum)