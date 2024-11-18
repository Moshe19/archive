# Просчитать сумму всех числовых элементов в объекте
# array = [1, 2, [3, 4, (5), 6, (7), 8], 1]
# решение 1
# def recursive_sum(array):
#     global sm
#     iterable = []
#     for el in array:
#         if hasattr(el, '__iter__'):  #Проверяем делимый ли объект
#             iterable.append(el)
#         elif type(el) in [int, float]:
#             sm += el
    
#     for el in iterable:
#         recursive_sum(el)
# array = [1, 2, [3, 4, (5), 6, (7), 8], 1]*1000
# sm = 0
# recursive_sum(array)
# print(sm)
        
        
# решение 2

def recursive_sum(*args, path=[]):
    total_sum = 0 
    for index, arg in enumerate(args):
        if hasattr(arg, '__iter__') and not isinstance(arg, str):
            total_sum += recursive_sum(*arg, path=path+[index]) 
        elif isinstance(arg, (int, float)):
            total_sum += arg  
        elif isinstance(arg, str):
            print(f"Строка '{arg}' на позиции", ''.join(f'[{n}]' for n in path+[index]))
    return total_sum 

array = [1, 2, 'abc', [3, 4, (5), 6, {7, 'xyz'}, 8], 1]  
recursive_sum(*array) 