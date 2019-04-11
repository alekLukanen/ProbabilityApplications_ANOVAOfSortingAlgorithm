
import random
import pandas as pd
import numba


@numba.jit(nopython=True)
def selection_sort(li):
    for i in range(0,len(li)):
        current_smallest_index = i
        for j in range(i, len(li)):
            if (li[j]<li[current_smallest_index]):
                current_smallest_index = j
        smallest_value = li[current_smallest_index]
        li[current_smallest_index] = li[i]
        li[i] = smallest_value
    return li


def time_selection_sort(sizes, number_of_tries=10, module='__main__'):
    import timeit
    data = {'size': [],
            'original_sorting': [],
            'time': []
           }
    for size in sizes:
        print(f'- SIZE: {size}')

        selection_sort([1])

        for _ in range(0, number_of_tries):
            print('-- sorting a sorted list: ')
            time = timeit.timeit(f'selection_sort(li)', 
                setup=f"from {module} import selection_sort, create_sorted_list; li = create_sorted_list({size})", number=1)
            data['size'].append(size)
            data['original_sorting'].append('sorted')
            data['time'].append(time)

            print('--', time)

        for _ in range(0, number_of_tries):
            print('-- sorting a randomized list: ')
            time = timeit.timeit(f'selection_sort(li)',
                setup=f"from {module} import selection_sort, create_randomized_list; li = create_randomized_list({size})", number=1)
            data['size'].append(size)
            data['original_sorting'].append('randomized')
            data['time'].append(time)

            print('--', time)

        for _ in range(0, number_of_tries):
            print('-- sorting a reversed list: ')
            time = timeit.timeit(f'selection_sort(li)',
                setup=f"from {module} import selection_sort, create_reversed_list; li = create_reversed_list({size})", number=1)
            data['size'].append(size)
            data['original_sorting'].append('reversed')
            data['time'].append(time)

            print('--', time)

    return pd.DataFrame(data=data)


def create_sorted_list(size):
    return [i for i in range(0, size)]


def create_reversed_list(size):
    return [i for i in range(size, 0, -1)]


def create_randomized_list(size):
    original_list = create_sorted_list(size)
    new_list = []
    for i in range(0, len(original_list)):
        index = random.randint(0, len(original_list)-1)
        new_list.append(original_list[index])
        del original_list[index]
    return new_list


if __name__ == '__main__':
    print('--- algorithms.py ---')
    list_sizes = [10000,20000,30000]
    runs = 35
    data = time_selection_sort(list_sizes, number_of_tries=runs)
    data.to_csv('data.csv', index=False)

    a = selection_sort(create_reversed_list(10))
    print(a)