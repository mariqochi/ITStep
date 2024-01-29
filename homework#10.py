#Homework 10

#1. დაწერე ფუნქცია რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას.
from random import randint


def list_generator(n, k):
    arr = []
    for i in range(n):
        arr.append(randint(1, k))
    return arr

a = list_generator(10, 1500)
print(a)
#2. დაასორტირე შექმნილი სია რომელიმე ოპტიმალური მეთოდით.
def selection_sort(some_arr):
    arr = some_arr
    indexing_length = range(0, len(arr) - 1)

    for i in indexing_length:
        min_value = i 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j

        
        if min_value != i:
            arr[min_value], arr[i] = arr[i], arr[min_value]
    print("Selection Sort!")
    return arr
print(a)
sorted_list=selection_sort(a)
print(sorted_list)

#4. დათვალე ძიების თითოეული მეთოდისთვის საჭირო დრო (დეკორატორის გამოყენებით) და დააკვირდი დროში სხვაობას მცირე, საშუალო და გრძელი სიის შემთხვევებში.

from time import time

def make_change(func):
    def inner(*args, **kwargs):   #არგუმენტების გადაცემა მომთხოვა უნივერსალური ფუნქციის შესაქმნელად
        start = time()
        result = func(*args, **kwargs)
        end = time()
        x = end - start
        print(f"Time taken for linear search: {x} seconds")
        return result
    return inner
#3. დასორტირებულ სიაში ელემენტის მოსაძებნად გამოიყენე ხაზობრივი და ბინარული ძიება.
@make_change
def search_linear(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


search_element = int(input("Enter the element for lenear search: "))

#a = list_generator(10, 100)
result = search_linear(sorted_list, search_element)

if result != -1:
    print(f"Element {search_element} found at index {result}")
else:
    print(f"Element {search_element} does not exist in list 'a'")


from time import time

def make_changer_for_binary(func):   #მეორედ იმიტომ ჩავწერე რომ აუტპუტში "Time taken for binary search" ჩანაწერი  გამოეტანა
    def inner(*args, **kwargs):   #არგუმენტების გადაცემა მომთხოვა უნივერსალური ფუნქციის შესაქმნელად
        start = time()
        result = func(*args, **kwargs)
        end = time()
        x = end - start
        print(f"Time taken for binary search: {x} seconds")
        return result
    return inner

@make_changer_for_binary 
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)

        else:
            return binary_search(arr, mid+1, high, x)

    else:
        return -1

search_element2 = int(input("Enter second element for binary search: "))

#a = list_generator(10, 100)
result = binary_search(sorted_list, 0, len(a)-1, search_element)

if result != -1:
    print(f"Element {search_element} found at index {result}")
else:
    print(f"Element {search_element} does not exist")
    result =binary_search(sorted_list,0, len(a)-1,search_element)


#[538, 932, 192, 1264, 1235, 805, 763, 412, 227, 283]
#Selection Sort!
#[192, 227, 283, 412, 538, 763, 805, 932, 1235, 1264]
#Enter the element for lenear search: 1235
#Time taken for linear search: 0.0 seconds
#Element 1235 found at index 8
#Enter second element for binary search: 1235
#Time taken for binary search: 0.0 seconds
#Time taken for binary search: 0.0009996891021728516 seconds
#Time taken for binary search: 0.0009996891021728516 seconds  binary-ს მეტი დრო მოანდომა პატარა სიაში
#Element 1235 found at index 8