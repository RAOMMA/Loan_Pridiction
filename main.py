


import argparse
import joblib

# Load the pre-trained logistic regression model
model = joblib.load('C:/salman/ML/Loan Predication/SVM.pkl')

tra=joblib.load("C:/salman/ML/Loan Predication/transfer.pkl")

# Create an argument parser
parser = argparse.ArgumentParser(description="Loan perdection")

# Add the --value argument to accept a data record
parser.add_argument('--Gender', type=str, required=True, help="Gender")
parser.add_argument('--Married', type=str, required=True, help="Married")
parser.add_argument('--Dependents', type=int, required=True, help="Dependents")
parser.add_argument('--Education', type=str, required=True, help="Education")
parser.add_argument('--Self_Employed', type=str, required=True, help="Self_Employed")
parser.add_argument('--ApplicantIncome', type=int, required=True, help="ApplicantIncome")
parser.add_argument('--CoapplicantIncome', type=int, required=True, help="CoapplicantIncom")
parser.add_argument('--LoanAmount', type=int, required=True, help="LoanAmount")
parser.add_argument('--Loan_Amount_Term', type=int ,required=True, help="Loan_Amount_Term")
parser.add_argument('--Credit_History', type=int, required=True, help="Credit_History")
parser.add_argument('--Property_Area', type=str, required=True, help="Property_Area")

# Parse the command-line arguments
args = parser.parse_args()


# Parse the data record as a list of floats
data_list =[[args.Gender,args.Married,args.Dependents,args.Education,args.Self_Employed,args.ApplicantIncome,args.CoapplicantIncome,args.LoanAmount,args.Loan_Amount_Term,args.Credit_History,args.Property_Area]]

#Convert to Dataframe
import pandas as pd
list=pd.DataFrame(data_list,columns=(['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']))

#Apply transfermation
x=tra.transform(list)

#predict
pred=model.predict(x)[0]

#Apply condition
if pred==1:
    print('yes')
elif pred==0:
    print('NO')