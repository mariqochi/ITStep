#task1
#1. დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sort() მეთოდის გამოყენებით (ზრდადობით)
from random import randint
def list_f():
    new_list = []
    for i in range(10):
        new_list.append(randint(1, 100))
    #print(new_list)
    return new_list


new_list=list_f()
print(new_list)
new_list.sort()
print(new_list)


#task2
#2. დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sorted() ფუნქციის გამოყენებით (კლებადობით)
from random import randint
def list_f():
    new_list = []
    for i in range(10):
        new_list.append(randint(1, 100))
    #print(new_list)
    return new_list

new_list=list_f()
print(new_list)

sorted_list=sorted(new_list, reverse=True)
print(sorted_list)   

#3
#დაწერე პროგრამა რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას და შექმნილი სიის სორტირება
#სცადე ორი განსხვავებული მეთოდით (მაგ. Bubble და Selection). დათვალე თითოეული მეთოდისთვის სორტირებისთვის საჭირო დრო 
#და დააკვირდი რომელი უფრო ეფექტურია მცირე(1000 ელემენტი), საშუალო(2000 ელემენტი) და გრძელი(3000 ელემენტი) სიის შემთხვევებში



from random import randint
from time import time

def list_f(num_elements):
    new_list = []
    for i in range(num_elements):
        new_list.append(randint(1, 100))
    return new_list


num_elements = int(input("Enter the number of elements in the list: "))

a = list_f(num_elements)

def make_change(func):
    def inner():
        start = time()
        result = func(a) 
        end = time()
        x = end - start
        print(f"Time taken: {x} seconds")
        return result
    return inner

@make_change
def bubble(list_a):
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]

    print("Bubble sort!")
    return list_a

sorted_list = bubble() 



#Enter the number of elements in the list: 1000
#Time taken: 0.07382559776306152 seconds --- მცირე ელემენტიან სიაზე ყველაზე ეფექტურია
#Enter the number of elements in the list: 2000
#Time taken: 0.316164493560791 seconds
#Enter the number of elements in the list: 3000
#Time taken: 0.6961500644683838 seconds

