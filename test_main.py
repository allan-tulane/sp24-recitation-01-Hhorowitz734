from main import *



def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1


def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	assert binary_search([1,3,5,7,200,500], 500) == 5
	assert binary_search([5,17,26,66,800,1233,1344], 17) == 1
	assert binary_search([1, 2, 5, 8, 15, 23, 43, 533, 1002, 3443, 7766], -1) == -1

	#The worst case runtime for binary search is the case
	#Where the item is not in the list, causing the algorithm
	#To run for logn iterations

	#The base case input to my implementation of binary search is one s.t. 
	#the key is at idx (left + right) // 2, as it then runs for
	#Only one iteration


def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1
