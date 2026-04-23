from flask import Flask, render_template, request

app = Flask(__name__)


def fizzbuzz(n: int) -> str:
    results: list[str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            results.append("Fizz Buzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return ", ".join(results)


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/fizzbuzz", methods=["POST"])
def calculate() -> str:
    raw = request.form.get("number", "")
    try:
        n = int(raw)
    except ValueError:
        return render_template("result.html", error="Enter a valid number.")
    if n < 1 or n > 20:
        return render_template("result.html", error="Number must be between 1 and 20.")
    return render_template("result.html", result=fizzbuzz(n))
