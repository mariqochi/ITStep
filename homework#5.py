#task1
#ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია საკუთარისახელის, გვარისდაასაკისშესახებ. თითოეულიმომხმარებლისინფორმაციაშეინახეინდივიდუალურსიაში. 
#შემდეგკისამივესიადაამატესაერთოცალრიელსიასსახელადconsumer_info. 
#Input_ისმეშვეობითმომხმარებლისინდექსისშეყვანისშემთხვევაშიპროგრამამუნდადაბრუნოსარჩეულმომხმარებელზეინფორმაციაშემდეგნაირად: Name: EleneLastname: Khardava

data=[]
consumer_info=[]
a=0
while a<3:
    firstname=input("Enter your firsname: ")
    lastname=input("Enter your lastname: ")
    age=input("Enter your age: ")
    data=[firstname, lastname, age]
    #print(data)
    
    consumer_info.append(data)
    a=a+1
    
#print(consumer_info)
n=int(input("Enter number of consumer: "))
print(f"Name: {consumer_info[n-1][0]}")
print(f"LastName: {consumer_info[n-1][1]}")
print(f"Age: {consumer_info[n-1][2]}")

#task2
#მომხმარებელიდაარეგისტრირეონლაინპლატფორმაზეთუსახელისველიარიქნებაცარიელი, ხოლოპაროლი8 სიმბოლოზემეტიანტოლია. 
#მისიმონაცემებიშეინახელისთში. შემდეგმიეცისაშუალებასცადოსპლატფორმაზეშესვლადაშეადარემისმიერშემოყვანილიინფორმაციასიაშიშენახულინფორმაციას. 
#დაბეჭდეშესაბამისიმესიჯი.

registered_users = []
while True:
    name = input("Enter your name to  register: ")
    password = input("Enter your password to  register: ")
    user=[name, password]
    
    if len(name) > 0 and len(password) > 7:
        registered_users.append(user)
        print("You have registered successfully!")
   
        break
    else:
        print("Name should have length greater than 0 and password length should be greater than 7")
        continue

while True:
    name = input("Enter your name to log in: ")
    password = input("Enter your password to log in: ")
    user=[name, password]
    #print (user)
  
    if user  in registered_users:
        print("Login successful!")
        break
    else:
        print("Invalid name or password. Please try again.")
        break


#task3
#შექმენიჩაშენებულისია, რომელშიციქნებაშენახულიცნობილიმსახიობებისშესახებინფორმაცია.
# მომხმარებელსშემოჰყავსმსახიობისსახელიანგვარი. თუსიაშიმოიძებნამსახიობი, დაბეჭდამისშესახებარსებულიინფორმაციარეზუმისსახით.
    


info = [
    ["Ben", "Affleck", 50],
    ["Jennifer", "Lopez", 47],
    ["Penelope", "Kruz", 46]
]
#print(info)

answer = input("Enter the last name: ")
found = False

for person in info:
    if answer.lower() == person[1].lower():
        print(f"First Name: {person[0]}, Last Name: {person[1]}, Age: {person[2]}")
        found = True
        break

if not found:
    print("This person is not in the list")