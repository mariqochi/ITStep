#Homework 13
#1. დაწერე ფუნქცია რომელიც მომხმარებელს ჩააწერინებს ტექსტურ ფაილში ინფორმაციას Input ფუნქციის დახმარებით, მანამ სანამ მომხმარებელი არ შეიყვანს სიტყვას _ “enough”.
with open ("second.txt", "w") as f:
    while True:
        answer=input("Enter Text: ")
        if answer.lower()=="enough":
            break
        f.write(f"{answer}\n")



#2. დაწერე ფუნქცია რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის ლოკაციას და შესაქმნელი ფაილის სახელს, 
#შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს და ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას.

import os

def create_file(folder_path, file_name):
    #file_path = folder_path + "/" + file_name --ვერ გავაერთიანე ამ მეთოდით, გამოვიყენე ჯოინი
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'w') as file:
        file.write("new line")

    return folder_path

def list_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    print(f"Files in {folder_path}: {files}")


folder_path_input = input("Enter your folder address: ")
file_name_input = input("Enter your file name: ")


folder_path = create_file(folder_path_input, file_name_input) 
list_files_in_folder(folder_path)
