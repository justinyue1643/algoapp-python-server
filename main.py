from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():
    return "hello world"


@app.route("/proto", methods=["GET"])
def proto() -> str:
    string = "def hello():\n\treturn \"hello\""
    print(string)
    exec(string)
    output = eval("hello()")

    return output


@app.route("/run", methods=['GET'])
def run_python_code() -> None:
    setup_code = request.args.get("setup_code")
    runnable_code = request.args.get("runnable_code")

    exec("exec(" + repr(setup_code).replace("\\", "0").replace("00", "\\") + ")")
    output = eval(runnable_code)

    response = {
        "output": output
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
