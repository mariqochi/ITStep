#task1
#დაწერე პროგრამა რომელიც გადაამრავლებს სიის ყველა წევრს კონკრეტულ რიცხვზე ლამბდას გამოყენებით.
list1 = [1, 2, 3, 4, 5]
print(list1)
a=int(input("Enter multiplier number: "))
multiplier=a

multiply_lambda = lambda x: x * multiplier

list2 = list(map(multiply_lambda, list1))

print(list2)





#task2
#დაწერე პროგრამა ლამბდას გამოყენებით, რომელიც გადაცემული სიის სიგრძეს დააბრუნებს,
# მას შემდეგ რაც წაშლის სიიდან ყველა სახელს რომელიც პატარა სიმბოლოთი იწყება. (გამოიყენე .isupper() მეთოდი)

list1 = ['andria', 'Beso', 'khatia', 'Dato', 'Nino']
resultlist=list(filter(lambda x: x[0].isupper(), list1))
print(resultlist)
listlength=sum(len(element) for element in resultlist)  # ამ პირობაში თითქოს საბოლოოდ სიის სიგრძე უნდა დაგვეთვალა, თუ არასწორად გავიგე ეს ბოლო ორი ხაზი არაა საჭირო
print(listlength)

#task3
#დაწერე პროგრამა რომელიც დააჯამებს სიაში არსებულ დადებით და უარყოფით რიცხვებს ცალცალკე. გამოიყენე ლამბდა ფუნქცია და filter.
list1 = ['5', '-8', '2', '-1', '3']
resultlistpositive=list(filter(lambda x: int(x)>0, list1))
resultlistnegative=list(filter(lambda x: int(x)<0, list1))

print(sum(map(int,resultlistpositive)))
print(sum(map(int,resultlistnegative)))


#task4

#დაწერე ბანკის ექაუნთის შექმნის, ანგარიშზე თანხის განთავსების და შემდგომ ექაუნთში შესვლის პროგრამა,
# არასწორი ინფორმაციის შეყვანა მომხმარებლისგან დააზღვიე try და except ბლოკის მეშვეობით.
registered_username =input("Enter your username to register: ")
registered_password = input("Enter your password to register: ")
entered_username = input("Enter your username to login: ")
entered_password = input("Enter your password to login: ")


try:
    if registered_username ==entered_username and registered_password == entered_password:
        print("Login  is successfull!")
    else:
        raise ValueError("Username or Password is incorrect. Please try again.")
except ValueError as e:
    print(e)

   
amount=0

amount=int(input("Enter amount of money: "))
#amount+=amount
print(f"Your amount is {amount}")
