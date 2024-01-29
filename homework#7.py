7-1-2-3
#task 1
#1. რეკურსიის დახმარებით შექმენი ფუნქცია, რომელიც იმდენჯერ დაბეჭდავს მისალმებას,
# რა რიცხვსაც გადასცემ არგუმენტად. (ციკლის გამოყენება არ შეიძლება)

def greeting(a):
    if a == 0:
        return ""
    else:
        return "hello\n" + greeting(a - 1)

a = int(input("Enter your number of greetings:"))
result = greeting(a) 
print(result)

#task2
#2. შექმენი ფუნქცია, რომელიც მიიღებს შეკვეთას, ანუ კერძის სახელს და რაოდენობას და დაბეჭდავს მას, 
#თუმცა რაოდენობას თუ არ მივუთითებთ შეცდომას არ ამოაგდებს და 1_ად ჩათვლის.
def dishorder (dishname, amount_of_portions=1):
    print(f"""
          Dish: {dishname}
          Portions: {amount_of_portions}""")
    return dishorder
dishorder_function=dishorder
result=dishorder_function("fhkhali")
print(result)

#task 3
#3. შექმენი ფუნქცია, რომელიც მიიღებს მინიმუმ 3 რიცხვს, და დააბრუნებს და დაბეჭდავს ნარმავლს.
def multiply(a,b,c):
    result=a*b*c
    return result
multiply_function=multiply
result=multiply_function(5,4,6)
print(result)