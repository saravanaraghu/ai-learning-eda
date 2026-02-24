import pandas as pd
import os
os.chdir(
    r"C:\Users\RaghuswamySaravana.A\projects\ai-learning-eda"
    )
df = pd.read_csv("employee_data_200.csv")
print(df.describe())