# Spam-Mail-Detector
This is a ML project using scikit learn logistic regression training model that detects whether a given mail is a spam mail or not. 
# How to use the Pyhton script
Make sure that you have numpy, pandas and scikit learn libraries already installed in your system. 
Make sure that the csv file is in the same folder where the script is there.
<br>
NOTE- to install these, make sure you have pip installed, to check- <br>
1. Open cmd
2. Type pip --version and hit ENTER
3. If a version is there, you are good to go!
<br>
Next you have to install these libraries mentioned above.
<br>
Next, after you run the script, it asks for a prompt. <br>
## Guidelines for the prompt you will enter
1. Try to keep it short.
2. Only text is accepted.
3. Pick any mail from the already give 'mail_data.csv' file. This will surely give you appropriate results.

# How to use the pyhton notebook
Run all cells one by one and make sure that the .csv file is in the same folder. 
1. In the last cell, there is the function to check an email. Run it. Follow the same steps in "Guidelines for the prompt you will enter".

# Model explanation and Future Steps
This model works on logistic regression with feature vectorization techniques. <br>
The data set is added, cleaned, extracted, converted, supplied and finally updated based on the performance of the model. <br>
As far as accuraccy of the model is concerned, we use a accuraccy checker to evaluate the performance of the model. It's current accuraccy is 96.5% <br>
## Future steps
1. Add more features into the existing model to refine the data training and the execution.
2. Try and test L1 and L2 regularization techniques.
3. Fine-tune the model with different parameters.
4. Incorporate more models like random forest, svm or neural networks
5. Convert this feature into a Django web app. 
