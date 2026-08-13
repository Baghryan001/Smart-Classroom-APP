# Ex_1 : Ստեղծել variables տարբեր data type-երով եւ տպել դրանց արժեքներն ու type-երը
# `type()` ֆունկցիայով։

# a = 11
# b = 4.44
# name = "Artavazd"
# is_adult = False
# result = None
# data = b"World"
#
# print(a,type(a))
# print(b,type(b))
# print(is_adult,type(is_adult))
# print(result,type(result))
# print(data,type(data))



# Ex_2 : User-ից վերցնել մեկ թիվ եւ տպել այդ թվի քառակուսին ու խորանարդը։

# x = int(input("Enter number: "))
#
# print("Square: ",pow(x , 2))
# print("Cube: ",pow(x , 3))



# Ex_3 : User-ից վերցնել Celsius ջերմաստիճան եւ փոխարկել Fahrenheit-ի։

# celsius = float(input("Enter Celsius: " ))
# fahrenheit = celsius * 1.8 + 32
# print("Fahrenheit : ",fahrenheit)



# Ex_4 : User-ից վերցնել name, age, city եւ profession։

# name =input("Enter your name: ")
# age = input("Enter your age: ")
# city = input("Enter your city: ")
# profession = input("Enter your profession: ")
#
# print(F"My name is {name}. I am {age} years old. I live in {city} and I work as {profession}.")



# Ex_5 : User-ից վերցնել թիվ եւ որոշել՝ այն զույգ է, թե կենտ։

# number = int(input("Enter number: "))
#
# if number % 2 == 0 :
#     print("The number is even")
#
# else :
#     print("The number is odd")



# Ex_6 : User-ից վերցնել age եւ որոշել cinema ticket-ի գինը։

# age = int(input("Enter your age: "))
#
# if age < 7 :
#     ticket = 0
#
# elif   age <= 17 :
#      ticket = 1000
#
# elif   age <=64 :
#     ticket = 2000
#
# else :
#     ticket = 1200
#
#
# print(f"The ticket costs {ticket} drams")



# Ex_7 : User-ից վերցնել product price եւ discount percent, հետո հաշվել final price-ը։

# product_price = int(input("Enter Product price:"))
# discount_percent = int(input("Enter Discount persent: "))
#
# if discount_percent < 0 or discount_percent > 100 :
#     print("Discount is wrong")
#
# else :
#     final_price = product_price - product_price * discount_percent * 0.01
#     print("Final price: ", final_price)



# Ex_8 : User-ից վերցնել weight եւ height, հաշվել BMI-ն եւ տպել BMI category։

# weight = float(input("Enter your weight:"))
# height = float(input("Enter your height: "))
#
#
# if weight <= 0:
#     print("Height is wrong")
#
# else :
#     BMI = weight / pow(height, 2)
#
#     if BMI < 18.5:
#         print("Category: Underweight")
#
#     elif BMI <= 24.9:
#         print("Category: Normal")
#
#     elif BMI <= 29.9:
#         print("Category: Overweight")
#
#     else:
#         print("Category: Obese։")


# Ex_9 : User-ից վերցնել password եւ գնահատել դրա ուժեղությունը՝ ըստ երկարության։

# password = input("Enter your password:")
# len_P = len(password)
#
# if len_P < 6 :
#     print("THe password is weak")
# elif len_P < 10 :
#     print("The password is medium")
# else :
#     print("The password is strong")


# Ex_10 : User-ից վերցնել թիվ եւ որոշել՝ այն դրական է, բացասական, թե զրո։

# number = float(input("Enter number: "))
#
# if number > 0 :
#     print("Number is positive")
# elif number < 0 :
#     print("Number is negative")
# else :
#     print("The number is 0")


# Ex_11 : User-ից վերցնել երկու թիվ եւ որոշել՝ որն է մեծ։

# number_1 = float(input("Enter first number:"))
# number_2 = float(input("Enter second number: "))
#
# if number_1 > number_2 :
#     print(" first number is greater")
# elif number_1 < number_2 :
#     print("second number is greater")
# else :
#     print(" numbers are equal")


# Ex_13 : User-ից վերցնել salary եւ հաշվել tax amount-ն ու net salary-ն։

# salary = int(input("Enter your salary:"))
# if salary <= 0 :
#     print("The salary is wrong")
# else :
#     if salary <= 150000 :
#       print(f"Gross salary - {salary}   Tax amount - 0   Net salary - {salary}")
#
#     elif salary <= 500000 :
#       tax = salary * 0.1
#       net = salary - tax
#       print(f"Gross salary - {salary}   Tax amount - {tax}   Net salary = {net}")
#
#     elif salary <= 1000000 :
#       tax = salary * 0.2
#       net = salary - tax
#       print(f"Gross salary - {salary}   Tax amount - {tax}   Net salary = {net}")
#
#     else :
#       tax = salary * 0.25
#       net = salary - tax
#       print(f"Gross salary - {salary}   Tax amount - {tax}   Net salary = {net}")



# Ex_12 : User-ից վերցնել առաջին թիվը, operator-ը եւ երկրորդ թիվը։

# number_1 = float(input("Enter first number: "))
# operator = input("Enter operator(+,-,*,/,%,//): ")
# number_2 = float(input("Enter second number: "))
#
# if number_2 == 0 :
#     print("Cannot divide by 0")
# elif operator == "+" :
#     print(number_1 + number_2)
# elif operator == "-" :
#     print(number_1 - number_2)
# elif operator == "*" :
#     print(number_1 * number_2)
# elif operator == "/" :
#     print(number_1 / number_2)
# elif operator == "//" :
#     print(number_1 // number_2)
# elif operator == "%" :
#     print(number_1 % number_2)
# else :
#     print("Wrong operator")



# Ex_14 : User-ից վերցնել value եւ target type, հետո convert անել value-ը ընտրված type-ի։

# value = input("Enter value: ")
# target_type = input("Enter target type(int,float,str,bytes): ")
#
# if target_type == "int" :
#     result = int(value)
#     print("Converted value: ", result)
#     print("Type: ", type(result))
# elif target_type == "float" :
#     result = float(value)
#     print("Converted value: ", result)
#     print("Type: ", type(result))
# elif target_type == "str" :
#     result = str(value)
#     print("Converted value: ",result)
#     print("Type: ", type(result))
# elif target_type == "bytes" :
#     result = value.encode("utf-8")
#     print("Converted value: ", result)
#     print("Type: ", type(result))



# Ex_15 : Գրել ծրագիր, որը user-ից վերցնում է name, age, python_level, score, has_laptop եւ
# preferred_language։

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# py_level = input("Enter your python level: ")
# score = int(input("Enter your score: "))
# has_laptop = input("Do you have a laptop (yes/no): ")
# preferred_language = input("Enter your preferred language: ")
#
# if age < 16:
#     print(f"{name}, you are too young for the course.")
#
# elif has_laptop == "yes":
#     print(f"{name}, laptop is required for the course.")
#
# elif score < 40:
#     print(f"{name}, you are assigned to the preparation group.")
#     print(f"Preferred language: {preferred_language}")
#
# elif py_level == "beginner" and score >= 40:
#     print(f"{name}, you are assigned to the beginner group.")
#     print(f"Preferred language: {preferred_language}")
#
# elif py_level == "intermediate" and score >= 70:
#     print(f"{name}, you are assigned to the intermediate group.")
#     print(f"Preferred language: {preferred_language}")
#
# elif py_level == "advanced" and score >= 85:
#     print(f"{name}, you are assigned to the advanced group.")
#     print(f"Preferred language: {preferred_language}")
#
# else:
#     print(f"{name}, manual review required.")



# Ex_16 : Գրել ծրագիր, որը user-ից վերցնում է username, password եւ role։

# username = input("Enter your username")
# password = input("Enter your password: ")
#
#
# if username != "admin" or password != "1234" :
#     print("Access denied.")
# else :
#      role = input("Enter your role: ")
#      if role == "teacher" :
#        print("The user has logged into the teacher dashboard.")
#      elif role == "student" :
#       print("The user has logged into the student dashboard.")
#      elif role == "manager":
#         print("The user has logged into the manager dashboard.")
#      else:
#          print("The role is unknown")


# Ex_17 : User-ից վերցնել balance, withdraw_amount եւ is_verified։

# balance = int(input("Enter your balance: "))
# amount = int(input("Enter your Withdraw_amount: "))
# is_verified = input("Is account verified ? : ")
#
# if amount <= 0 :
#     print("Wrong amount")
# elif is_verified == "no" :
#     print("Verification is compulsory: ")
# elif amount < balance :
#     print("Withdrawal is a successful:")
# else:
#     print("Not enough balance:")



# Ex_18 : User-ից վերցնել score, attendance_percent եւ has_project։

# score = int(input("Enter score: "))
# att_percent = int(input("Enter attendance percent: "))
# has_projeck = input("Do you have a projeck ?  ")
#
# if score < 0 or score > 100 :
#     print("Invalid score.")
# elif att_percent < 70 :
#     print("The student fails due to attendance.")
# elif has_projeck != "yes" :
#     print("The student fails due to project.")
# else:
#       if score >= 90:
#          print("Excellent")
#       elif score >= 75:
#            print("Good")
#       elif score >= 60:
#            print("Passed")
#       else:
#             print("Failed")



# Ex_19 : User-ից վերցնել temperature, is_raining եւ wind_speed։

# temperature = int(input("Enter temperature: "))
# is_raining = input("Is it raining ? : ")
# wind_speed = int(input("Wind spedd : "))
#
# if temperature < -40 or temperature > 60:
#     print("Invalid temperature.")
#
# else:
#     if is_raining == "yes":
#         if wind_speed > 50:
#             print("Storm risk! Stay at home.")
#         else:
#             print("Take an umbrella.")
#     else:
#         if temperature >= 30:
#             print("Hot weather: wear light clothes.")
#         elif temperature >= 15:
#             print("Good weather.")
#         elif temperature >= 0:
#             print("Cold weather: wear a jacket.")
#         else:
#             print("Very cold: wear warm clothes.")