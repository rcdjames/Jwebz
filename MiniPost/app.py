import os
from datetime import datetime
from flask import Flask, request, jsonify, json, render_template


'''
Version 1.0
8/09/2024
A basic Flask web app that saved POST data on file in plain text.


'''


app = Flask(__name__)


APP_DATA_STORE = "store.txt" # where to store POST request data to file
APP_DEBUG_MODE = True # debug mode for development only
APP_LISTEN_INTERFACE = "0.0.0.0"
APP_PORT = 5001
APP_RETURN_HTML = True # render view route as JSON or HTML


@app.route("/", methods=["GET"])
def index():
    # reject if file store cannot be found
    if not os.path.exists(APP_DATA_STORE):
        return jsonify({"error":"There is no data to return"}), 500
    # attempt to read data store file
    try:
        with open(APP_DATA_STORE, 'r') as store:
            record_total = len(store.readlines())
        return render_template("index.html", total=record_total)
    except Exception as error:
        # unable to process this request
        return jsonify({"error":str(error)}), 500


@app.route("/view", methods=["GET"])
def view():
    # reject if file store cannot be found
    if not os.path.exists(APP_DATA_STORE):
        return jsonify({"error":"There is no data to return"}), 500
    # attempt to read data store file
    try:
        with open(APP_DATA_STORE, 'r') as store:
            view_store = []
            for line in store.readlines():
                view_store.append(line)
            if APP_RETURN_HTML:
                return "<br>".join([line.strip() for line in view_store]) # return data store as HTML
            else:
                return jsonify({"store":view_store}) # return data store as JSON
    except Exception as error:
        # return error unable to process request
        return jsonify({"error":str(error)}), 500


@app.route("/submit", methods=["POST"])
def submit():
    content_type = request.headers.get('Content-Type') # check Content-Type is correct
    if (content_type == 'application/json'):
        data = request.get_json() # convert POST data into JSON format
        if data is None:
            return jsonify({"error": "No JSON data provided"}), 400
        ts = datetime.now().strftime("%c")
        data.update({"timestamp":ts}) # append basic timestamp from local time to request
        # append POST data to file
        with open(APP_DATA_STORE, "a") as store:
            store.write(json.dumps(data) + "\n")
        print(f"A new POST request was recieved {ts} - {request.content_length} bytes") # log POST to console
        return jsonify({"message":"POST data saved successfully"}), 200 # POST request success and saved to file
    else:
        return jsonify({"error":"Content-Type is not supported. Must be application/json"}), 400 # POST request is rejected due to bad Content-Type


if __name__ == "__main__":
    app.run(host=APP_LISTEN_INTERFACE, port=APP_PORT, debug=APP_DEBUG_MODE)
