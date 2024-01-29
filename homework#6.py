#task 1
#1. შექმენიფუნქცია, რომელიცმომხმარებლისგანმიღებულინფორმაციასგაასამმაგებსდადაბეჭდავსშემდეგნაირად: 
#input: “ablabdabdab”Output: „Tripled: ablabdabdabablabdabdabablabdabdab“

a=input("Enter information: ")
def tripled(a):
    result= a * 3
    #result=tripled(a)
    return result
result=tripled(a)
print(f"Tripled: {result}")


#task 2
#2. შექმენიფუნქცია, რომელიცმიიღებსმომხმარებლისწონასდადააბრუნებსმისწონასმთვარეზე. (მთვარისგრავიტაცია6_ჯერნაკლებიადედამიწისაზე)

def weightonthemoon(a):
    result = a / 6
    return result
a=int(input("Enter your weght: "))
print(f"your weigt is : {weightonthemoon(a)}")


#task3

#3. შექმენიკალკულატორისფუნქცია, რომელიცმიიღებსგამოსახულებასმომხმარებლისგანinput()ფუნქციისდახმარებით(სამმონაცემს_ პირველრიცხვს, მოქმედებას(+ -* / ^), მეორერიცხვს) მაგ. „2 * 6“.  ფუნქციადაშლისსტრიქონსsplit()ფუნქციისგამოყენებით. დათვლისდადააბრუნებსშედეგს. გაითვალისწინერომრიცხვისშეყვანისმაგიერსიმბოლოებისშეყვანისშემთხვევაშიუნდადააბრუნოსფუნქციამშესაბამისიმესიჯი. 
#ასევენულზეგაყოფაარშეიძ₾ება, ამშემთხვევაშიცუნდადააბრუნოსშესაბამისიმესიჯი. (დააბრუნოსდაარადაპრინტოს)


def calculation(a):
    while True:
        elements = a.split()

        if not elements[0].isdigit() or not elements[2].isdigit():
            print("Please input integer numbers.")
            a = input("Enter information: ")
            continue
        elif elements[1] == '/' and int(elements[2]) == 0:
            print("Dividing by zero is forbidden.")
            a = input("Enter information: ")
            continue
        elif elements[1] not in ('/', '*', '+', '-'):   #ეს პირობა დავამატე 
            print("Please enter one of the valid operators: '/', '*', '+', '-'")
            a = input("Enter information: ")
            continue
        else:
            num1 = int(elements[0])
            operator = elements[1]
            num2 = int(elements[2])
            break

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2

    print(f"Result: {result}")


calculated_numbers = input("Enter information: ")
calculation(calculated_numbers)