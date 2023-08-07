#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as sklearn
from flask import Flask, render_template
with open (r'C:/Desktop/Language_Detection.csv', encoding = 'utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'\tColumn names are {" ".join(row)}')
            print('\n\n')
            line_count += 1
        else:
             print(f'\t{row[0]} language = {row[1]} \n\n')
             line_count += 1
df = pd.read_csv(r'C:/Desktop/Language_Detection.csv')
X = df.iloc[100:, :-1]
y = df.iloc[100:, -1]
X_train, X_test, y_train, y_test = sklearn(X, y, test_size=0.05, random_state=0)
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
from flask import request
# import the necessary language detection functions and ML model

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
    return render_template('index.html', language=language)
    return render_template('index.html')


# In[ ]:




