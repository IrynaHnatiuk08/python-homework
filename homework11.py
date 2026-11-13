import time
n = 500000
target = 499999

my_list = list(range(500000))
my_set = set(my_list)

start = time.perf_counter()
found_list = target in my_list
duration_list = time.perf_counter() - start

start = time.perf_counter()
found_set = target in my_set
duration_set = time.perf_counter() - start

print(f"List search: {duration_list:.6f} сек, Set search: {duration_set:.6f} сек")

