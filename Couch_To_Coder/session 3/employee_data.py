employees = [
 {
 "first_name":"Jose",
 "last_name":"Lopez",
 "email":"joselopez0944@example.com",
 "age":25,
 "job_title":"Project Manager",
 "years_of_experience":1,
 "salary":8500,
 "department":"Product"
 },
 {
 "first_name":"Diane",
 "last_name":"Carter",
 "email":"dianecarter1228@example.com",
 "age":26,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":2,
 "salary":7000,
 "department":"Product"
 },
 {
 "first_name":"Shawn",
 "last_name":"Foster",
 "email": None,
 "age":37,
 "job_title":"Customer Service Rep",
 "years_of_experience":14,
 "salary":17000,
 "department":"Business"
 },
 {
 "first_name":"Brenda",
 "last_name":"Fisher",
 "email":"brendafisher3185@example.com",
 "age":31,
 "job_title":"Web Developer",
 "years_of_experience":8,
 "salary":10000,
 "department":"Product"
 },
 {
 "first_name":"Sean",
 "last_name":"Hunter",
 "email": None,
 "age":35,
 "job_title":"Project Manager",
 "years_of_experience":11,
 "salary":14500,
 "department":"Product"
 },
 {
 "first_name":"Joshua",
 "last_name":"Jacobs",
 "email":"joshuajacobs5904@example.com",
 "age":28,
 "job_title":"Project Manager",
 "years_of_experience":3,
 "salary":10500,
 "department":"Business"
 },
 {
 "first_name":"Brianna",
 "last_name":"Marshall",
 "email":None,
 "age":33,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":10,
 "salary":11000,
 "department":"Product"
 },
 {
 "first_name":"John",
 "last_name":"Tate",
 "email":"johntate7881@example.com",
 "age":33,
 "job_title":"Mobile Developer",
 "years_of_experience":10,
 "salary":11000,
 "department":"Product"
 },
 {
 "first_name":"Jillian",
 "last_name":"Byrd",
 "email":None,
 "age":34,
 "job_title":"Business Analyst",
 "years_of_experience":10,
 "salary":11000,
 "department":"Business"
 },
 {
 "first_name":"Melanie",
 "last_name":"Sharp",
 "email":"melaniesharp9256@example.com",
 "age":41,
 "job_title":"Web Developer",
 "years_of_experience":15,
 "salary":14500,
 "department":"Product"
 },
 {
 "first_name":"Brandy",
 "last_name":"Mckee",
 "email":None,
 "age":37,
 "job_title":"Marketing Manager",
 "years_of_experience":14,
 "salary":14000,
 "department":"Business"
 },
 {
 "first_name":"Robert",
 "last_name":"Simpson",
 "email":"robertsimpson11778@example.com",
 "age":36,
 "job_title":"Marketing Manager",
 "years_of_experience":12,
 "salary":15000,
 "department":"Business"
 },
 {
 "first_name":"George",
 "last_name":"Mckenzie",
 "email":"georgemckenzie12384@example.com",
 "age":28,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":4,
 "salary":10000,
 "department":"Product"
 },
 {
 "first_name":"Joseph",
 "last_name":"Smith",
 "email":None,
 "age":40,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":14,
 "salary":14000,
 "department":"Product"
 },
 {
 "first_name":"Dana",
 "last_name":"Crawford",
 "email":"danacrawford14310@example.com",
 "age":32,
 "job_title":"Project Manager",
 "years_of_experience":8,
 "salary":12000,
 "department":"Product"
 },
 {
 "first_name":"Christopher",
 "last_name":"Benson",
 "email":None,
 "age":29,
 "job_title":"Web Developer",
 "years_of_experience":5,
 "salary":7500,
 "department":"Product"
 },
 {
 "first_name":"Nicole",
 "last_name":"Smith",
 "email":"nicolesmith16360@example.com",
 "age":26,
 "job_title":"Designer",
 "years_of_experience":4,
 "salary":10000,
 "department":"Product"
 },
 {
 "first_name":"Peter",
 "last_name":"Jimenez",
 "email":"peterjimenez17791@example.com",
 "age":28,
 "job_title":"UX Designer",
 "years_of_experience":3,
 "salary":6500,
 "department":"Business"
 },
 {
 "first_name":"Sergio",
 "last_name":"Boyle",
 "email":"sergioboyle18425@example.com",
 "age":31,
 "job_title":"Tester",
 "years_of_experience":6,
 "salary":9000,
 "department":"Product"
 },
 {
 "first_name":"Brianna",
 "last_name":"Moss",
 "email":None,
 "age":31,
 "job_title":"Designer",
 "years_of_experience":5,
 "salary":10500,
 "department":"Product"
 },
 {
 "first_name":"Taylor",
 "last_name":"Garner",
 "email":"taylorgarner20196@example.com",
 "age":32,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":6,
 "salary":11000,
 "department":"Product"
 },
 {
 "first_name":"Michael",
 "last_name":"Padilla",
 "email":"michaelpadilla21381@example.com",
 "age":29,
 "job_title":"Customer Service Rep",
 "years_of_experience":5,
 "salary":9500,
 "department":"Business"
 },
 {
 "first_name":"Yvette",
 "last_name":"Walker",
 "email":None,
 "age":26,
 "job_title":"Designer",
 "years_of_experience":2,
 "salary":7000,
 "department":"Product"
 },
 {
 "first_name":"Kristina",
 "last_name":"Pena",
 "email":"kristinapena23750@example.com",
 "age":34,
 "job_title":"Business Analyst",
 "years_of_experience":11,
 "salary":12500,
 "department":"Business"
 }
]





# To Print the name of the person with the highest salary ( i was playing around with dfferent numbers till it gave me one name :)
for salary in employees:
    if salary["salary"] >= 17000:
        print("Person with the highest salary : ", salary["first_name"])
        print("<------------------------------------>")
 

# HOW TO Calculate the combined years of experience of all employees
combined_experience = sum(employee["years_of_experience"] for employee in employees)
print("Combined years of experience:", combined_experience)
print("<------------------------------------>")



# code to  Collect details of employees without email addresses
employees_without_email = [employee for employee in employees if employee["email"] is None]
print("Employees without email addresses:", employees_without_email)
print("<------------------------------------>")



# To Compare Product department salaries to Business department salaries
product_salaries = sum(employee["salary"] for employee in employees if employee["department"] == "Product")
business_salaries = sum(employee["salary"] for employee in employees if employee["department"] == "Business")
print("Total Product department salaries:", product_salaries)
print("<------------------------------------>")
print("Total Business department salaries:", business_salaries)
if product_salaries > business_salaries:
    print("<------------------------------------>")
    print("Product department costs more.")
else:
    print("<------------------------------------>")
    print("Business department costs more.")



# Extension 5: Calculate the average salary for people over 30 years of age
over_30_salaries = [employee["salary"] for employee in employees if employee["age"] > 30]
average_over_30_salary = sum(over_30_salaries) / len(over_30_salaries)
print("<------------------------------------>")
print("Average salary for people over 30:", average_over_30_salary)



# Extension 6: Count employees with certain job titles
job_title_counts = {}
for employee in employees:
    job_title = employee["job_title"]
    if job_title in job_title_counts:
        job_title_counts[job_title] += 1
    else:
        job_title_counts[job_title] = 1
print("<------------------------------------>")        
print("Job title counts:", job_title_counts)
print("<------------------------------------>")