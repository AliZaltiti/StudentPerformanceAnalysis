import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

print(df.head())
print(df.info())

print("Number of students:", df.shape[0])
print("Average final grade (G3):", df["G3"].mean())

gender_avg = df.groupby("sex")["G3"].mean()
print(gender_avg)

gender_avg.plot(kind="bar")
plt.title("Average Final Grade by Gender")
plt.xlabel("Gender")
plt.ylabel("Average G3")
plt.show()

plt.scatter(df["absences"], df["G3"])
plt.title("Absences vs Final Grade")
plt.xlabel("Absences")
plt.ylabel("Final Grade (G3)")
plt.show()

study_avg = df.groupby("studytime")["G3"].mean()
print(study_avg)

study_avg.plot(kind="line", marker="o")
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time Level")
plt.ylabel("Average G3")
plt.show()

parent_edu = df[["Medu", "Fedu", "G3"]]
print(parent_edu.corr())
