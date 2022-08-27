import pandas as pd
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("D:\STEM\Hackathon\Git\CotCare\Data.csv")

X = df[["Month", "Temp"]]
y = df["Full?"]

clf = GaussianNB() 
clf.fit(X, y)

#Pickle
import joblib
joblib.dump(clf, "D:\STEM\Hackathon\Git\CotCare\clf.pkl")