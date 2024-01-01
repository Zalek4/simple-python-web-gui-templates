# FastAPI
From the FastAPI [website](https://fastapi.tiangolo.com/):

*FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.*

While Flask is much more popular, FastAPI is the meatier of the two.

### Uvicorn
Uvicorn is the the server we'll be using to run our FastAPI app. FastAPI is capable of running asyncronous commands and, since Uvicorn uses ASGI standards, they're excellent paired together. For those who don't know, ASGI stands for Asynchronous Server Gateway Interface.

Some additional reading for those interested:
- [ASGI specifications](https://www.uvicorn.org/#the-asgi-interface)
- [Why ASGI?](https://www.uvicorn.org/#why-asgi)
- [Other ASGI solutions](https://www.uvicorn.org/#alternative-asgi-servers)

In our case, we're not getting too into the weeds to get a basic server running that we can connect to with Pywebview. The code below is all you need. 

All of our imports for the 'main.py' file:
```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from threading import Event, Thread
import uvicorn
import webview
```

- First, we create an event tracker. This will let us kill the Uvicorn server when the main window of our program exits.

```python
# main.py

# This is an event tracker we're using to kill the uvicorn server when the app gets closed
stop_event = Event()
```
- Second, we create a function to run the Uvicorn server.
```python
# main.py

# Run the uvicorn server
def run_server():
	while not stop_event.is_set():
		uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=False)
```
- Third, we run the function with the Threading module, which allows us to run the Pywebview window immediately after. If we don't start the Uvicorn server like this, the program will never move past the run_server() function, and no window will be created.
```python
# main.py

if __name__ == "__main__":
	# Start a thread to run the uvicorn server before we try to connect to it with pywebview
	t = Thread(target=run_server)
	t.daemon = True # this makes it so the server shuts down when the main program exits
	t.start()
```
And that's it! Running this code will create a server that we can send requests to in order to pass data to and from our frontend GUI.

### Pywebview
[Pywebview](https://pywebview.flowrl.com/) is awesome, and can actually be used without Uvicorn and FastAPI to do pretty much exactly the same thing. In this case we've bypassed that functionality in favor of ASGI/speed. 

I've found the desktop app implementation of Pywebview is visually cleaner and faster than other options like Flaskwebgui (which is also awesome and can be used with FastAPI/Uvicorn if that's your jam), so that's why I've chosen to run it in some of these templates.

It's super easy to start up a window.
- First, we need to define our app as a FastAPI instance.
```python
# main.py

# Define the FastAPI app
app = FastAPI()
```
- Second, we need to start the desktop app with the same address:port as our Uvicorn server. We'll add this to our 'if __name__ == "__main__"' check at the bottom of main.py. We also place some logic at the bottom of this if statement to update our stop event when the windows closes, which will kill our Uvicorn server.
```python
# main.py

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
```

And that's it! We now have a Python script that will open a local server, and run a desktop window connected to it. Now we can add add HTML content to our new app.

- First, we have to tell FastAPI where we keep the rest of our app, since it won't look in our package folder by default. We're also going to be using Jinja2 to set up our HTML pages as templates that FastAPI can use.
```python
# main.py

# Get the directory for all of our html page templates, and mount our path to the 'static' folder.
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
```

- Second, we need to create a method to handle each page we want to display. In this case, we're displaying a loading page for 3 seconds, and then we're loading our main app page. The 3 second delay is handled in the javascript file attached to 'loading.html'.
```python
# main.py

# Loading page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
	return templates.TemplateResponse("loading.html", {"request": request})

# Home page
@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
	return templates.TemplateResponse("index.html", {"request": request})
```
```javascript
// loading_script.js

// This creates a timer of 3 seconds. The loading screen will play for that duration, and then load the main program.

let count = 3;
const timer = setInterval(function() {
    count--;
    console.log(count);
    if (count === 0) {
    clearInterval(timer);
    console.log("Time's up!");
    switchPage()
    }
}, 1000);

function switchPage() {
    document.location.href = '/home';
}

```
```html
<!---loading.html-->

<link rel="stylesheet" href="/static/gui/loading.css">
```
Notice the *'@app.get("/", response_class=HTMLResponse)'* decorator for each of the pages in the Python code. The first argument passed to these (in this case "/", which is the root directory) is the "web" link our local frontend will connect to our backend through.

A more basic decorator/function pair can look like this one from the official docs:
```python
@app.get("/hello-world")
def hello_world():
    return {"message": "Hello World"}
```
This creates a function that will be run when the frontend sends a 'get' request to the '/hello-world' address of our application. These can also be run asyncronously in FastAPI with the 'async' function tag:
```python
@app.get("/hello-world")
async def hello_world():
    return {"message": "Hello World"}
```
And that's it for this quick guide! There's a *ton* more you can do with FastAPI, and I would encourage anyone reading to check out the [official documentation](https://fastapi.tiangolo.com/learn/) for more.