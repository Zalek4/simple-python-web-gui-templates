# A Note on Web GUI's For Python.
Python is an incredible language. It has a simple syntax, an insane amount of available modules, and an excellent amount of free learning material on the web. 

Even still, it's been suprisingly challenging to find a simple, no frills guide on how to use web languages as a frontend for Python-driven desktop apps. The best one I've come across is by [Will Tejeda](https://www.youtube.com/watch?v=5HSz9EVEstI&t=465s&ab_channel=WillTejeda) - thanks for your straight forward content Will!

This repository is for anyone sick of reading Medium articles that only give you 75% of the information you need to understand what's going on with this stuff. Hopefully, these templates and guides can help some folks get started. 

The link between a web frontend and a Python backend is suprisingly simple, and you don't need Electron or similar alternatives to do it (but you can totally use those if you want to).

___
***I AM NOT A PROFESSIONAL PROGRAMMER, AND MY UNDERSTANDING OF THESE TOOLS ISN'T PERFECT. SOME OF THE EXPLAINATIONS IN THIS REPOSITORY MAY BE INACCURATE/SLIGHTLY WRONG.***
___

# Why Not Just Use Something Like PyQT, Tkinter or Kivy?

I'm an artist by trade, so I like pretty things. While the above options don't look bad, HTML, CSS and Javascript give me the level of design control that I desire. Web browsers are also incredibly powerful tools, and bring a level of professionalism to your projects. They're stable, well tested, and well documented.

There are *many* modules like the the ones mentioned above that provide robust tools for creating user interfaces completely within Python. If you're looking for the least complicated solution, and aren't worried about granular visual control, then I absolutely recommend something like Tkinter or PyQT.

# Templates in This Repository
- FastAPI
- Flask (WIP)
- Python-webui (WIP)
- Flaskwebgui (WIP)
- Pywebview (WIP)

# Using These Templates
I recommend either copying the contents of each template into your main project folder, or opening the folder of each one you want to try in your IDE of choice. Some funkiness can occure with relative folder paths if you try to run any of these with this entire repo open.
- First, create a virtual environment in the folder of the template you're using. You can do this by running the following command after you've CD'd to your repo/project folder.
```bash
python -m venv venv
```
- Next, install the required modules using the included requirements.txt file in each template's folder. 
```bash
pip install -r requirements.txt
```
- Once everything is done installing, you should be able to run the examples by running the 'main.py' file from within your IDE.


# The Anatomy of a Web-based Python Desktop App
The structure is fairly simple, and is composed of 3 parts.
- Backend (Python)
    - This is all of our code that does stuff. In this case, I've organized all of this logic in the '/static/engine' directory, as well as the 'main.py' file in the main template folders. The 'main.py' file is the program entry point for each of these templates.
- Frontend (HTML, Javascript and CSS)
    - This is everything the user sees and touches. Buttons, text inputs, graphs, you name it.
- Server
    - This handles ferrying data between the frontend and the backend, and can have different levels of visibility depending on the module you're using. Example: Python-webui allows direct binding of Python functions to HTML elements, whereas FastAPI requires you serve the result of Python functions as JSON data. There is no right or wrong answer here - it all has to do with what your needs/preferences are.