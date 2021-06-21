#Project 1: Basic School administration tool
import csv
def write_into_csv(info_list):
    with open("My_captain.csv","a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "phone_Number", "Email_Id"])
        writer.writerow(info_list)
condition = True
while(condition):
    student_info = input("enter student information in the following format name age phone_number email:")
    print("Entered information:"+ student_info)
    student_info_list = student_info.split(' ')
    print("Entered split up information is:"+ str(student_info_list))
    print("\nThe entered information is -\nName: {}\nAge: {}\nphone_Number:{}\nEmail_Id:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    write_into_csv(student_info_list)

    condition_check = input("enter (Yes/No) if you want to enter the further student details:")
    if condition_check == "Yes":
        condition = True
    elif condition_check == "No":
        condition = False
















