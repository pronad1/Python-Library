# step 1: Import libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# step 2: Prepare Data
data={
    'Hours' : [2,4,6,8,10],
    'Attendance' : [70,80,78,85,90],
    'Passed' : [0,0,1,1,1]
}
df=pd.DataFrame(data)

x=df[['Hours','Attendance']]  #features
y=df['Passed']     #target

# Steps 3: Split into training & testing sets
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=0)

# Step 4: Train the model
model=LogisticRegression()
model.fit(x_train,y_train)

# Step 5: Predict
y_pred=model.predict(x_test)

# Step 6: Evaluate accuracy
print('Accuracy: ',accuracy_score(y_test,y_pred))

print('Intercept: ',model.intercept_)
print('Coefficients: ',model.coef_)

# model.predict([[5,80]])