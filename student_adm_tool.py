import csv
def write(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact Number","E-mail ID"])
        writer.writerow(info_list)
student_info_list=[]
condition=True
student_num=1
while(condition):
         student_info=input("Enter student information for student #{} in the following format(Name Age Contact_Number E-mail_ID):".format(student_num))
         student_info_list=student_info.split(' ')
         print("\nThe entered information is -\nName: {}\nAge: {}\nContact_Number: {}\nE-mail_ID: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
         ans=input("Is the enterde information correct?(yes/no): ")
         if ans=='yes':
             write(student_info_list)
             condition_check=input("Enter (yes/no) if you want to enter information for another student:")
             if condition_check=="yes":
                 condition =True
                 student_num+=1
             elif condition_check=="no":
                 condition=False
         elif ans=="no":
             print("\nPlease re-enter the values!")
