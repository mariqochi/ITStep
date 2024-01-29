11-1-2-3

11-1
#1. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას, თუმცა უნიკალური ელემენტებით (გამოიყენე set მონაცემთა ტიპი).
def unique_list(*args):
  
    for i, elements in enumerate(args):
       
        unique_set = set(elements)
        uniq_list = list(unique_set)
        
        print (F"Your unique list is: {uniq_list}")
        return uniq_list
        
my_list = [1, 2, 2, 3, 4, 4, 5]
rezult_list=unique_list(my_list)

#მეორე ვარიანტი
def unique_list(input_list):  
    unique_set = set(input_list)
    uniq_list = list(unique_set)
        
    print (F"Your unique list is: {uniq_list}")
    return uniq_list

input_list = [1, 2, 2, 3, 4, 4, 5]
rezult_list=unique_list(input_list)

11-2
#2. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე set ტიპის მონაცემს უნიკალური ელემენტებით, რომლის შეცვლაც შეუძლებელი იქნება (გამოიყენე frozenset).

def immutable_set(input_list):
    your_set = set(input_list)
    frozen_set = frozenset(your_set)
    print(f"Your frozen set is: {frozen_set}")
    return frozen_set

input_list = [1, 2, 3, 3, 4]
result_set = immutable_set(input_list)


11-3

#3. შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს tuple ტიპის მონაცემად და დააბრუნებს შედეგს.

def set_to_tuple(a, b):
    union_set = a.union(b)
    my_tuple = tuple(union_set)
    print(f"Your tuple is: {my_tuple}")
    return my_tuple

set1 = {1, 2, 3}
set2 = {1,3, 4, 5}
result_tuple = set_to_tuple(set1, set2)