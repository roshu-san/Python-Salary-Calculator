print("Your Salary Calculator/Calculator de Salariu")
language = input("Choose/Alegeti: 1 for english/2 pentru română ")
while language == "1" or "2":
    while language == "1":
        print("This program helps you calculate your salary or to find out how much money you could save in a day, week, month or year.")
        user_input = float(input("How much do you make per hour? "))

        hours_worked = float(input("How many hours do you usually work per day? "))

        days_worked = float(input("How many days do you usually work per week? "))

        daily_salary = user_input * hours_worked

        weekly_salary = daily_salary * days_worked

        monthly_salary = weekly_salary * 4

        annual_salary = monthly_salary * 12

        print("This is your daily salary:", daily_salary)
        print("This is your weekly salary:", weekly_salary)
        print("This is your monthly salary:", monthly_salary)
        print("This is your annual salary:", annual_salary)

        percentage = float(input("What percentage of your salary do you wish to save per month? "))
        percentage_daily_salary = percentage * daily_salary / 100
        percentage_weekly_salary = percentage * weekly_salary / 100
        percentage_monthly_salary = percentage * monthly_salary / 100
        percentage_annual_salary = percentage * annual_salary / 100
        print("This is your daily savings:", percentage_daily_salary)
        print("This is your weekly savings:", percentage_weekly_salary)
        print("This is your monthly savings:", percentage_monthly_salary)   
        print("This is your annual savings:", percentage_annual_salary)
        break

    while language == "2":
        print("Acest program vă ajută să vă calculați salariul sau vă arată cât puteți economisi într-o zi, săptămână, lună sau într-un an. ")
        user_input = float(input("Cât câștigați pe oră? "))

        hours_worked = float(input("Câte ore lucrați pe zi? "))

        days_worked = float(input("Câte zile lucrați pe săptămână? "))

        daily_salary = user_input * hours_worked

        weekly_salary = daily_salary * days_worked

        monthly_salary = weekly_salary * 4

        annual_salary = monthly_salary * 12

        print("Acesta este salariul dvs. zilnic:", daily_salary)
        print("Acesta este salariul dvs. săptămânal:", weekly_salary)
        print("Acesta este salariul dvs. lunar:", monthly_salary)
        print("Acesta este salariul dvs. anual:", annual_salary)

        percentage = float(input("Cât la sută din salariu doriți să puneți deoparte? "))
        percentage_daily_salary = percentage * daily_salary / 100
        percentage_weekly_salary = percentage * weekly_salary / 100
        percentage_monthly_salary = percentage * monthly_salary / 100
        percentage_annual_salary = percentage * annual_salary / 100
        print("Salariul economisit într-o zi:", percentage_daily_salary)
        print("Salariul economisit într-o săptămână:", percentage_weekly_salary)
        print("Salariul economisit într-o lună:", percentage_monthly_salary) 
        print("Salariul economisit într-un an:", percentage_annual_salary)     
        break
    break