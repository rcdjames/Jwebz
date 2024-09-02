from flask import Flask, request, render_template
import json


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")

@app.route("/post_json", methods=["POST"])
def post_json():
	content_type = request.headers.get('Content-Type')
	if (content_type == 'application/json'):
		j = request.get_json()
		#for k, v in j.items():
		#	print("k=",k,"v=",v)

		print(j["thumbnail"]["url"])
		return "OK"
	else:
		return 'Content-Type not supported!'


if __name__ == "__main__":
	app.run("0.0.0.0", port=5001)

