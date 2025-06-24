
#Assignment 2.1

def calcu_grades():
    t_marks = 0
    n_subjects = 5

    print("Enter marks for 5 subjects (out of 100 each):")

    for i in range(n_subjects):
        while True:
            mark = float(input(f"Enter marks for subject {i+1}: "))
            if 0 <= mark <= 100:
                t_marks += mark
                break
            else:
                print("Marks should be between 0 and 100. Please try again.")
    percentage = (t_marks / (n_subjects * 100)) * 100

    print(f"\nTotal Marks: {t_marks}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 60:
        grade = 'A'
    elif percentage >= 50:
        grade = 'B'
    elif percentage >= 40:
        grade = 'C'
    elif percentage >= 33:
        grade = 'D'
    else:
        grade = 'Fail'

    print(f"Grade: {grade}")
# TO EXECUTE ->
#calcu_grades()


#Assignment 2.2

def factorial_():
    while True:
        n = int(input("Enter a integer: "))
        if n >= 0:
            break
        else:
            print("Invalid input. Please enter an integer.")

    factorial = 1

    if n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, n + 1):
            factorial *= i  # This is equivalent to factorial = factorial * i
        print(f"The factorial of {n} is {factorial}")
# TO EXECUTE ->
#factorial_()

#Assignment 2.3

def bill():
    
    bill_items = []
    prices = []

    while True:
        print("\nBilling Options ->")
        print("a. Create Bill")
        print("b. Display Item Price and Total Bill Amount")
        print("c. Display Total Bill")
        print("d. Exit")

        choice = input("Enter your choice: ")

        if choice == 'a':
            it_name = input("Enter item name: ")
            
            it_price = float(input(f"Enter price for {it_name}: "))
            bill_items.append(it_name)
            prices.append(it_price)
            print(f"'{it_name}' added to the bill.")

        elif choice == 'b':
            
            print("\nCurrent Bill Items ->")
                
            for i in range(len(bill_items)):
                item = bill_items[i]
                price = prices[i]
                print(f"{i+1}. {item}: ${price:.2f}")
            total_bill = sum(prices)
            print(f"\nCurrent Total Bill Amount: ${total_bill:.2f}")

        elif choice == 'c':
            total_bill = sum(prices)
            print("\nTotal Bill ->")
            print(f"Total Bill Amount: ${total_bill:.2f}")

        elif choice == 'd':
            print("Exiting billing system. Thank you!")
            break
        else:
            print("Invalid choice. Please select from 'a', 'b', 'c', or 'd'.")

# TO EXECUTE ->
bill()

#Assignment 2.4

def smallest_number():
    #li = [51, 19, 87, 5, 25, 93, 15]
    num = input("Enter numbers separated by spaces: ")
    l = [int(x) for x in num.split()]
    
    smallest = min(l)
    print(f"The list is: {l}")
    print(f"The smallest number in the list is: {smallest}")
# TO EXECUTE ->
#smallest_number()


#Assignment 2.5

def second_greatest():
    
    #li = [51, 19, 87, 5, 25, 93, 15]
    

    num = input("Enter numbers separated by spaces: ")
    li = [int(x) for x in num.split()]

    print(f"Original list: {li}")
    
    unique_sorted_list = sorted(list(set(li)))

    if len(unique_sorted_list) < 2:
        print("needs at least two unique elements.")
    else:
        second_greatest = unique_sorted_list[-2]
        print(f"Unique sorted list: {unique_sorted_list}")
        print(f"The second greatest number is: {second_greatest}")
# TO EXECUTE ->
#second_greatest()


#Assignment 2.6

def second_smallest():
    
    #my_lis = [51, 19, 87, 5, 25, 93, 15]
    
   
    num = input("Enter numbers separated by spaces: ")
    lis = [int(x) for x in num.split()]

    print(f"Original list: {lis}")

    unique_sorted_list = sorted(list(set(lis)))

    if len(unique_sorted_list) < 2:
        print("needs at least two unique elements.")
    else:
        second_smallest = unique_sorted_list[1]
        print(f"Unique sorted list: {unique_sorted_list}")
        print(f"The second smallest number is: {second_smallest}")
# TO EXECUTE ->
#second_smallest()

