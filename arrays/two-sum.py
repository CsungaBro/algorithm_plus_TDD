from logger import logger_init
from tester import Tester
class Solution(Tester):
    def twoSum(self, nums, target):
        # print(nums)
        cont = [-1, -1]
        id_nums = [ x for x in range(len(nums))]
        self.quick_sort(nums, id_nums,0, len(nums)-1)
        for count, num in enumerate(nums):
            new_nums = nums[count + 1:]
            new_target = target - num
            other_num = self.binary_search(new_nums, 0, len(new_nums)-1, new_target)
            if other_num == -1:
                continue
            else:
                cont = [count, count + other_num + 1] 
                break
        # print(nums)
        # print("\b")
        # print(id_nums)
        return [id_nums[cont[0]], id_nums[cont[1]]]

    def binary_search(self, nums, low, high, target):
        if high >= low:
            mid = int((high + low) // 2)
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                return self.binary_search(nums, low, mid - 1, target)

            elif nums[mid] < target:
                return self.binary_search(nums, mid + 1, high, target)
        else:
            return -1

    def partition(self, arr, id_arr, low, high):
        i=low-1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]
                id_arr[i], id_arr[j] = id_arr[j], id_arr[i]
                
        arr[i+1], arr[high] = arr[high], arr[i+1]
        id_arr[i+1], id_arr[high] = id_arr[high], id_arr[i+1]
        return i+1

    def quick_sort(self, arr, id_arr, low, high):
        if low < high:
            pi = self.partition(arr, id_arr, low, high)

            self.quick_sort(arr, id_arr, low, pi-1)
            self.quick_sort(arr, id_arr, pi+1, high)



tests = [
    [
        [1,2,5,6,8,10,11,15,19],18,[4,5]],
    [
        [2,7,11,15],9,[0,1]
    ],
    [
        [3,2,4],6,[1,2]
    ],
    [
        [3,3],6,[0,1]
    ],
    [
        [0,4,3,0],0,[0,3]        
    ],
    [
        [150,24,79,50,88,345,3],200,[0,3]
    ]
]

S = Solution()
S.tester(S.twoSum, tests)