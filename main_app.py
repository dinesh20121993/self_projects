from db_access import get_user_data
from flask import Flask, render_template

app = Flask(__name__)
table_headings = ("ID", "Name", "Email", "Age", "Gender", "User_name", "Password", "Address")
table_data = get_user_data()

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/table/")
def table_display():
    return render_template("table.html", table_headers = table_headings, data = table_data)

if __name__ == "__main__":
    app.run(debug=True)