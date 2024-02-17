import copy
from typing import List
import random
import time

# print(copy.__doc__)
# print(copy.__all__)

# lst: List[int] = [4, '55', 5454]

# binary search algorithm

if __name__ == '__main__':

	start = time.perf_counter()
	list0 = [elt for elt in range(-10_500_000, 10_500_000)]
	list0 = sorted(list0)
	left_bord, right_bord = 0, len(list0)-1
	search_elt = -10_456_980

	while left_bord <= right_bord:
		middle = (left_bord + right_bord) // 2
		if list0[middle] == search_elt:
			print(f'\nelt which i try to find: {list0[middle]}')
			print(f'elt which u ask to find: {search_elt}')
			print(f'position in list: {middle}/{len(list0)}')
			break
		elif list0[middle] < search_elt:
			left_bord = middle + 1
		elif list0[middle] > search_elt:
			right_bord = middle - 1
		else:
			print(f'no {search_elt} in list0')
			break
	runtime = time.perf_counter() - start
	print(f"\ntook {runtime:.4f} secs")
