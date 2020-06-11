import random

list_ = [random.randint(1, 100) for _ in range(10)]
print(list_)

def quicksort(my_list):
    if len(my_list) < 2:
        return my_list

    mainElem = my_list[0]
    lessElems = [i for i in my_list if i <= mainElem]
    largeElems = [i for i in my_list if i > mainElem]

    return quicksort(lessElems) + [mainElem] + quicksort(largeElems)


l = quicksort(list_)
print(l)
print(list_)