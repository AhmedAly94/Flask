from flask import Flask, render_template, request, url_for

app = Flask(__name__) #object

#main route
@app.route("/")
def main():
   return render_template("index.html")

@app.route("/simple")
def simple():
    return render_template("simple.html")

@app.route("/calculate",methods = ["post"])
def calculate():
    first_number= int(request.form["firstNumber"])
    operation=request.form["operation"]
    second_number=int(request.form["secondNumber"])

    if operation == "plus":
        result = first_number + second_number
    elif operation == "minus":
        result = first_number - second_number
    elif operation == "multiply":
        result = first_number * second_number
    elif operation == "divide":
        result = first_number / second_number
    else:
        return "try again"
    return render_template("simple.html",result = result)

if __name__ == "__main__":
    app.run(debug=False)