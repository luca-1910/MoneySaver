from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            # Extract inputs
            day = int(request.form["day"])
            month = int(request.form["month"])
            year = int(request.form["year"])
            goal_amount = float(request.form["amount"])

            today = datetime.today()

            # Validate and adjust year
            if 25 <= year <= 99:
                year = 2000 + year
            elif year < 2025:
                raise ValueError("Year must be 2025 or later.")

            # Create date object
            save_date = datetime(year, month, day)

            # Check if date is in the future
            if save_date <= today:
                raise ValueError("Date must be in the future.")

            # Weeks remaining
            weeks_remaining = round((save_date - today).days / 7)

            if goal_amount <= 0:
                raise ValueError("Amount must be more than $0")

            weekly_saving = round(goal_amount / weeks_remaining)

            result = {
                "save_date": save_date.strftime("%d-%m-%Y"),
                "weeks_remaining": weeks_remaining,
                "goal_amount": goal_amount,
                "weekly_saving": weekly_saving
            }

        except ValueError as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
