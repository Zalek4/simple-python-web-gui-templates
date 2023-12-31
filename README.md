*THIS REPO IS A WORK IN PROGRESS*
# A Note on Web GUI's For Python.
Python is an incredible language. It has a simple syntax, an insane amount of available modules, and an excellent amount of free learning material on the web. Even still, it's suprisingly challenging to find a simple, no frills guide on how to use web languages as a frontend for Python-driven desktop apps.

Hopefully, this template and this readme can help some folks get started. The link between a web frontend and a Python backend is suprisingly simple, and you don't need Electron or similar alternatives to do it (but you can totally use those if you want to).

___
I AM NOT A PROFESSIONAL PROGRAMMER, AND SOME EXPLAINATIONS BELOW MAY BE INACCURATE/SLIGHTLY WRONG. 
___

# Templates in This Repository
- FastAPI
- Flask (WIP)
- Python-webui (WIP)

# Why Not Use PyQT? Tkinter? Kivy?
I'm an artist by trade, so I like pretty things. While the above options don't look bad, HTML, CSS and Javascript give me a level of design control that I desire. Web browsers are also incredibly powerfult tools, and bring a level of professionalism to your projects. They're stable, well tested, and well documented.

# The Anatomy of a Web-based Python Desktop App
The structure is fairly simple, and is composed of 3 parts.
- Backend (Python)
    - This is all of our code that does stuff. In this case, I've organized all of this logic in the '/static/engine' directory, as well as the 'main.py' file in the '/fastapi' directory.
- Frontend (HTML, Javascript and CSS)
    - This is everything the user sees and touches. Buttons, text inputs, graphs, you name it.
- Server
    - This handles ferrying data between the frontend and the backend. This can have different levels of visibility depending on the module you're using. Example - Python-webgui allows direct binding of Python functions to HTML elements, whereas FastAPI requires you serve the result of Python functions as JSON data. There is no right or wrong answer here - it all has to do with what your needs/preferences are.