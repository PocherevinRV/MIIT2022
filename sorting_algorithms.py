import math
import time
import random

NUMBER_OF_ELEMENTS_IN_TEST_LIST = 100000
NUMBER_OF_TESTS = 1000
RAND_MAX = 100000

def generate_list(number_of_elements):
    list_ = [0] * number_of_elements
    for index in range(number_of_elements):
        list_[index] = random.randint(-RAND_MAX, RAND_MAX)
    return list_


def BubbleSort(list_):
    swapped = True
    last_index = len(list_)
    while swapped:
        swapped = False
        for index in range(last_index - 1):
            if list_[index] > list_[index + 1]:
                list_[index], list_[index + 1] = list_[index + 1], list_[index]
                swapped  = True
        last_index -= 1
    return list_

def sort_check(list_):
    for index in range(len(list_) - 1):
        if list_[index] > list_[index + 1]:
            return False
    return True

def test(func):
    total_timer = 0
    for test_number in range(NUMBER_OF_TESTS):
        test_list = generate_list(NUMBER_OF_ELEMENTS_IN_TEST_LIST)
        timer = time.time()
        test_list = func(test_list)
        timer = time.time() - timer
        total_timer += timer
        if sort_check(test_list):
            print("Required time in test №", test_number + 1, "is", timer, "seconds")
        else:
            print("Error in test №", test_number + 1)
    print("Required time for", NUMBER_OF_TESTS, "tests is", total_timer, "seconds")
    print("Average time for", NUMBER_OF_TESTS, "tests is", total_timer/NUMBER_OF_TESTS, "seconds")

def search_test(func):
    total_timer = 0
    test_list = sorted(generate_list(NUMBER_OF_ELEMENTS_IN_TEST_LIST))
    for test_number in range(NUMBER_OF_TESTS):
        timer = time.time()
        search_elem = random.randint(-RAND_MAX, RAND_MAX)
        answer = func(test_list, search_elem)
        timer = time.time() - timer
        total_timer += timer
        if not(search_check(test_list, search_elem, answer)):
            print("Error in test №", test_number + 1)
    print("Total time for", NUMBER_OF_TESTS, "tests is", total_timer, "seconds")
    print("Average time for", NUMBER_OF_TESTS, "tests is", total_timer/NUMBER_OF_TESTS, "seconds")

def simple_search(list_, search_elem):
    for index in range(len(list_)):
        if list_[index] == search_elem:
            return index
    return None

def binary_search(list_, search_elem):
    search_left = 0
    search_right = len(list_) - 1
    while search_left < search_right:
        search_middle = (search_left + search_right) // 2
        if search_elem <= list_[search_middle]:
            search_right = search_middle
        else:
            search_left = search_middle + 1
    if search_left == search_right:
        if list_[search_left] == search_elem:
            return search_left
        else:
            return None
    return None

def old_binary_search(list_, search_elem):
    search_left = 0
    search_right = len(list_) - 1
    while search_left < search_right:
        search_middle = (search_left + search_right) // 2
        if search_elem < list_[search_middle]:
            search_right = search_middle - 1
        elif search_elem > list_[search_middle]:
            search_left = search_middle + 1
        else:
            return search_middle
    if search_left == search_right:
        if list_[search_left] == search_elem:
            return search_left
        else:
            return None
    return None


def search_check(list_, search_elem, answer):
    if answer == None:
        for index in range(len(list_)):
            if list_[index] == search_elem:
                return False
        return True
    else:
        '''
        for index in range(answer):
            if list_[index] == search_elem:
                return False
        '''
        if list_[answer] == search_elem:
            return True
        else:
            return False


search_test(simple_search)
search_test(binary_search)
search_test(old_binary_search()binary_search)
#test(BubbleSort)
    
    
