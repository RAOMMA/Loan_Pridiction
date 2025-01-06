# Loan Predication

## Overview

This project offers a machine-learning model that create classification on loan applicable or NOt applicablr person based on various features. It utilizes a SVM Model trained on a dataset.


## Dataset

- **Dataset Name**: Loan Predication
- **Data Source**: https://www.kaggle.com/datasets/ninzaami/loan-predication  and also upload on git .
- The dataset contains the following attributes:
  - Feature columns (13): Numerical and catagorical values representing various loan-related features.
  - Target column: price of houses.

## Project Structure

- `README.md`: Documentation of the project.
- `main.py`: Python script for making loan classification.
- `data.joblib` : weights of transformer used to transfer data before traning.
- `model.joblib`: Pre-trained svm model for diabetes classification.

## Setup

1. Clone the repository:
   ```shell
   git clone <repository-url>
   cd Loan Predication
Create a virtual environment (recommended) and install the required dependencies:
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

## Usage
Clone this repository to your local machine.
Ensure you have the pre-trained logistic regression model ('model.pkl') in the same directory as the script ('diabetes_prediction.py').
Open a command prompt or terminal and navigate to the directory where the script is located.
Run the script with the --value argument followed by a comma-separated list of feature values that you want to classify.
## For example:
python main.py --Gender Male, --Married No, --Dependents 0, --Education Graduate, --Self_Employed No, --ApplicantIncome 5849, --CoapplicantIncome 0, --LoanAmount 128, --Loan_Amount_Term 360, --Credit_History 1, --Property_Area Urban

Follow the instructions in the script for classification.

## Model Training
The project uses a SVM model for classification. The pre-trained model is saved as 'svm.pkl'.

## Evaluation
The script provides binary predictions. You can evaluate the model's performance using metrics like accuracy,and classification_report.

## Results
The project provides classification for loan based on the input features. The performance of the model may vary depending on the dataset used.

## Future Improvements
There are several ways to improve the model and the project:

Explore more advanced machine learning techniques.
Fine-tune hyperparameters for better model performance.
Gather more labeled data for improved accuracy.
## References

- Author: Mirza Salman
- Contact: salmansaluu661@gmail.com

Feel free to customize this README to include any additional information you want to provide about the project.
