"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### TODO

	#confirm input array is sorted
	#performance could be increased by
	#just doing this once in binary_search
	#mylist = sorted(mylist)

	mid = (left + right) // 2

	if (mylist[mid] != key and left >= right):
		return -1

	if (mylist[mid] == key): 
		return mid
	elif (mylist[mid] < key):
		return _binary_search(mylist, key, mid + 1, right)
	elif (mylist[mid] > key):
		return _binary_search(mylist, key, left, mid - 1)
	




	###




def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `search_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO

	start_time = time.time()
	search_fn(mylist, key)
	end_time = time.time()
	return (end_time - start_time) * 1000
	#end_time - start_time -> time elapsed, times 1000 to convert to ms


	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO

	results = []

	for size in sizes:

		test_list = list(range(int(size)))

		linear_size = time_search(linear_search, test_list, -1)
		binary_size = time_search(binary_search, test_list, -1)

		results.append((size, linear_size, binary_size))
	
	return results


	###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))


#print_results(compare_search())
"""
The above evaluates to:

 % python3 main.py
|            n |   linear |   binary |
|--------------|----------|----------|
|       10.000 |    0.002 |    0.002 |
|      100.000 |    0.004 |    0.003 |
|     1000.000 |    0.038 |    0.011 |
|    10000.000 |    0.383 |    0.005 |
|   100000.000 |    3.812 |    0.006 |
|  1000000.000 |   41.543 |    0.024 |
| 10000000.000 |  542.593 |    0.032 |

Yes, these results are pretty in line with our run time assessment,
though there is some loss to performance due to my probably not 100%
optimal implementation. I'd imagine there is also some loss in time 
due to all the recursive calls
"""


"""
Question 10
------------
The worst case complexity for linear searching a list of n elements k times is O(nk)
The worst case complexity for binary searching a list of n elements k times in O(klogn)

For input < 10, the binary search after sorting is faster. Otherwise, for an unsorted list 
It is better to just stick to linear search
"""