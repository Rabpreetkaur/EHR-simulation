import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
import datetime

# File to store patient records
FILE_NAME = "ehr_data.csv"
AUDIT_LOG = "audit_log.csv"

# Check if file exists, if not, create it with headers
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Patient ID", "Name", "Age", "Gender", "Diagnosis", "Medication", "Doctor", "Notes", "Timestamp"])

if not os.path.exists(AUDIT_LOG):
    with open(AUDIT_LOG, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Action", "Patient ID", "Timestamp"])

# Function to generate unique patient ID
def generate_patient_id():
    return f"PT{int(datetime.datetime.now().timestamp())}"

# Function to save data
def save_data():
    patient_id = id_entry.get()
    if not patient_id:
        patient_id = generate_patient_id()
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    diagnosis = diagnosis_var.get()
    medication = medication_var.get()
    doctor = doctor_entry.get()
    notes = notes_entry.get("1.0", tk.END).strip()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if not (name and age and gender and diagnosis and medication and doctor):
        messagebox.showwarning("Input Error", "All fields except Notes are required!")
        return
    
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([patient_id, name, age, gender, diagnosis, medication, doctor, notes, timestamp])
    
    with open(AUDIT_LOG, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Record Added", patient_id, timestamp])
    
    messagebox.showinfo("Success", "Patient Record Saved Successfully!")
    clear_entries()

# Function to clear entry fields
def clear_entries():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("Select")
    diagnosis_var.set("Select")
    medication_var.set("Select")
    doctor_entry.delete(0, tk.END)
    notes_entry.delete("1.0", tk.END)

# GUI Setup
root = tk.Tk()
root.title("EHR Simulation - Mock Data Entry")
root.geometry("400x550")

# Labels and Entry Fields
tk.Label(root, text="Patient ID (Auto-generated if left blank):").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Gender:").pack()
gender_var = tk.StringVar(root)
gender_var.set("Select")
gender_dropdown = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female", "Other"])
gender_dropdown.pack()

tk.Label(root, text="Diagnosis:").pack()
diagnosis_var = tk.StringVar(root)
diagnosis_var.set("Select")
diagnosis_dropdown = ttk.Combobox(root, textvariable=diagnosis_var, values=["Hypertension", "Diabetes", "Asthma", "Migraine", "High Cholesterol"])
diagnosis_dropdown.pack()

tk.Label(root, text="Medication:").pack()
medication_var = tk.StringVar(root)
medication_var.set("Select")
medication_dropdown = ttk.Combobox(root, textvariable=medication_var, values=["Lisinopril", "Metformin", "Albuterol", "Sumatriptan", "Atorvastatin"])
medication_dropdown.pack()

tk.Label(root, text="Doctor:").pack()
doctor_entry = tk.Entry(root)
doctor_entry.pack()

tk.Label(root, text="Notes:").pack()
notes_entry = tk.Text(root, height=4, width=40)
notes_entry.pack()

tk.Button(root, text="Save Record", command=save_data).pack(pady=5)
tk.Button(root, text="Clear", command=clear_entries).pack()

root.mainloop()
