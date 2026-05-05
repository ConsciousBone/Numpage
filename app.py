from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/button", methods=["POST"])
def handle_button():
    data = request.get_json()
    button_id = data.get("id")
    print(f"a button was pressed somewhere maybe with id {button_id}")
    if button_id == "0":
        print("wow it works!")
    return jsonify({"message":"success?"})

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", error = error), 404