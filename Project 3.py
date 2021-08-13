"""3.Write an improved version of the futval . py program from Chapter 2. Your program
    will prompt the user for the amount of the investment, the annualized interest rate,
    and the number of years of the investment. The program will then output a nicely formatted
    table that tracks the value of the investment year by year. Your output might look something like this:

    Year        Value
    ----------------
    0    $2000.00
    1    $2200.00
    2	 $2420.00
    3	 $2662.00
    4	 $2928.20
    5	 $3221.02
    6	 $3542.12
    7	 $3897.43
"""

import json

if __name__ == '__main__':
    while True:
        try:
            amount = int(input("Enter Principle amount $: "))
            interest = float(input("Enter Rate of Interest: "))
            years = int(input("Enter Years in Investment: "))
        except:
            print("\n!!!Please Enter in Numerals only!!!\n")
            continue

        amount_dct = {}

        for i in range(int(years) + 1):
            if "." in str(amount):
                amount_dct[i] = float(str(amount)[0:str(amount).index(".")+3])
            else:
                amount_dct[i] = float(amount)
            amount = amount * (1 + int(interest)/100)

        print("Year     Value\n----------------", json.dumps(amount_dct, indent=1).replace(":", "      ")
              .replace('"', "").replace(",", "").replace("{", "").replace("}", ""))
        break
