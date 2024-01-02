from flask import Flask, render_template, jsonify, request
from threading import Event, Thread
import webview
import static.engine.functions as Functions

# This is an event tracker we're using to kill the uvicorn server when the app gets closed
stop_event = Event()

# Define the Flask app and window title
app = Flask(__name__)
app_title = "App Title"
host = "http://127.0.0.1"
port = 5000

# Loading page
@app.route("/")
def loading():
	return render_template("loading.html")

@app.route("/home")
def home():
	return render_template("index.html")

@app.route("/get", methods=['GET'])
def get_request():
	result = Functions.create_dictionary()
	return(result)

@app.route("/post", methods=['POST'])
def post_request():
	valueFromJavascript = request.get_json()
	print(f"This is from Javascript : {valueFromJavascript}")
	return(jsonify(valueFromJavascript))

# Run the uvicorn server
def run_server():
	while not stop_event.is_set():
		app.run(host=host.replace("http://", ""), port=port, use_reloader=False)

if __name__ == "__main__":
	# Start a thread to run the uvicorn server before we try to connect to it with pywebview
	t = Thread(target=run_server)
	t.daemon = True # this makes it so the server shuts down when the main program exits
	t.start()

	# Create our window with pywebview
	webview.create_window(app_title, f"{host}:{port}", resizable=True, maximized=True)
	webview.start(debug=True)

	# Tell flask to stop
	stop_event.set()