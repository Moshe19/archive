# # Напишите функцию, которая будет принимать список чисел и возвращать два числа, абсолютная разность которых минимальна.
# # Пару чисел нужно вернуть в виде списка, отсортированного по возрастанию.

# def min_difference_pair(nums):
#     nums.sort()
#     return list(min([i for i in zip(nums, nums[1:])], key = lambda x: x[1] - x[0]))
    
# print(min_difference_pair ([1, 5, 10, 23, 34, 12, 0, -5, -2]))


# Напишите функцию, которая будет принимать список чисел и проверять, является ли каждое число больше суммы всех предыдущих чисел.

def greater_than_sum(nums):
    i = 2
    while i <= len(nums):
        return all(nums[i] > sum(nums[:i]) for i in range(1, len(nums)))



print(greater_than_sum ([2, 3, 7, 13, 28]))  