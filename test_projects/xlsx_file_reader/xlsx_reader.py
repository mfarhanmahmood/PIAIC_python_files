import os
import pandas as pd

dirname = os.path.dirname(__file__)
relative_path = '.\\db\\PIAIC Islamabad Batch 3 Quarter 1 Final Grades_Results - Onsite.xlsx'
file_errors_location = os.path.join(dirname, relative_path)
df = pd.read_excel(file_errors_location)
roll_no = input("Enter your roll no. (PIAIC00000): ")
print(df.loc[df['Roll Number'] == roll_no.upper()])
