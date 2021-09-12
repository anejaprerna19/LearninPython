#Password Checker Assignment from Udemy Course
#In this simple assignment, we take user inputs for username and password and then calculate and print the length of password.
username= input("What is your username? ");
password= input("Enter the password ");

pass_length= len(password)
hidden_pass= '*' * pass_length

print(f'{username}, your password {hidden_pass} is {pass_length} letters long ')