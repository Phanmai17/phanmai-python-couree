
# ============================================================
# PERSONAL INCOME TAX CALCULATOR
# PROGRESSIVE TAX RATE
# ============================================================
#
# Program Features:
# 1. Receive net income from the user
# 2. Calculate progressive income tax
# 3. Display tax for each tax bracket
# 4. Display total tax
# 5. Display income after tax
# 6. Calculate Effective Tax Rate
#
# ============================================================


# ------------------------------------------------------------
# SECTION 1: TAX RATES
# ------------------------------------------------------------

RATE_1 = 0.00

RATE_2 = 0.05

RATE_3 = 0.10

RATE_4 = 0.15

RATE_5 = 0.20

RATE_6 = 0.25

RATE_7 = 0.30

RATE_8 = 0.35


# ------------------------------------------------------------
# SECTION 2: INCOME LIMITS
# ------------------------------------------------------------

LIMIT_1 = 150000

LIMIT_2 = 300000

LIMIT_3 = 500000

LIMIT_4 = 750000

LIMIT_5 = 1000000

LIMIT_6 = 2000000

LIMIT_7 = 5000000


# ------------------------------------------------------------
# SECTION 3: GET INCOME
# ------------------------------------------------------------

def get_income():

    """
    Get net income from the user.
    """

    while True:

        try:

            income = float(
                input("Enter net income: ")
            )

            if income < 0:

                print(
                    "Please enter income greater than or equal to 0."
                )

                continue

            return income

        except ValueError:

            print(
                "Please enter numbers only."
            )


# ------------------------------------------------------------
# SECTION 4: CALCULATE TAX STEP 1
# ------------------------------------------------------------

def calculate_step_1(income):

    if income <= LIMIT_1:

        amount = income

    else:

        amount = LIMIT_1

    tax = amount * RATE_1

    return amount, tax


# ------------------------------------------------------------
# SECTION 5: CALCULATE TAX STEP 2
# ------------------------------------------------------------

def calculate_step_2(income):

    if income <= LIMIT_1:

        amount = 0

    elif income <= LIMIT_2:

        amount = income - LIMIT_1

    else:

        amount = LIMIT_2 - LIMIT_1

    tax = amount * RATE_2

    return amount, tax


# ------------------------------------------------------------
# SECTION 6: CALCULATE TAX STEP 3
# ------------------------------------------------------------

def calculate_step_3(income):

    if income <= LIMIT_2:

        amount = 0

    elif income <= LIMIT_3:

        amount = income - LIMIT_2

    else:

        amount = LIMIT_3 - LIMIT_2

    tax = amount * RATE_3

    return amount, tax


# ------------------------------------------------------------
# SECTION 7: CALCULATE TAX STEP 4
# ------------------------------------------------------------

def calculate_step_4(income):

    if income <= LIMIT_3:

        amount = 0

    elif income <= LIMIT_4:

        amount = income - LIMIT_3

    else:

        amount = LIMIT_4 - LIMIT_3

    tax = amount * RATE_4

    return amount, tax


# ------------------------------------------------------------
# SECTION 8: CALCULATE TAX STEP 5
# ------------------------------------------------------------

def calculate_step_5(income):

    if income <= LIMIT_4:

        amount = 0

    elif income <= LIMIT_5:

        amount = income - LIMIT_4

    else:

        amount = LIMIT_5 - LIMIT_4

    tax = amount * RATE_5

    return amount, tax


# ------------------------------------------------------------
# SECTION 9: CALCULATE TAX STEP 6
# ------------------------------------------------------------

def calculate_step_6(income):

    if income <= LIMIT_5:

        amount = 0

    elif income <= LIMIT_6:

        amount = income - LIMIT_5

    else:

        amount = LIMIT_6 - LIMIT_5

    tax = amount * RATE_6

    return amount, tax


# ------------------------------------------------------------
# SECTION 10: CALCULATE TAX STEP 7
# ------------------------------------------------------------

def calculate_step_7(income):

    if income <= LIMIT_6:

        amount = 0

    elif income <= LIMIT_7:

        amount = income - LIMIT_6

    else:

        amount = LIMIT_7 - LIMIT_6

    tax = amount * RATE_7

    return amount, tax


# ------------------------------------------------------------
# SECTION 11: CALCULATE TAX STEP 8
# ------------------------------------------------------------

def calculate_step_8(income):

    if income <= LIMIT_7:

        amount = 0

    else:

        amount = income - LIMIT_7

    tax = amount * RATE_8

    return amount, tax


# ------------------------------------------------------------
# SECTION 12: CALCULATE ALL TAX
# ------------------------------------------------------------

def calculate_tax(income):

    step_1_amount, step_1_tax = (
        calculate_step_1(income)
    )

    step_2_amount, step_2_tax = (
        calculate_step_2(income)
    )

    step_3_amount, step_3_tax = (
        calculate_step_3(income)
    )

    step_4_amount, step_4_tax = (
        calculate_step_4(income)
    )

    step_5_amount, step_5_tax = (
        calculate_step_5(income)
    )

    step_6_amount, step_6_tax = (
        calculate_step_6(income)
    )

    step_7_amount, step_7_tax = (
        calculate_step_7(income)
    )

    step_8_amount, step_8_tax = (
        calculate_step_8(income)
    )

    total_tax = (

        step_1_tax
        + step_2_tax
        + step_3_tax
        + step_4_tax
        + step_5_tax
        + step_6_tax
        + step_7_tax
        + step_8_tax

    )

    return (

        step_1_amount,
        step_1_tax,

        step_2_amount,
        step_2_tax,

        step_3_amount,
        step_3_tax,

        step_4_amount,
        step_4_tax,

        step_5_amount,
        step_5_tax,

        step_6_amount,
        step_6_tax,

        step_7_amount,
        step_7_tax,

        step_8_amount,
        step_8_tax,

        total_tax

    )


# ------------------------------------------------------------
# SECTION 13: PRINT LINE
# ------------------------------------------------------------

def print_line():

    print("-" * 60)


# ------------------------------------------------------------
# SECTION 14: SHOW HEADER
# ------------------------------------------------------------

def show_header():

    print_line()

    print(
        "PERSONAL INCOME TAX CALCULATOR"
    )

    print(
        "PROGRESSIVE TAX RATE"
    )

    print_line()


# ------------------------------------------------------------
# SECTION 15: SHOW TAX DETAILS
# ------------------------------------------------------------

def show_tax_detail(income):

    result = calculate_tax(income)


    step_1_amount = result[0]

    step_1_tax = result[1]


    step_2_amount = result[2]

    step_2_tax = result[3]


    step_3_amount = result[4]

    step_3_tax = result[5]


    step_4_amount = result[6]

    step_4_tax = result[7]


    step_5_amount = result[8]

    step_5_tax = result[9]


    step_6_amount = result[10]

    step_6_tax = result[11]


    step_7_amount = result[12]

    step_7_tax = result[13]


    step_8_amount = result[14]

    step_8_tax = result[15]


    total_tax = result[16]


    print()

    print("TAX DETAILS")

    print_line()


    print(
        "Step 1 : 0 - 150,000 Baht"
    )

    print(
        "Income in this step = "
        "{:,.2f} Baht".format(step_1_amount)
    )

    print(
        "Tax Rate = 0%"
    )

    print(
        "Tax = {:,.2f} Baht".format(step_1_tax)
    )

    print()


    print(
        "Step 2 : 150,001 - 300,000 Baht"
    )

    print(
        "Income in this step = "
        "{:,.2f} Baht".format(step_2_amount)
    )

    print(
        "Tax Rate = 5%"
    )

    print(
        "Tax = {:,.2f} Baht".format(step_2_tax)
    )

    print()


    print(
        "Step 3 : 300,001 - 500,000 Baht"
    )

    print(
        "Income in this step = "
        "{:,.2f} Baht".format(step_3_amount)
    )

    print(
        "Tax Rate = 10%"
    )

    print(
        "Tax = {:,.2f} Baht".format(step_3_tax)
    )

    print()


    print(
        "Step 4 : 500,001 - 750,000 Baht"
    )

    print(
        "Income in this step = "
        "{:,.2f} Baht".format(step_4_amount)
    )

    print(
        "Tax Rate = 15%"
    )

    print(
        "Tax = {:,.2f} Baht".format(step_4_tax)
    )

    print()


    print(
        "Step 5 : 750,001 - 1,000,000 Baht"
    )

    print(
        "Income in this step = "
        "{:,.2f} Baht".format(step_5_amount)
    )

    print(
        "Tax Rate = 20%"
    )

    print(
        "Tax = {:,.2f} Baht".format(step_5_tax)
    )

    print()


    print(
        "Step 6 : 1,000,001 - 2,000,000 Baht"
    )

    print(
        "Income in this step = "
        "{:,.2f} Baht".format(step_6_amount)
    )

    print(
        "Tax Rate = 25%"
    )

    print(
        "Tax = {:,.2f} Baht".format(step_6_tax)
    )

    print()


    print(
        "Step 7 : 2,000,001 - 5,000,000 Baht"
    )

    print(
        "Income in this step = "
        "{:,.2f} Baht".format(step_7_amount)
    )

    print(
        "Tax Rate = 30%"
    )

    print(
        "Tax = {:,.2f} Baht".format(step_7_tax)
    )

    print()


    print(
        "Step 8 : More than 5,000,000 Baht"
    )

    print(
        "Income in this step = "
        "{:,.2f} Baht".format(step_8_amount)
    )

    print(
        "Tax Rate = 35%"
    )

    print(
        "Tax = {:,.2f} Baht".format(step_8_tax)
    )

    print_line()

    print(
        "Total Tax = {:,.2f} Baht".format(
            total_tax
        )
    )

    print_line()


# ------------------------------------------------------------
# SECTION 16: CALCULATE REMAINING INCOME
# ------------------------------------------------------------

def calculate_remaining_income(
    income,
    tax
):

    remaining_income = income - tax

    return remaining_income


# ------------------------------------------------------------
# SECTION 17: CALCULATE EFFECTIVE TAX RATE
# ------------------------------------------------------------

def calculate_effective_rate(
    income,
    tax
):

    if income == 0:

        return 0

    effective_rate = (
        tax / income
    ) * 100

    return effective_rate


# ------------------------------------------------------------
# SECTION 18: SHOW SUMMARY
# ------------------------------------------------------------

def show_summary(income):

    result = calculate_tax(income)

    total_tax = result[16]


    remaining_income = (
        calculate_remaining_income(
            income,
            total_tax
        )
    )


    effective_rate = (
        calculate_effective_rate(
            income,
            total_tax
        )
    )


    print()

    print_line()

    print("CALCULATION SUMMARY")

    print_line()


    print(
        "Net Income = {:,.2f} Baht".format(
            income
        )
    )


    print(
        "Total Tax = {:,.2f} Baht".format(
            total_tax
        )
    )


    print(
        "Income After Tax = {:,.2f} Baht".format(
            remaining_income
        )
    )


    print(
        "Effective Tax Rate = {:.2f}%".format(
            effective_rate
        )
    )


    print_line()


# ------------------------------------------------------------
# SECTION 19: RUN CALCULATION
# ------------------------------------------------------------

def run_program():

    show_header()

    income = get_income()

    show_tax_detail(income)

    show_summary(income)


# ------------------------------------------------------------
# SECTION 20: SHOW MENU
# ------------------------------------------------------------

def show_menu():

    print()

    print_line()

    print("PROGRAM MENU")

    print_line()

    print("1. Calculate Tax")

    print("2. Show Tax Rates")

    print("3. Exit")

    print_line()


# ------------------------------------------------------------
# SECTION 21: SHOW TAX RATES
# ------------------------------------------------------------

def show_tax_rate():

    print()

    print_line()

    print(
        "PROGRESSIVE TAX RATES"
    )

    print_line()


    print(
        "0 - 150,000 Baht : 0%"
    )


    print(
        "150,001 - 300,000 Baht : 5%"
    )


    print(
        "300,001 - 500,000 Baht : 10%"
    )


    print(
        "500,001 - 750,000 Baht : 15%"
    )


    print(
        "750,001 - 1,000,000 Baht : 20%"
    )


    print(
        "1,000,001 - 2,000,000 Baht : 25%"
    )


    print(
        "2,000,001 - 5,000,000 Baht : 30%"
    )


    print(
        "More than 5,000,000 Baht : 35%"
    )


    print_line()


# ------------------------------------------------------------
# SECTION 22: MAIN PROGRAM
# ------------------------------------------------------------

def main():

    while True:

        show_menu()

        choice = input(
            "Enter your choice (1-3): "
        )


        if choice == "1":

            run_program()


        elif choice == "2":

            show_tax_rate()


        elif choice == "3":

            print()

            print(
                "Program terminated."
            )

            break


        else:

            print()

            print(
                "Invalid choice. "
                "Please select 1, 2, or 3."
            )


# ------------------------------------------------------------
# SECTION 23: START PROGRAM
# ------------------------------------------------------------

if __name__ == "__main__":

    main()
  
