from flask import Flask, render_template, request, send_file
import os

from sales_forecast import create_chart, CHART_FILE

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    months = [
        "jan","feb","mar","apr",
        "may","jun","jul","aug",
        "sep","oct","nov","dec"
    ]

    sales = []

    for month in months:

        value = request.form.get(month)

        if value.strip() != "":
            sales.append(int(value))

    if len(sales) < 2:
        return "Please enter at least 2 months of data."

    create_chart(sales)

    return send_file(CHART_FILE, mimetype="image/png")


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )