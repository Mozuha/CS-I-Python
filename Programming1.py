# Alyosha Perez, Mizuki Hashimoto
type_of_employee = input('Enter your type of employment: ')
invalid = True  # Assigns the boolean valuable True to invalid to run while operator

while invalid:

    if type_of_employee == 'Salaried':
        salary = int(input('Enter your salary: '))
        weekly_salary = salary * 5  # Employee work 5 days per week
        print('Your weekly pay amount is $', weekly_salary, '.')
        invalid = False  # Assigns the boolean valuable False to not run while operator

    elif type_of_employee == 'Hourly':
        pay_rate = int(input('Enter your pay rate: '))
        work_hours = int(input('Enter your working hours: '))
        invalid = False
        if work_hours <= 40:
            weekly_pay = pay_rate * work_hours
            print('Your weekly pay amount is $', weekly_pay, '.')

            """
            For over 40 hours:
            Time and a half pay is 50% more than an employee's regular pay rate. 
            Evaluate weekly pay amount by add time and a half pay times over work hours to pay amount until 40 hours 
            work.
            We did (pay_rate * 40) because in this situation, it is apparent that employee has already worked for 
            40 hours before his work hours exceed.
            """
        elif work_hours > 40:
            weekly_pay = (pay_rate * 40) + ((pay_rate * 1.5) * (work_hours - 40))
            print('Your weekly pay amount is $', weekly_pay, '.')

    else:
        print('Invalid. Try again.')  # Tell user that the variable user entered is invalid
        invalid = True  # Assigns the boolean valuable True to run while operator
        type_of_employee = input('Enter your type of employment: ')  # Ask user to enter the type of employment again
