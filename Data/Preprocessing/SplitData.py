import pandas as pd
from sklearn.model_selection import train_test_split

input_df = pd.read_csv("Data_C.csv")

df = input_df[["stockcode", "roc", "ey", "label"]]

train, test = train_test_split(df, test_size=0.2, random_state=42, stratify=df[["label"]])

output_train_df = train.drop(columns=["stockcode"])
output_test_df = test.drop(columns=["stockcode"])

output_train_df.to_csv("Training_Data.csv", index=False)
output_test_df.to_csv("Test_Data.csv", index=False)
