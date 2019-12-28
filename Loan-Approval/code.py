# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
bank=pd.read_csv(path)
categorical_var=bank.select_dtypes(include= 'object')
print(categorical_var)
numerical_var= bank.select_dtypes(include = 'number')
print(numerical_var)

# code starts here






# code ends here


# --------------
# code starts here
banks=bank.drop('Loan_ID', 1)
banks
bank_mode=banks.mode()

banks=banks.fillna('bank_mode')
banks

#code ends here


# --------------
# Code starts here
avg_loan_amount=banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc='mean')
avg_loan_amount


# code ends here



# --------------
# code starts here
loan_approved_se=((banks['Self_Employed'] == 'Yes') & (banks['Loan_Status']== 'Y')).sum()
loan_approved_nse=((banks['Self_Employed'] == 'No') & (banks['Loan_Status']== 'Y')).sum()
Total_Loan_status=614
percentage_se=loan_approved_se*100/Total_Loan_status
print(percentage_se)
percentage_nse=loan_approved_nse*100/Total_Loan_status
print(percentage_nse)


# code ends here


# --------------
# code starts here
loan_term=banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )
loan_term
big_loan_term=loan_term.apply(lambda x: x>=25).sum()
big_loan_term



# code ends here


# --------------
# code starts here

loan_groupby=banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History',]

mean_values=loan_groupby.mean()
mean_values


# code ends here


