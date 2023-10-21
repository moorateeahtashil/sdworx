import prediction
from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predictor')
def predictor():
    return render_template("predictor.html")

@app.route('/prediction', methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return "Kindly fill out the form and then click the Predict button to get the prediction!"

    if request.method == "POST":
        empid = request.form.get("empid")
        satisfaction = request.form.get("satisfaction")
        evaluation = request.form.get("evaluation")
        project = request.form.get("projects")
        hours = request.form.get("hours")
        time = request.form.get("years")
        accident = request.form.get("accident")
        promotion = request.form.get("promotion")
        department = request.form.get("department")
        sal = request.form.get("salary")

        # results = prediction.predict(satisfaction, evaluation, project, hours, time, accident, promotion, department, sal)
        results = random.choice([True, False])


        a = "Prediction - The Employee Will Leave the Company." if results else "Prediction - The Employee Will Not Leave the Company."
        accident_str = "Yes" if int(accident) else "No"
        promotion_str = "Yes" if int(promotion) else "No"

        department_mapping = {
            "accounting": "Accounting",
            "hr": "HR",
            "IT": "IT",
            "management": "Management",
            "product_mng": "Product Management",
            "RandD": "R & D",
            "sales": "Sales",
            "support": "Support",
            "technical": "Technical"
        }
        department_str = department_mapping.get(department, department)

        sal_mapping = {
            "low": "Low",
            "medium": "Medium",
            "high": "High"
        }
        sal_str = sal_mapping.get(sal, sal)

        return render_template("prediction.html", x=results, y=a, a1=satisfaction, a2=evaluation, a3=project, a4=hours,
                               a5=time, a6=accident_str, a7=promotion_str, a8=department_str, a9=sal_str, a10=empid)

if __name__ == "__main__":
    app.run()
