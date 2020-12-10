from main.models import Student, Subject_attempts, Subject, Register
from django.contrib.auth.models import User

subjects = [
    ['Engineering Physics 1', 'PH8151', 'CSE', 1, '2020-12-10', '350'], 
    ['Engineering Chemistry 1', 'CH8151', 'CSE', 1, '2020-12-12', '350'],
    ['Problem Solving Using Python', 'CS8151', 'CSE', 1, '2020-12-14', '350'],

    ['Engineering Physics 2', 'PH8251', 'CSE', 2, '2020-12-10', '350'],
    ['Engineering Chemistry 2', 'CH8251', 'CSE', 2, '2020-12-12', '350'],
    ['Programming In C', 'CS8251', 'CSE', 2, '2020-12-14', '350'],

    ['Object Oriented Programming', 'CS8351', 'CSE', 3, '2020-12-10', '350'],
    ['Data Structures', 'CS8352', 'CSE', 3, '2020-12-12', '350'],
    ['Communication Engineering', 'EC8356', 'CSE', 3, '2020-12-14', '350'],

    ['Operating Systems', 'CS8451', 'CSE', 4, '2020-12-10', '350'],
    ['Computer Architecture', 'CS8452', 'CSE', 4, '2020-12-12', '350'],
    ['Software Engineering', 'CS8453', 'CSE', 4, '2020-12-14', '350'],

    ['Object Oriented Analysis and Design', 'CS8551', 'CSE', 5, '2020-12-10', '350'],
    ['Theory Of Computation', 'CS8552', 'CSE', 5, '2020-12-12', '350'],
    ['Computer Networks', 'CS8553', 'CSE', 5, '2020-12-14', '350'],

    ['Mobile Computing', 'CS8651', 'CSE', 6, '2020-12-10', '350'],
    ['Internet Programming', 'CS8652', 'CSE', 6, '2020-12-12', '350'],
    ['Distributed Systems', 'CS8653', 'CSE', 6, '2020-12-14', '350'],

    ['Cryptography and Network Security', 'CS8751', 'CSE', 7, '2020-12-10', '350'],
    ['Cloud Comouting', 'CS8752', 'CSE', 7, '2020-12-12', '350'],
    ['Principles Of Management', 'MG8753', 'CSE', 7, '2020-12-14', '350'],

    ['Fundamentals Of Nano Science', 'GE8851', 'CSE', 8, '2020-12-10', '350'],
    ['Speech Processing', 'CS8852', 'CSE', 8, '2020-12-12', '350'],

    ['Engineering Physics 1', 'PH8151', 'IT', 1, '2020-12-10', '350'],
    ['Engineering Chemistry 1', 'CH8151', 'IT', 1, '2020-12-12', '350'],
    ['Problem Solving Using Python', 'CS8151', 'IT', 1, '2020-12-14', '350'],


    ['Engineering Physics 2', 'PH8251', 'IT', 2, '2020-12-10', '350'],
    ['Engineering Chemistry 2', 'CH8251', 'IT', 2, '2020-12-12', '350'],
    ['Programming In C', 'CS8251', 'IT', 2, '2020-12-14', '350'],

    ['Discrete Mathematics', 'MA8351', 'IT', 3, '2020-12-10', '350'],
    ['Data Structures', 'CS8352', 'IT', 3, '2020-12-12', '350'],
    ['Communication Engineering', 'EC8356', 'IT', 3, '2020-12-14', '350'],

    ['Probability and Statistics', 'MA8451', 'IT', 4, '2020-12-10', '350'],
    ['Computer Architecture', 'CS8452', 'IT', 4, '2020-12-12', '350'],
    ['Environmental Engineering', 'GE8453', 'IT', 4, '2020-12-14', '350'],

    ['Web Technology', 'IT8551', 'IT', 5, '2020-12-10', '350'],
    ['Algebra and Number Theory', 'MA8552', 'IT', 5, '2020-12-12', '350'],
    ['Computer Networks', 'CS8553', 'IT', 5, '2020-12-14', '350'],

    ['Computational Intelligence', 'IT8651', 'IT', 6, '2020-12-10', '350'],
    ['Internet Programming', 'CS8652', 'IT', 6, '2020-12-12', '350'],
    ['Mobile Communication', 'IT8653', 'IT', 6, '2020-12-14', '350'],

    ['Cryptography and Network Security', 'CS8751', 'IT', 7, '2020-12-10', '350'],
    ['Cloud Comouting', 'CS8752', 'IT', 7, '2020-12-12', '350'],
    ['Principles Of Management', 'MG8753', 'IT', 7, '2020-12-14', '350'],

    ['Fundamentals Of Nano Science', 'GE8851', 'CSE', 8, '2020-12-10', '350'],
    ['Electronic Commerce', 'IT8852', 'CSE', 8, '2020-12-12', '350'],

    ['Engineering Physics 1', 'PH8151', 'Mech', 1, '2020-12-10', '350'], 
    ['Engineering Chemistry 1', 'CH8151', 'Mech', 1, '2020-12-12', '350'],
    ['Problem Solving Using Python', 'CS8151', 'Mech', 1, '2020-12-14', '350'],

    ['Materials Science', 'PH8253', 'Mech', 2, '2020-12-10', '350'],
    ['Engineering Mathematics 2', 'MA8251', 'Mech', 2, '2020-12-12', '350'],
    ['Engineering Mechanics', 'GE8251', 'Mech', 2, '2020-12-14', '350'],

    ['Manufacturing Technology 1', 'ME8351', 'Mech', 3, '2020-12-10', '350'],
    ['Fluid Mechanics', 'ME8352', 'Mech', 3, '2020-12-12', '350'],
    ['Engineering Thermodynamics', 'ME8356', 'Mech', 3, '2020-12-14', '350'],

    ['Manufacturing Technology 2', 'ME8451', 'Mech', 4, '2020-12-10', '350'],
    ['Engineering Metullurgy', 'ME8452', 'Mech', 4, '2020-12-12', '350'],
    ['Thermal Engineering', 'ME8453', 'Mech', 4, '2020-12-14', '350'],

    ['Object Oriented Analysis and Design', 'CS8551', 'CSE', 5, '2020-12-10', '350'],
    ['Theory Of Computation', 'CS8552', 'CSE', 5, '2020-12-12', '350'],
    ['Computer Networks', 'CS8553', 'CSE', 5, '2020-12-14', '350'],

    ['Thermal Engineering 2', 'ME8651', 'Mech', 6, '2020-12-10', '350'],
    ['Dynamics and Machines', 'ME8652', 'Mech', 6, '2020-12-12', '350'],
    ['Design of Machine Elements', 'ME8653', 'Mech', 6, '2020-12-14', '350'],

    ['Mechatronics', 'ME8751', 'Mech', 7, '2020-12-10', '350'],
    ['Power Plant Engineering', 'ME8752', 'Mech', 7, '2020-12-12', '350'],
    ['Process and Plan Cost Estimation', 'ME8753', 'Mech', 7, '2020-12-14', '350'],

    ['Fundamentals Of Nano Science', 'GE8851', 'Mech', 8, '2020-12-10', '350'],
    ['Vibration and Noise Control', 'ME8852', 'Mech', 8, '2020-12-12', '350'],

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
