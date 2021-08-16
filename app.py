from flask import Flask, request, jsonify, Response, make_response

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return "hello world"


@app.route("/proto", methods=["GET"])
def proto() -> str:
    string = "def hello():\n\treturn \"hello\""
    print(string)
    exec(string)
    output = eval("hello()")

    return output


@app.route("/run", methods=["GET"])
def run_python_code() -> Response:
    setup_code = request.args.get("setup_code")
    runnable_code = request.args.get("runnable_code")
    print(f"setup_code: \n{setup_code}\n\n")
    print(f"runnable_code: \n{runnable_code}\n\n")

    try:
        exec("exec(" + repr(setup_code).replace("\\", "0").replace("00", "\\") + ")")
        output = eval(runnable_code)
    except Exception as e:
        print(e)
        response = make_response(
            jsonify({"error": str(e)}),
            400
        )

        return response
    else:
        response = make_response(
            jsonify({"output": output}),
            200
        )

        return response


if __name__ == "__main__":
    app.run()
