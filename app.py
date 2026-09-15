#step 1: Load Important modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
import streamlit as st
# this streamlit is for web based application projects

# Web page code
st.title(" HEALTH INSURANCE COMPANY")
img_url = "https://www.investindia.gov.in/team-india-blogs/overview-insurance-industry-india"
st.image(img_url)

#  lOAD DATA  and  ML MODEL PART
url = "https://raw.githubusercontent.com/ankitmisk/UIT-data/refs/heads/main/Insurance.csv"
df = pd.read_csv(url)

# step 3: EDA : Exploratory data analysis
df.drop("Customer_ID", axis = 1 , inplace = True)

df["Previous_Insurance"] = df['Previous_Insurance'].map({'Yes': 1, 'No': 0})
df["Insurance_Bought"] = df['Insurance_Bought'].map({'Yes': 1, 'No': 0})
# To get top 5 row data

# step 4: Divide dataset info features and target
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

#step 5: Divide data into Training & testing part
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# step 6 : Train Model
model = LogisticRegression()
model.fit(X_train, y_train)   

#show data sample
show data sample 
st.write(df.head())

# Create side bar for user input form
st.sidebar.title("fill customer Details")
st.sidebar.image(img_url)

for index, col_name in enumerate(X.columns):
  min_v = X[col_name].min()
  max_v = X[col_name].max()
  if col_name != "Previous_Insurance":
      value = st.sidebar.slider(f"select value for {col_name}",
                            min_value = min_v,
                            max_value = max_v)
else:
  value = st.sidebar.number_input(f"select value for {col_name}(0:No, 1:yes):")

all_ans.append(value)

ud = {j:all_ans[i] for i,j in enumerate(X.columns)}
user.df = pd.Dataframe(ud, index = [1])
st.write(user_df)

#==================Predicion==============
if st.button("Click to predict"):
  with st.spinner("Predicting.."):
    import time
    time.sleep(2)
    final_ans = model.predict([all_ans]) [0]
    if final_ans == 0:
    st.info("❎Customer will not buy the insurance❎")
else:
  st.success("✅Customer will buy the insurance✅")
               



