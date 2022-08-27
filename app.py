from flask import Flask, request, render_template
import pandas as pd
import joblib


# Declaration
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle=
        clf = joblib.load("D:\STEM\Hackathon\Git\CotCare\clf.pkl")
        
        # Get input values
        Month = request.form.get("Month")
        Temp = request.form.get("Temp")
        
        # Put inputs to dataframe
        X = pd.DataFrame([[Month, Temp]], columns = ["Month", "Temp"])
        
        # Get prediction
        prediction = clf.predict(X)[0]
        
    else:
        prediction = ""
        
    return render_template("web.html", output = prediction)

# Run the app
if __name__ == '__main__':
    app.run(debug = True)