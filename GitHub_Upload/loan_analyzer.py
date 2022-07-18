# coding: utf-8
import csv
from pathlib import Path

loan_costs = [500, 600, 200, 1000, 450]
total_loans = len(loan_costs)
loan_price = 500,
remaining_months = 9 
future_value = 1000
annual_discount_rate = 0.20

print("The total number of loans in the list is", total_loans)

total_value = sum(loan_costs)
print(total_value," is the sum of all loans")

average_loan_price = total_value / total_loans
print("The average loan price is", average_loan_price)

present_value = (future_value)/(1+annual_discount_rate/12)**remaining_months


print("The Present Value is ", present_value)

new_loan = {
    "loan_price": 500,
    "remaining_months":9,
    "repayment_interval":"bullet",
    "future_value":1000,}
    
loan_future_value = new_loan.get(future_value)
loan_remaining_months = new_loan.get(remaining_months)

print("The loan future value is", future_value)
print("The loan has",remaining_months, "months remaining.")

present_value = (future_value)/(1+annual_discount_rate/12)**remaining_months

if present_value == loan_price:
    print("Loan is worth atlest the cost to buy")
else:
    print("Loan is too expensive")



   
    def calculate_present_value(new_loan):
       return (new_loan["future_value"])/(1+annual_discount_rate/12)** new_loan["remaining_months"]
        
    print("The New Loan Present Value is ",calculate_present_value(new_loan))
    


#1. Create a new, empty list called `inexpensive_loans`.
#2. Use a for loop to select each loan from a list of loans.
#    a. is less than or equal to 500
#    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
#. Print the list of inexpensive_loans.



loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },]

inexpensive_loans = [] 
for loan in loans:     
    if loan['loan_price'] <= 500:
        inexpensive_loans.append(loan["loan_price"])
print(inexpensive_loans)


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

output_path = Path("inexpensive_loans.csv")

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    for item in inexpensive_loans:
         csvwriter.writerow(loan.values())







    