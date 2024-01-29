#task1
#მომხმარებელსშემოაყვანინეინფორმაციადადათვალერამდენირიცხვი, ანბანისასოდასხვასიმბოლოამოცემულიწინადადებაში. შედეგიდაბეჭდე.გამოიყენეforციკლი, isalphaდაisdigitფუნქციები. 
import re
count=0
count2=0
count3=0
a=input("enter: ")
for symbol in a:
    print(symbol)
    if symbol.isalpha()==True: 
        count=count+1
    elif symbol.isdigit()==True:
        count2=count2+1
    else:
        count3=count3+1
print(count)
print(count2)
print(count3)

#task 2
#2.მომხმარებელსშეაყვანინეორიწინადადებადამათგანშეადგინემესამეშემდეგწესებზედაყრდნობით. შექმნილიწინადადებაუნდაიწყებოდესპირველიწინადადებისპირველისიმბოლოთი, რომელსაცჯერმოჰყვებამეორეწინადადებისბოლოსიმბოლო, შემდეგკიპირველიწინადადებისმეორესიმბოლოდამეორეწინადადებისბოლოდანმეორესიმბოლო.
a=input("Enter first sentence: ")
b=input("Enter second sentence: ")
print (a[0], b[-1],a[1], b[-2])



#task 3
#მომხმარებელსშეაყვანინეორიწინადადებადაშეამოწმე, პირველწინადადებაშიარსებულიყველასიმბოლოთუშედისმეორეწინადადებაშიდაპირიქით, მეორეწინადადებაშიშემავალიყველასიმბოლოთუშედისპირველწინადადებაში. თუესორიპირობადაკმაყოფილდა, დაბეჭდე:„Strings are balanced!“თურომელიმეპირობადაირღვა, დაბეჭდე:„Strings are not balanced!“

a=input("Enter first sentence: ")
b=input("Enter second sentence: ")
for i in a:
    if i in b:
        a=b
    else:
        a!=b
if a==b:
    print ("Strings are balanced!")
else:
    ("Strings are not balanced!")
