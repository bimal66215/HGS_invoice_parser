# Importing the necessary modules

import cv2
import pytesseract
import re
import os
import pandas as pd

# Getting the path for the Tesseract.exe file.

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# Creating a Emprty DataFrame with the Columns "file_name", "Date", "Due_Date", "Balance_Due"

df = pd.DataFrame(columns=["file_name", "Date", "Due_Date", "Balance_Due"])

# Looping through the files in the current project directory except main.py and .idea

for file_name in os.listdir():
    if file_name not in ["main.py",".idea"]:

        # Reading the image

        image = cv2.imread(file_name)

        # Getting the Textual Data from the Image using the Tesseract OCR engine.

        text = pytesseract.image_to_string(image,lang='eng')

        # Creating the Regex pattern to extract Date, Due Date and Balance Due.

        date_pattern = re.compile(r'(?<!Due\s)Date:\s[a-zA-z]{3}\s\d{2},\s\d{4}')
        Due_pattern = re.compile(r'(?<=Due\s)Date:\s[a-zA-z]{3}\s\d{2},\s\d{4}')
        Balance_Due_pattern = re.compile(r'(?<=Balance due:)\s\$\d+\.\d+')

        # Getting only the Date from the matched pattern in the text.

        date = date_pattern.findall(text)[0].split(': ')[1]
        due_date = Due_pattern.findall(text)[0].split(': ')[1]
        balance_Due = Balance_Due_pattern.findall(text)[0]

        # Creating a temporary dictionary to add files to the DataFrame

        dict = {
            "file_name": [file_name.rsplit('.',1)[0]],
            "Date" : [date],
            "Due_Date": [due_date],
            "Balance_Due": [balance_Due]
        }

        # Concating the current the df with dict Data to add row to the DataFrame 'df'

        df = pd.concat([df, pd.DataFrame(dict)])

# Resetting the index for the Datframe

df = df.reset_index()

# Displaying the Dataframe in the console
print(df)

# Saving the DataFrame as a Excel file with no index

df.to_excel("output.xlsx", index=False)







