
#1. დაწერე ფუნქცია რომელიც ლექსიკონიდან დუბლიკატებს ამოშლის და ყველა უნიკალური value_ს მქონე ლექსიკონს დააბრუნებს.

def remove_dublicates(input_dict):
    new_dict={}
    for key, value in input_dict.items(): 
     
        if value not in new_dict.values():
            new_dict[key]=value

    return new_dict

my_dict={'a':1, 'b':2, 'c':3, 'd':2}
result_list=remove_dublicates(my_dict)
print(result_list)

#2.დაწერე ფუნქცია რომელიც შეამოწმებს გადაცემული ლექსიკონი ცარიელია თუ არა და დააბრუნებს შესაბამის პასუხს.


def is_empty_dict(input_dict):
    if not input_dict:
        print("The dictionary is empty")
    else:
        print("The dictionary is not empty")


input_dict = {"a": [2, 4, 5]}
#input_dict = {}
is_empty_dict(input_dict)


#3. დაწერე ფუნქცია, რომელიც გადაცემული სტრიქონისგან ლექსიკონს შექმნის და დააბრუნებს. ვთქვათ გადავეცით ფუნქციას სტრიქონი, 
#უნდა დააბრუნოს სიმბოლოები key_ს ადგილას და მათი რაოდენობა value_ს ადგილას. მაგალითად გადავეცით სტრიქონი :
# 'racoon' უნდა დააბრუნოს ლექსიკონი: {'r': 1, 'a': 1, ‘c': 1, 'o': 2, ‘n': 1}





def from_dict_to_string(input_string):
    my_dict_count = {}

   
    for char in input_string:
    
        if char in my_dict_count:
 
            my_dict_count[char] += 1
        else:
           
            my_dict_count[char] = 1

  
    return my_dict_count


input_string = 'racoon'
result = from_dict_to_string(input_string)

print(result)