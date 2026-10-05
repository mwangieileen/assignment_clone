#Dictionary of students with multiple objects 
students={
    "Student_1": {
    "Name": "Alice",
    "Age": 20 ,
    "DOB": "2003-01-15",
    "Location": "Nairobi",
    "ADM_No": 1100
    },
    "Student_2":{
        "Name": "Bob",
        "Age": 21,
        "DOB": "2002-05-20",
        "Location": "Mombasa",
        "ADM_No": 1101
    },
    "Student_3":{
        "Name": "Charlie",
        "Age": 22,
        "DOB": "2001-09-10",
        "Location": "Kisumu",
        "ADM_No": 1102
    },
    "Student_4":{
        "Name": "David",
        "Age": 23,
        "DOB": "2000-12-25",
        "Location": "Nakuru",
        "ADM_No": 1103
    },
    "Student_5":{
        "Name": "Eva",
        "Age": 24,
        "DOB": "1999-03-30",
        "Location": "Eldoret",
        "ADM_No": 1104
    }
}
print(students)

#Vertical printing of the dictionary as is
import pprint
pprint.pprint(students,sort_dicts=False)

#Normal printing of the dictionary- Horizontally
print(students["Student_1"])

#Vertically Print student_5 as is
pprint.pprint(students["Student_5"],sort_dicts=False)



