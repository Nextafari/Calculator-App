import random
import xlwt

#This is a class that returns the name, gender, age, state, and account balance of data inside it.
class human_data(object):
    def __init__(self, name, gender, age, state, account_balance):
        self.name = name
        self.gender = gender
        self.age = age
        self.state = state 
        self.account_balance = account_balance

name = ["Sara Lamb",
    "Ed Smith",
    "Derrick Owen",
    "Fredrick Sanchez",
    "May Buchanan",
    "Alexandra Porter",
    "Willie Carroll",
    "Ora Hayes",
    "Laverne Love",
    "Terrell Caldwell",
    "Silvia Morris",
    "Eduardo Lawson",
    "Terrence Goodman",
    "Sabrina Reynolds",
    "Johnathan Murray",
    "Alison Santos",
    "John Baldwin",
    "Alice Ramsey",
    "Rene Wilkerson",
    "Raymond Burgess",
    "Guadalupe Herrera",
    "Leona Delgado",
    "Marty Alvarado",
    "Bridget Stevenson",
    "Nadine Rogers",
    "Brent Morales",
    "Vincent Tate",
    "Darnell Morgan",
    "Robert Garrett",
    "Robin Floyd",
    "Carlos Oliver",
    "Allen Ortiz",
    "Earnest Reid",
    "Dwight Romero",
    "Heidi Newton",
    "Angel Munoz",
    "Verna Holland",
    "Alfonso Gilbert",
    "Randy Mcbride",
    "Enrique Rhodes",
    "Kelly Ellis",
    "Pam Parker",
    "Faith Wagner",
    "Saul Joseph",
    "Terry Padilla",
    "Grady Fernandez",
    "Jay Rivera",
    "Maria Walker",
    "Loren Figueroa",
    "Teresa Rodgers",
    "Reginald Brooks",
    "Elsie Weaver",
    "Dianne Clark",
    "Celia Webster",
    "Misty Peterson",
    "Gerald Bowen",
    "Clark Gross",
    "Gregg Keller",
    "Barbara Jensen",
    "Rafael Harrington",
    "Roberto Simon",
    "Sidney Bell",
    "Allison Davis",
    "Alexander Patterson",
    "Donald Meyer",
    "Irving Welch",
    "Bruce Moreno",
    "Marjorie Ramos",
    "Samuel Drake",
    "Mario Dixon",
    "Charlie Myers",
    "Suzanne Fields",
    "Ivan Roberson",
    "Salvador Wolfe",
    "Curtis Conner",
    "Austin Hughes",
    "Spencer Long",
    "Tyler Stone",
    "Irene Goodwin",
    "Guadalupe Cobb",
    "Marguerite Cross",
    "Jacqueline Gonzalez",
    "Lauren Cox",
    "Paula Reed",
    "Wayne Ortega",
    "Jim Harris",
    "Ashley Houston",
    "Dallas Huff",
    "Georgia Harper",
    "Della Vargas",
    "Amanda Warren",
    "Jimmy Greene",
    "Deborah Dunn",
    "Rita Ferguson",
    "Doug Haynes",
    "Betsy Bush",
    "Jody Jennings",
    "Kristin Bennett",
    "Ebony Roberts",
    "Dale Hanson"]

gender = ["male", "Female"]
age =  range(18, 50)
state = ["Lagos", "Ebonyi", "Ekiti", "Anambra", "Oyo", "Kaduna", "Abia", "Ondo", "Rivers", "Kogi", "Bayelsa", "Borno"]
account_balance = range(10000, 150000)



#for i in range(50):
#	carmen = human_data(name = random.choice(name), gender = random.choice(gender), age = random.choice(age), state = random.choice(state), account_balance = random.choice(account_balance))
#	print(carmen.name, carmen.gender, carmen.gender, carmen.age, carmen.state, carmen.account_balance)



account_balance_1 = [60672, 141186,  43783,  58940, 145279,  44012, 104968, 137770,  92175, 127007,  19360, 140173,  45729,  44644,  86793, 135121, 126298, 131831,  47335,  98915, 125707,  78197,  52719,  80207, 118783, 121661,  86251,  74374,  29683,  83515, 109823, 139515,  39745,  72436, 133825,  50611,  73827, 102668,  45501,  23625, 119861,  21288, 117099, 122686,  19600,  34601,  27711,  36032, 110593,  69942]

state_1 = [ "Lagos",
   "Ondo",
    "Oyo",
 "Borno ",
"Anambra",
"Anambra ",
"Kaduna ",
  "Lagos",
"Anambra ",
    "Oyo",
"Ebonyi ",
   "Abia",
  "Lagos",
  "Borno",
   "Oyo ",
"Eakiti ",
"baonyi ",
"Bayelsa",
 "Ebonyi",
 "Ekiti ",
 "Rivers",
   "Kogi",
"Anambra",
   "Oyo ",
  "Kogi ",
"Bayelsa",
"Anambra",
   "Ondo",
   "Abia",
 "Ekiti ",
"Anambra ",
  "Ekiti",
   "Abia",
  "Kogi ",
  "Lagos",
 "Ebonyi",
"Anambra ",
   "kogi",
   "Abia",
 "Borno ",
   "Kogi",
  "Kogi ",
  "Ondo ",
  "Lagos",
 "Ebonyi",
  "Ekiti",
   "Abia",
 "Lagos ",
  "Ekiti",

]

name_12 = ["Ed Smith", "Guadalupe Cobb", "Verna Holland", "Saul Joseph", "Heidi Newton", "Silvia Morris", "Rafael Harrington",
"Suzanne Fields", "Della Vargas", "John Baldwin", "Tyler Stone", "Salvador Wolfe", "Deborah Dunn", "Sabrina Reynolds", "Paula Reed",
"Jacqueline Gonzal",
"Paula Reed",
"Eduardo Lawson",
"Jay Rivera",
"Mario Dixon",
"Elsie Weaver",
"Roberto Simon",
"Alison Santos",
"Della Vargas",
"Doug Haynes",
"Samuel Drake",
"Jimmy Greene",
"Carlos Oliver",
"Rene Wilkerson",
"Alison Santos",
"Dale Hanson",
"Alison Santos",
"Clark Gross",
"Willie Carroll",
"Doug Haynes",
"Wayne Ortega",
"Enrique Rhodes",
"Allison Davis",
"Donald Meyer",
"Misty Peterson",
"Samuel Drake",
"Dale Hanson",
"Rafael Harrington",
"Allen Ortiz",
"Sara Lamb",
"Allison Davis",
"Dianne Clark",
"Laverne Love",
"Bridget Stevenson",
"Willie Carroll",
]

gender_1 = ["Female", "Female", "male  ", "male  ", "Female", "male  ", "Female", "Female", "male  ", "Female", "male  ", "Female", "Female",
"Female", "male  ", "Female", "male  ", "male  ", "Female", "male  ", "Female", "Female", "Female", "Female", "male  ", "Female", "male  ",
"Female", "Female", "male  ", "Female", "male  ", "Female", "male  ", "Female", "Female", "male", "male", "male", "Female", "Female",
"male", "Female", "Female", "Female", "Female", "Female", "male", "male "]




age_1 = [23, 34, 44, 33, 25, 23, 41, 21, 19, 47, 49, 22, 30, 43, 46, 46, 30, 45, 18, 20, 44, 47,28, 27, 40, 20, 40, 31, 29,24,
28, 33, 40, 27, 30, 46, 31, 27, 46, 24, 31, 41, 43, 22, 44, 19, 36, 27]

#A varible book was created to initialize the xlwt workbook and store the value in the variable, book
book = xlwt.Workbook()
#Another variabe was created to creat and name a sheet 
sheet = book.add_sheet("Employee data")

#Here the sheet created above were being written into it taking the row and colum into consideration while doing this
#In the first sheet here, we are referencing row1, column1 in excel and naming the column "Name".
# This was done for the other sheets as well; taking the rows and columns into consideration
sheet.write(0, 0, "Name")
sheet.write(0, 1, "Gender")
sheet.write(0, 2, "Age")
sheet.write(0, 3, "State")
sheet.write(0, 4, "Account Balance")



#A for loop is used here to write into the sheet, we also used the enumerate function to enumerate(number) the items 
# that are being written into the work book. using the enumerate function mandates that we call both the index(position)
# and the value of what we intend to loop. we can also name these variables (index and value) anything that appeals to us.
for index, value in enumerate(name_12):
   sheet.write(index+1, 0, value)

for index, value in enumerate(gender_1):
   sheet.write(index+1, 1, value)

for index, value in enumerate(age_1):
    sheet.write(index+1, 2, value)

for index, value in enumerate(state_1):
    sheet.write(index+1, 3, value)

for index, value in enumerate(account_balance_1):
    sheet.write(index+1, 4, value)


#We use a variable to hold the name that we want to call the workbook, and we go ahead to call the .save function on the 
#book variable that we created in line 232 to save the work book and pass the name variable holding the workbook's name
#created on line 269 below as an argument to the book.save(xyz) function
name_2 = "Employee data.xls"
book.save(name_2)




