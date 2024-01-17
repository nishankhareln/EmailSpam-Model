This is a model developed using logistic regression which is a supervisied Machine learning.Here we have trained our model using different labelled dataset to check whether the given mail / email is spam or not.If it is spam it show
it is sapm otherwise it is not spam. we have use import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer #for converting text data to numerical values
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

such type of libraries used here. We have used Tfid Vectorizer for converting text data to numerical values.
