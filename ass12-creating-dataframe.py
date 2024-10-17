import pandas as pd

#load csv file into a dataframe
df=pd.read_csv("E:\\ Download\\business-financial-data-june-2024-quarter-csv.csv")

#identify categorical colums
categorical_colums=df.select_dtypes(include=['object']).columns

#Perform one-hot encoding
df_encoded=pd.get_dummies(df,columns=categorical_colums)
print(df_encoded)


# The program loads a CSV file.
# It identifies the categorical columns in the DataFrame.
# It then transforms these categorical columns into numeric columns using one-hot encoding, making the data suitable for use in machine learning algorithms.