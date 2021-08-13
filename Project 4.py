"""4. As an alternative to APR, the interest accrued on an account is often described
      in terms of a nominal rate and the number of compounding periods. For example,
      if the interest rate is 3percent and the interest is compounded quarterly, the account
      actually earns 3/4% interest every 3 months.
      Modify the futval . py program to use this method of entering the interest rate. The
      program should prompt the user for the yearly rate (rate) and the number of times that
      the interest is compounded each year (periods). To compute the value in ten years,
      the program will loop 10 * periods times and accrue rate/period interest on each iteration.

    futval.py:
    # A program to compute the value of an investment
    # carried 10 years into the future
    def main () :
        print ("This program calculates the future value")
        print ("of a 10-year investment.")
        principal - eval (input ("Enter the initial principal: ") )
        apr - eval (input ("Enter the annual interest rate: ") )
        for i in range (10) :
        principal = principal * (1 + apr)
        print ("The value in 10 years is: ", principal)
    main ()
"""


# A program to compute the value of an investment
# carried 10 years into the future
def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    for i in range(10):
        principal += principal * (i + apr/100)
    print("The value in 10 years is: ", principal)


main()
