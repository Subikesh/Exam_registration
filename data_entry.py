from main.models import Student, Subject_attempts, Subject, Register
from django.contrib.auth.models import User
student = Student(user = User.objects.get(username='subikesh'), DOB = '2000-02-14', Gender = 'Male', Semester = 5)

subjects = [
    ['Physics', 'PH1234', 'CSE', 1, '2020-12-10', '350'], 
    ['Chemistry', 'CH1224', 'CSE', 1, '2020-12-12', '350'],
    ['Physics', 'PH1234', 'IT', 1, '2020-12-10', '350'],
    ['Chemistry', 'CH1224', 'IT', 1, '2020-12-12', '350'],
    ['Operating Systems', 'CS2234', 'CSE', 2, '2020-12-10', '350'],
    ['Database management system', 'CS2224', 'CSE', 2, '2020-12-12', '350'],
    ['Number Theory', 'MA2234', 'ECE', 2, '2020-12-10', '350'],
    ['Environmental Studies', 'CH2224', 'ECE', 2, '2020-12-12', '350'],
    ['Manufacturing technology', 'ME1234', 'Mech', 3, '2020-12-10', '350'],
    ['Fluid mechanics', 'ME3224', 'Mech', 3, '2020-12-12', '350'],
    ['Communication Engineering', 'EC3232', 'CSE', 3, '2020-12-15', '350'],
    ['Object Oriented Design and analysis', 'CS5832', 'CSE', 5, '2020-12-18', '350']
]

for subject in subjects:
    sub = Subject(Name= subject[0], Sub_code= subject[1], Department= subject[2], Semester= subject[3], DateofExam = subject[4], Fee= subject[5])
    sub.save()

users = [
    ['310618104102', 'sudharshan@gmail.com', '13dec2000', 'Sudharshanam', ''], ['2000-12-13', 'Male', 'CSE', 5],
    ['310618104130', 'abcd@gmail.com', '01jan2000', 'ABC', ''], ['2000-12-31', 'Female', 'CSE', 3],
]

for i in range(0, len(users), 2):
    user = User(username = users[i][0], password = users[i][2], email = users[i][1], first_name= users[i][3], last_name = users[i][4])
    user.save()
    stud = Student(user = user, DOB= users[i+1][0], Gender= users[i+1][1], Department= users[i+1][2], Semester = users[i+1][3])
    stud.save()
