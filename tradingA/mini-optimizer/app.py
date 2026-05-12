from flask import Flask, render_template, request
from optimizer import run_optimizer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        numbers = request.form.get("numbers")
        try:
            numbers = [float(x) for x in numbers.split(",")]
            result = run_optimizer(numbers)
        except Exception as e:
            result = f"Error: {e}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
