import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('./loan_prediction_model.pkl', 'rb'))

# Function to handle prediction
def predict_loan():
    try:
        input_data = [
            0 if gender_var.get() == 'Female' else 1,
            1 if married_var.get() == 'Yes' else 0,
            {'0': 0, '1': 1, '2': 2, '3+': 3}[dependents_var.get()],
            0 if education_var.get() == 'Graduate' else 1,
            1 if self_employed_var.get() == 'Yes' else 0,
            float(applicant_income_entry.get()),
            float(coapplicant_income_entry.get()),
            float(loan_amount_entry.get()),
            float(loan_term_var.get()),
            float(credit_history_var.get()),
            {'Urban': 2, 'Rural': 0, 'Semiurban': 1}[property_area_var.get()]
        ]
        prediction = model.predict([input_data])[0]
        result = "✅ Loan Approved" if prediction == 1 else "❌ Loan Not Approved"
        messagebox.showinfo("Prediction Result", result)
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# Create main window
root = tk.Tk()
root.title("Loan Approval Predictor")
root.geometry("400x600")

# Define Tkinter variables
gender_var = tk.StringVar(value="Male")
married_var = tk.StringVar(value="No")
dependents_var = tk.StringVar(value="0")
education_var = tk.StringVar(value="Graduate")
self_employed_var = tk.StringVar(value="No")
loan_term_var = tk.StringVar(value="360.0")
credit_history_var = tk.StringVar(value="1.0")
property_area_var = tk.StringVar(value="Urban")

# UI Layout
fields = [
    ("Gender", gender_var, ['Male', 'Female']),
    ("Married", married_var, ['Yes', 'No']),
    ("Dependents", dependents_var, ['0', '1', '2', '3+']),
    ("Education", education_var, ['Graduate', 'Not Graduate']),
    ("Self Employed", self_employed_var, ['Yes', 'No']),
    ("Loan Term", loan_term_var, ['360.0', '120.0', '180.0', '240.0']),
    ("Credit History", credit_history_var, ['1.0', '0.0']),
    ("Property Area", property_area_var, ['Urban', 'Rural', 'Semiurban'])
]

for label_text, var, options in fields:
    ttk.Label(root, text=label_text).pack(pady=(10,0))
    ttk.Combobox(root, textvariable=var, values=options, state="readonly").pack()

# Entry fields for numerical input
ttk.Label(root, text="Applicant Income").pack(pady=(10, 0))
applicant_income_entry = ttk.Entry(root)
applicant_income_entry.pack()

ttk.Label(root, text="Coapplicant Income").pack(pady=(10, 0))
coapplicant_income_entry = ttk.Entry(root)
coapplicant_income_entry.pack()

ttk.Label(root, text="Loan Amount").pack(pady=(10, 0))
loan_amount_entry = ttk.Entry(root)
loan_amount_entry.pack()

# Predict button
ttk.Button(root, text="Predict Loan Approval", command=predict_loan).pack(pady=20)

# Run the application
root.mainloop()
