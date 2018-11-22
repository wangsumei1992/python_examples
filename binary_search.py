"""二分查找法前提是必须是按顺序排序的列表"""
def binary_search(list, val):
    low = 0                       #最小数下标
    high = len(list) - 1          #最大数下标
    while low <= high:
        mid = (low + high) // 2   #中间数下标
        if list[mid] == val:      #如果中间数与目标值相等
            return mid
        elif list[mid] > val:     #如果val值在中间数左边，移动high下标
            high = mid - 1
        else:
            low = mid + 1         #如果val在中间数右边，移动low下标
    return

set = binary_search([1,2,3,4,5], 3)
print(set)
