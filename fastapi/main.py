import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import webview
from threading import Event, Thread
from fastapi.templating import Jinja2Templates

# This is an event tracker we're using to kill the uvicorn server when the app gets closed
stop_event = Event()

# Define the FastAPI app and window title
app = FastAPI()
app_title = "Lute"

# Get the directory for all of our html page templates, and mount our path to the 'static' folder.
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Loading page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
	return templates.TemplateResponse("loading.html", {"request": request})

# Home page
@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
	return templates.TemplateResponse("index.html", {"request": request})

# Run the uvicorn server
def run_server():
	while not stop_event.is_set():
		uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=False)

if __name__ == "__main__":
	# Start a thread to run the uvicorn server before we try to connect to it with pywebview
	t = Thread(target=run_server)
	t.daemon = True # this makes it so the server shuts down when the main program exits
	t.start()

	# Create our window with pywebview
	webview.create_window(app_title, "http://127.0.0.1:5000", resizable=True, maximized=True)
	webview.start(debug=True)

	# Tell uvicorn to stop
	stop_event.set()