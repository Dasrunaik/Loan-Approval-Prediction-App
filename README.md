
#  Loan Prediction App

This is a Streamlit web application that predicts whether a loan will be approved or rejected based on user inputs. It uses a machine learning model trained on financial and personal data.

---

##  Features

- Interactive sliders and dropdowns for input
- Prediction of loan approval based on trained ML model
- Real-time feedback
- Built with Python, Streamlit, and scikit-learn

---

##  Project Structure

loan_approval/
│
├── app.py # Main Streamlit app

├── model.pkl # Trained ML model (e.g., RandomForest, SVM, etc.)

├── sc.pkl # Scaler (e.g., StandardScaler or MinMaxScaler)

└── README.md # This file


---

##  Model Input Features

The app takes the following inputs:

- Number of Dependents (`no_of_dependents`)
- Education Level (`Graduated` / `Not Graduated`)
- Self-Employment Status (`Yes` / `No`)
- Annual Income
- Loan Amount
- Loan Term (in years)
- CIBIL Score (0 - 1000)
- Total Assets

These features are preprocessed and passed to the trained model to predict approval status.

---

##Requirements

Python 3.7+

streamlit

pandas

scikit-learn

pickle (standard library)



## Sample Output


 Loan is Approved

 Loan is Rejected


