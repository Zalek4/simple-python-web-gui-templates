# A Note on Web GUI's For Python.
Python is an incredible language. It has a simple syntax, an insane amount of available modules, and an excellent amount of free learning material on the web. Even still, it's suprisingly challenging to find a simple, no frills guide on how to use web languages as a frontend for Python-driven desktop apps.

Hopefully, this template and this readme can help some folks get started. The link between a web frontend and a Python backend is suprisingly simple, and you don't need Electron or similar alternatives to do it (but you can totally use those if you want to).

___
I AM NOT A PROFESSIONAL PROGRAMMER, AND SOME EXPLAINATIONS BELOW MAY BE INACCURATE/SLIGHTLY WRONG. 
___

# Why Not Use PyQT? Tkinter? Kivy?
I'm an artist by trade, so I like pretty things. While the above options don't look bad, HTML, CSS and Javascript give me a level of design control that I desire. If you don't need any of that, then I can't recommend something like PyQT, Tkinter or Kivy enough!

# FastAPI
This has quickly become my go-to for any new Python GUI I need to make. It's simple, fast (duh), and I like that Pydantic is integrated with it.

### Uvicorn
FastAPI is capable of running asyncronous commands, which means Flask won't work as well in this case. Uvicorn uses ASGI standards, which means it's very fast. ASGI stands for Asynchronous Server Gateway Interface.
- [ASGI specifications](https://www.uvicorn.org/#the-asgi-interface)
- [Why ASGI?](https://www.uvicorn.org/#why-asgi)
- [Other ASGI solutions](https://www.uvicorn.org/#alternative-asgi-servers)

In our case, we're not getting too into the weeds with it to get a basic server running that we can connect to with Pywebview. The code below is all you need. 
- First, we create an event tracker. This will let us kill the Uvicorn server when we close our main program.

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
And that's it! Running this code will create a server that we can send requests to in order to pass Python to and from our frontend GUI.

### Pywebgui
Pywebgui is awesome, and can actually be used without Uvicorn and FastAPI to do pretty much exactly the same thing. In this case we've bypassed that functionality in favor of ASGI/speed. I've found the desktop app implementation of Pywebview is visually cleaner and faster than other options like Flaskwebgui (which is also awesome and can be used with FastAPI/Uvicorn if that's your jam), so that's why I've chosen to run it in my templates.

It's crazy easy to start up a window.
- First, we need to define our app as a FastAPI instance.
```python
# main.py

# Define the FastAPI app
app = FastAPI()
```
- Second, we need to start the desktop app with the same address:port as our Uvicorn server. We'll add this to our 'if __name__ == "__main__"' check at the bottom of main.py. We also place some logic at the bottom of this if statement to update our stop event when the windows closes, which will kill our Uvicorn server.
```python
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