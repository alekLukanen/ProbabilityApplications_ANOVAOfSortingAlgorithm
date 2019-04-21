
import random
import pandas as pd
import numba
import time

'''
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
'''

def timsort(li):
    li.sort()
    return li


def time_timsort_sort(sizes, number_of_tries=10, module='__main__'):
    import timeit
    import time
    data = {'size': [],
            'original_sorting': [],
            'time': []
           }
    for size in sizes:
        print(f'- CHANED TO SIZE: {size}')

        #selection_sort([1])

        for _ in range(0, number_of_tries):
            print(f'-- sorting a random normal list of size {size}: ')
            timeX = timeit.timeit(f'timsort(li)', 
                setup=f"from {module} import timsort, create_random_normal_list; li = create_random_normal_list({size})", number=1)
            data['size'].append(size)
            data['original_sorting'].append('normal(0,1)')
            data['time'].append(timeX)

            print('--', timeX)

        for _ in range(0, number_of_tries):
            print(f'-- sorting a uniform random list of size {size}: ')
            timeX = timeit.timeit(f'timsort(li)',
                setup=f"from {module} import timsort, create_randomized_list; li = create_randomized_list({size})", number=1)
            data['size'].append(size)
            data['original_sorting'].append('uniform(0,1)')
            data['time'].append(timeX)

            print('--', timeX)

        for _ in range(0, number_of_tries):
            print(f'-- sorting a gamma random list of size {size}: ')
            timeX = timeit.timeit(f'timsort(li)',
                setup=f"from {module} import timsort, create_random_gamma_list; li = create_random_gamma_list({size})", number=1)
            data['size'].append(size)
            data['original_sorting'].append('gamma(1,1)')
            data['time'].append(timeX)

            print('--', timeX)

        for _ in range(0, number_of_tries):
            print(f'-- sorting a sorted list of size {size}: ')
            timeX = timeit.timeit(f'timsort(li)', 
                setup=f"from {module} import timsort, create_sorted_list; li = create_sorted_list({size})", number=1)
            data['size'].append(size)
            data['original_sorting'].append('sorted')
            data['time'].append(timeX)

            print('--', timeX)

        for _ in range(0, number_of_tries):
            print(f'-- sorting a reversed list: of size {size}: ')
            timeX = timeit.timeit(f'timsort(li)',
                setup=f"from {module} import timsort, create_reversed_list; li = create_reversed_list({size})", number=1)
            data['size'].append(size)
            data['original_sorting'].append('reversed')
            data['time'].append(timeX)

            print('--', timeX)

    return pd.DataFrame(data=data)


def create_uniform_random_walk(length):
    start = 0.0
    walk = [start]
    for i in range(1,length):
        walk.append(walk[i-1]+random.uniform(-1.0,1.0))
    return walk


def create_sorted_list(size):
    return [i/(size*1.0) for i in range(0, size)]


def create_reversed_list(size):
    return [i/(size*1.0) for i in range(size, 0, -1)]


def create_randomized_list(size):
    '''
    original_list = create_sorted_list(size)
    new_list = []
    for i in range(0, len(original_list)):
        index = random.randint(0, len(original_list)-1)
        new_list.append(original_list[index])
        del original_list[index]
    return new_list
    '''
    return [random.uniform(0.0, 1.0) for i in range(0, size)]


def create_random_normal_list(size):
    return [random.normalvariate(0.0, 1.0) for i in range(0, size)]


def create_random_gamma_list(size):
    return [random.gammavariate(1.0, 1.0) for i in range(0, size)]


if __name__ == '__main__':
    print('--- algorithms.py ---')
    list_sizes = [1_000_000, 2_000_000, 3_000_000]
    runs = 35
    data = time_timsort_sort(list_sizes, number_of_tries=runs)
    data.to_csv('data.csv', index=False)