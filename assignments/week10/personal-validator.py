"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
print(" === PERSONAL INFORMATION VALIDATOR === ")
name = input("Enter your name: ")
age = input("Enter your age: ")
phone = input("Enter your phone number: ")
 
name (name.isalpha())
 
check_name = False
for c in name:
    check_name = c.isalpha() and c.isspace
 
check_age = False
if 18 <= age <65:
    check_age = True
 
check_phone = False
if len(phone) ==10 and phone.isdigit():
    check_phone = True
 
print("Valaidation Results:")
if check_name:
    print("Name: Valid (contains only letters and spaces)")
 
else:
    print("Name: Invalid")
 
if check_age:
    print("Age: Valid ({age} years old)")
 
else:
    print("Age: Invalid")
 
if check_phone:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid")
 
print("Formatted Information:")
print(f"Name: {name.upper()}")
     
if 18 <= age < 30:
    print("Age Group: Young Adult (18-30)")
elif 30 <= age < 60:
    print("Age group: Adult (31-50)")
elif age >60:
    print("Age Group: Senior (>60)")
 
print(f"Phone: +66-{phone}")