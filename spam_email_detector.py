#importing all the dependencies for the project
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Loading data from a csv file to a pandas dataframe
raw_mail_data = pd.read_csv("./mail_data.csv")

"""Now we clean this raw data that contains null values to clean the data."""

# Replace all null values with a null string ''
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)), '')
mail_data

#print(mail_data.isna().sum().sum()) #this will count the no. of null values in the dataframe

#mail_data.shape

"""Label Encoding"""

# label spam mail as 0;  ham mail as 1;

mail_data.loc[mail_data['Category'] == 'spam', 'Category',] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category',] = 1

#print(mail_data)

"""Train-Test split- dividing the given data into two sub parts in which 1 is used to train and the other is used to evaluate the model."""

# separating the data as texts and label

X = mail_data['Message']

Y = mail_data['Category']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

"""Now we have our train-test split and the next step is to convert the data into numbers so that the model can understand. This will be done via vectors that will transform text data into numbers format. This is called feature extraction."""

# transform the text data to feature vectors that can be used as input to the Logistic regression

feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english', lowercase=True)

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

# convert Y_train and Y_test values as integers

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

#print(X_train_features)



model = LogisticRegression()

model.fit(X_train_features, Y_train)


predicted_on_train_data = model.predict(X_train_features)
accuracy_on_train_data = accuracy_score(Y_train, predicted_on_train_data)
#print(accuracy_on_train_data)

# Now we test our model on the basis of test data 
predicted_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test, predicted_on_test_data)
#print(accuracy_on_test_data)


def SpamOrHam(input_mail_by_user) : 
  input_mail_string = [input_mail_by_user]
  input_mail = input_mail_string
  input_mail_features = feature_extraction.transform(input_mail)
  prediction_result = model.predict(input_mail_features)
  if (prediction_result==0):
    print("This mail is a spam mail")
  else: 
    print("This mail is a ham mail")
x = input("Enter a mail :")
SpamOrHam(x)

