import random
import timeit

def findMinRec(l, n):
    if (n == 1):
        return l[0]
    min = findMinRec(l, n-1)
    if (l[n-1] < min):
        return l[n-1]
    return min

def findMinRecWithoutLen(l):
    if (len(l) == 1):
        return l[0]
    return min(l[0], findMinRecWithoutLen(l[1:]))
    # min = findMinRecWithoutLen(l[1:])
    # if (l[0]<min):
    #     return l[0]
    # return min

def test_find_min():
    assert findMinRec([34, 56, 12, 3, 14, 15], 6) == 3
    assert findMinRecWithoutLen([34, 56, 12, 3, 14, 15]) == 3

test_find_min()

def cautare(l, el):
    for e in l:
        if e == el:
            return True
    return False

def binary_search(l, low, high, el):
    '''
    index la care se afla el daca e in lista
    altfel, -1
    :param l: l ordonata crescator
    :param el:
    :return:
    '''
    if high>=low:
        middle = (high + low) //2
        if el == l[middle]:
            return middle
        elif l[middle] > el:
            return binary_search(l, low, middle - 1, el)
        else:
            return binary_search(l, middle + 1, high, el)
    else:
        return -1

def test_binary_search():
    lista = [3, 6, 8, 12, 19, 20]
    assert binary_search(lista, 0, len(lista) - 1, 12) == 3
    assert binary_search(lista, 0, len(lista) - 1, 37) == -1


test_binary_search()

def selection_sort(arr):
    for poz in range(0, len(arr) - 1):
        pozMin = poz
        for i in range(poz + 1, len(arr)):
            if arr[i] < arr[pozMin]:
                pozMin = i
        if pozMin > poz:
            arr[pozMin], arr[poz] = arr[poz], arr[pozMin]
    return arr

def insertion_sort(arr):
    for i in range(0, len(arr)):
        ind = i - 1
        valCurenta = arr[i]
        while ind >= 0 and valCurenta < arr[ind]:
            arr[ind + 1] = arr[ind]
            ind-=1
        arr[ind + 1] = valCurenta
    return arr

def interclasare(l, st1, dr1, st2, dr2):
    rez = []
    while st1<dr1 and st2<dr2:
        if l[st1] < l[st2]:
            rez.append(l[st1])
            st1+=1
        else:
            rez.append(l[st2])
            st2+=1
    while st1< dr1:
        rez.append(l[st1])
        st1+=1
    while st2< dr2:
        rez.append(l[st2])
        st2+=1
    return rez

def mergeSortRec(l, start, end):
    if end - start > 1:
        m = (start + end) // 2
        mergeSortRec(l, start, m)
        mergeSortRec(l, m, end)
        lista = interclasare(l, start, m, m, end)
        for i in range(len(lista)):
            l[i+start] = lista[i]
    return l

def quick_sort_refactor(arr):
    if arr == []:
        return  []
    else:
        pivot = arr[0]
        lesser = quick_sort_refactor([x for x in arr[1:] if x < pivot])
        greater = quick_sort_refactor([x for x in arr[1:] if x >= pivot])
        return lesser + [pivot] + greater

def test_sorting():
    assert selection_sort([3, 2, 1, 56, 17, 19, 20]) == [1, 2, 3, 17, 19, 20, 56]
    assert insertion_sort([3, 2, 1, 56, 17, 19, 20]) == [1, 2, 3, 17, 19, 20, 56]
    assert mergeSortRec([3, 2, 1, 56, 17, 19, 20], 0, 7) == [1, 2, 3, 17, 19, 20, 56]
    assert quick_sort_refactor([3, 2, 1, 56, 17, 19, 20]) == [1, 2, 3, 17, 19, 20, 56]

test_sorting()

def work_with_timers():
    lista = []
    for i in range(100000):
        lista.append(random.randint(1, 1000))

    starttime = timeit.default_timer()
    quick_sort_refactor(lista)
    endtime = timeit.default_timer()
    print(endtime - starttime)

    import_module = 'import random'
    test_code = '''
def quick_sort_refactor(arr):
    if arr == []:
        return  []
    else:
        pivot = arr[0]
        lesser = quick_sort_refactor([x for x in arr[1:] if x < pivot])
        greater = quick_sort_refactor([x for x in arr[1:] if x >= pivot])
        return lesser + [pivot] + greater
lista = []
for i in range(10000):
    lista.append(random.randint(1, 1000))
quick_sort_refactor(lista)
    '''
    print('---------- ')
    print(timeit.timeit(stmt=test_code, setup=import_module, number=5))

work_with_timers()