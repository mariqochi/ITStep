#homework2
#task1




# 1. ვიქტორინაშეადგინევიქტორინისპროგრამა. მომხმარებელსუნდადავუსვათკითხვა: 
# “რომელიიმპერიისმიერაგებულიწყალ-მომარაგებისსისტემა(აკვედუკი) ფუნქციონირებსდღესაც?
# ”სავარაუდოპასუხები: 1.შუმერთა2.სელჩუკთა3.რომის4.მონღოლთამომხმარებელმაუნდაშეიყვანოსსწორიპასუხისნომერიანთავადსწორიპასუხი. 
# შეცდომისშემთხვევაშიიბეჭდება: „არა! სწორიპასუხიარომის!“სწორიპასუხისშემთხვევაშიიბეჭდება: „სწორია!“


print ("რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (ავედუკი) ფუნქციონირებს დღესაც?", '\n', "სავარაუდო პასუხები:",'\n',  "1.შუმერთა",'\n', "2.სელჩუკთა",'\n', "3.რომის",'\n', "4.მონღოლთა",'\n')
a=input( )
if a=="რომის" or a=="3":
    print("სწორია!")
else:
    print ("არა! სწორი პასუხია რომის")



#task 2
# 2. ონლაინმაღაზიაპროგრამაგთავაზობსპროდუქტისსამკატეგორიას. მაგ.1.ლეპტოპები2.პერსონალურიკომპიუტერები
# 3.მობილურებიმომხმარებელიირჩევსერთ-ერთს.პროგრამაითხოვსმაქსიმალურბიუჯეტსდაბიუჯეტისმიხედვითსთავაზობსმომხმარებელსკონკრეტულმოდელსარჩეულკატეგორიაში. 
# (თითოკატეგორიაშიმინიმუმ3 პროდუქტიმაინცუნდაიყოს)თუბიუჯეტიძალიანმცირეა, პროგრამაბეჭდავს, რომამთანხაშიარგააჩნიაშემოთავაზება.


print ("აირჩიეთ სასაურველი კატეგორია:", '\n',  "1.ლეპტოპები",'\n', "2.პერსონალური_კომპიუტერები",'\n', "3.მობილურები",'\n')
a="ლეპტოპები"
b="პერსონალური_კომპიუტერები"
c="მობილურები"
e=input ()

budjet=int(input("შეიყვანე შენი ბიუჯეტი: "))


if e==a:
    if 650<=budjet <= 1000:
            print ("Lenovo")
    elif 1000<budjet<=2000:
       print ("Asus")
    elif budjet>2000:
       print ("Apple")
    else:
        print ("აღნიშნულ თანხაში თქვენს მიერ არჩეულ კატეგორიაში შემოთავაზებები არ გაგვაჩნია :(")
    
elif e==b:
    if 600<=budjet <= 900:
       print ("Dell")
    elif 900<budjet<=1500:
        print ("Acer")
    elif budjet>1500:
        print ("HP")
    else:
        print ("აღნიშნულ თანხაში თქვენს მიერ არჩეულ კატეგორიაში შემოთავაზებები არ გაგვაჩნია :(")
else:
    if 300<=budjet <= 800:
        print ("Xiaomi")
    elif e==c and 500<budjet<=1800:
        print ("Samsung")
    elif budjet>1800:
        print ("Iphone")
    else:
        print ("აღნიშნულ თანხაში თქვენს მიერ არჩეულ კატეგორიაში შემოთავაზებები არ გაგვაჩნია :(")


#task #3 ბოლო ვერსიებზე შემცირებული მაქვს ვარიანტების რაოდენობა, რადგან ძალიან გაიწელა:)
# 3. ქუესთის შედგენა (Text Based Adventure Game)
# დაწერე ერთმანეთში ჩასმული if-else კონსტრუქციების
# გამოყენებით მარტივი ტექსტზე დაფუძნებული სათავგადასავლო თამაში.
# მაგ. თავიდან პროგრამა ბეჭდავს მომხმარებლის ადგილსამყოფელს და სთავაზობს მქომედების რამდენიმე ვარიანტს. სხვადასხვა არჩევანის შემთხვევაში თამაშ სხვადასხვანაირად ვითარდება.
print ("თქვენ იმყოფებით ათენში  და უნდა ჩახვიდეთ პარიზში უმოკლეს დროში  რომ აიღოთ პრიზი, თამაშს მოიგებს მონაწილე ვისაც ბილეთში დაუფიქსირდება უახლესი თარიღი და დრო, პირველ რიგში აირჩიეთ ტრანსპორტის სახეობა:", '\n',  "1.თვითმფრინავი",'\n', "2.მატარებელი",'\n', "3.გემი",'\n')
a="თვითმფრინავი"
b="მატარებელი"
c="გემი"

am="პირდაპირი რეისი"
al="ორი გადაჯდომა"
an="ორზე მეტი გადაჯდომა"
km="პირველი კლასი"
kl="ბიზნეს კლასი"
kn="პრემიუმ კლასი" 
ko="პირველი კლასი ორივე რეისი"
ki="ბიზნეს კლასი და პირველი კლასი"
ka="პრემიუმ კლასი და ბიზნეს კლასი"
kb="პირველი კლასი ყველა რეისი"
kq="ბიზნეს კლასი ყველა რეისი"
kj="პრემიუმ კლასი ყველა რეისი"

e=input ()



if e==a:
    print ("აირჩიეთ:",'\n', "პირდაპირი რეისი",'\n',"ორი გადაჯდომა",'\n',"ორზე მეტი გადაჯდომა",'\n')
    t=input()
    if t==am:
        print ("აირჩიეთ:",'\n', "პირველი კლასი",'\n',"ბიზნეს კლასი",'\n',"პრემიუმ კლასი",'\n')
        k=input()
        if k==kl:
            print ("ბილეთები არ არის, თამაში დასრულდა")
        elif k==kn:
            print ("თამაშის ბიუჯეტი არ არის საკმარისი ბილეთის შესაძენად, თქვენ გჭირდებათ დამატებითი დრო, რომ გამოიმუშავოთ საკმარისი თანხა")
        else:
            print ("თქვენ შეიძინეთ ბილეთი, ჩაფრენის დრო არის 02.12.2023:18:00")
    elif t==al:
        print ("აირჩიეთ:",'\n', "პირველი კლასი ორივე რეისი",'\n',"ბიზნეს კლასი და პირველი კლასი",'\n',"პრემიუმ კლასი და ბიზნეს კლასი",'\n')
        k2=input()
       
        if k2==ko:
                print ("ბილეთები  არის,  ჩაფრენის დრო : 04.12.2023:18:00")
        elif k2==ki:
                print ("ბილეთები  არის,  ჩაფრენის დრო : 03.12.2023:18:00")
        else:
                print ("ბილეთები არ არის")
    else:
        print ("აირჩიეთ:",'\n', "პირველი კლასი ყველა რეისი",'\n',"ბიზნეს კლასი ყველა რეისი",'\n',"პრემიუმ კლასი ყველა რეისი",'\n')
        k3=input()
        if k3==kb:
             print ("ბილეთები  არ არის თქვენ დაასრულეთ თამაში")
        elif k3==kq:
             print ("ბილეთები  არის, ჩაფრენის დრო: 02.12.2023:17:30")
        else:
             print ("ბილეთები  არის, ჩაფრენის დრო: 02.12.2023:21:30")
elif e==b:
    print ("აირჩიეთ:",'\n', "პირდაპირი რეისი",'\n',"ორი გადაჯდომა",'\n',"ორზე მეტი გადაჯდომა",'\n')
    t=input()
    if t==am:
        print ("აირჩიეთ:",'\n', "პირველი კლასი",'\n',"ბიზნეს კლასი",'\n',"პრემიუმ კლასი",'\n')
        k=input()
        if k==kl:
            print ("ბილეთები არის, ჩასვლის დრო: 02.12.2023:22:04")
        elif k==kn:
            print ("ბილეთები არის, ჩასვლის დრო: 02.12.2023:16:04, გილოცავთ თქვენ მოიგეთ თამაში, რადგან ჩახვალთ პირველი")
        else:
            print ("თქვენ შეიძინეთ ბილეთი, ჩაფრენის დრო არის 02.12.2023:18:00")   
    elif t==al:
         print ("ორი გადაჯდომის არჩევის შემთხვევაში დარჩენილი არის მხოლოდ ბიზნეს კლასის ბილეთები, ჩასვლის დრო  02.12.2023:14:00:()")
    else:
         print ("ორი გადაჯდომის არჩევის შემთხვევაში დარჩენილი არის მხოლოდ პრემიუმ კლასის ბილეთები, ჩასვლის დრო  02.12.2023:12:00:()")
else:
     print ("გემი დადის კვირაში ერთხელ, უხლოეს მგზავრობაზე დარჩენილია მხოლოდ პრემიუიმ კლასის ბილეთები, ჩასვლის დრო:  02.12.2023:22:00:()")