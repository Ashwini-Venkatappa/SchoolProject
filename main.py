import datetime
import re
import os
from pathlib import Path


def validate_name(name):
    """ Function to validate input names"""
    if name.isalpha():
        temp = name
    else:
        print("Invalid entry for name.\nName cannot contain special characters or numbers")
        temp = '$'
    return temp


class Name:
    """ Attributes :
    first_name
    last_name
    """
    def __init__(self):
        first_name = input("First name\t:")
        last_name = input("Last name\t:")
        self.first_name = validate_name(first_name)
        self.last_name = validate_name(last_name)


class Address:
    """Attributes:
    address_line
    city
    state
    zipcode"""
    def __init__(self):
        self.address_line = input("Address\t:")
        self.city = str(input("District\t:"))
        self.state = str(input("State\t:"))
        try:
            self.zipcode = int(input("Zipcode\t:"))
        except ValueError:
            print("Invalid zipcode")
            self.zipcode = '$'


class StudentInfo(Name, Address):

    def __init__(self):
        Name.__init__(self)
        Address.__init__(self)
        while True:
            try:
                date = input("Date of birth DD/MM/YYYY\t:")
                day, month, year = date.split('/')
                datetime.datetime(int(year), int(month), int(day))
                self.DOB = date
                break
            except ValueError:
                self.DOB = "$"
                print("Invalid entry for Date of birth.\nEnter date in the format DD/MM/YYYY\t:")

        sex = input("Sex M/F\t:")
        sex = sex.upper()
        if sex == 'M':
            self.sex = 0
        elif sex == 'F':
            self.sex = 1
        else:
            self.sex = "$"
            print("Invalid entry for sex")

        try:
            grade = int(input('Applying for grade 1/2/3\t:'))
            if grade < 1 or grade > 3:
                raise ValueError
        except ValueError:
            print("Invalid option.\n The number must be in the range of 1-3\t:")
        self.language = str(input("Primary speaking language English/kannada/Hindi/other\t:"))


class ParentInfo(Name, Address):
    def __init__(self):
        Name.__init__(self)
        Address.__init__(self)
        relationship = str(input("Relationship with the student:Mother/Father/Guardian\t:"))
        relationship = relationship.upper()
        if relationship == 'MOTHER':
            self.relationship = 0
        elif relationship == 'FATHER':
            self.relationship = 1
        elif relationship == 'Guardian':
            self.relationship = 2
        else:
            print("Invalid input")
            self.relationship = '$'
        email_id = input("Enter EmailId\t:")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email_id):
            self.email_id = email_id
        else:
            self.email_id = '$'
            print("Invalid Email")
        try:
            self.contact_number = int(input("Contact number\t:"))
        except ValueError:
            self.contact_number = '$'
            print("Invalid contact number\n")

        #Occupation info
        self.occupation = str(input("Occupation\t:"))
        self.company_name = str(input("Company Name\t:"))
        try:
            self.annual_income = int(input("Annual income number\t:"))
        except ValueError:
            self.annual_income = '$'
            print("Invalid annual income\t:\n")


class SiblingInfo(Name):
    def __init__(self):
        Name.__init__(self)
        try:
            self.age = int(input('Age\t:'))
            self.standard = int(input("class\t:"))
        except ValueError:
            self.age = "$"
            self.standard = "$"
            print("Invalid input")

try:
    print("Welcome. I am Ella. I will be assisting you with your admissions today. ")
    print("Press ESC to quite the application")
    working_dir = os.getcwd()
    file_folder = Path(working_dir)
    file_to_open = file_folder / "StudentData.txt"
    while True:
        print("Enter student information")
        student1 = StudentInfo()
        print("Enter Parent/Guardian Information")
        parent1 = ParentInfo()
        print("Sibling information is optional")
        sibling = SiblingInfo()
        student_Details = list(student1.__dict__.values())
        student_Details.extend(parent1.__dict__.values())
        student_Details.extend(sibling.__dict__.values())
        print(student_Details)
        student_Details_str = '|'.join(map(str, student_Details))
        try:
            if os.stat(file_to_open).st_size == 0:
                index = 1
            else:
                with open(file_to_open, "rb") as f:
                    # sets Reference point to last record
                    total_ele = (len(student_Details_str) + 2)
                    f.seek(-2, 2)
                    last_index = f.read(1)
                    #temp_list = list(temp.split("|"))
                    #last_index = int(temp_list[0])
                    index = int(last_index) + 1
        except FileNotFoundError:
            index = 1
            open(file_to_open, "w")

        student_Details_str = student_Details_str+"|"+str(index)+"\n"
        with open(file_to_open, "a") as f:
            f.writelines(student_Details_str)

except KeyboardInterrupt:
    print("Thank you")

