# ERLC FISHING

This is Script for Roblox [ERLC](https://www.roblox.com/games/2534724415/Emergency-Response-Liberty-County) (Emergency Response: Liberty County)

This code automates the fishing process generating passive money.

# Structure

- [Requirements](#requirements)
- [Setup Guide](#setup-guide)

## Requirements

- Windows 10/11 (tested on Win 11)
- Python 3.8+ ([Download](https://www.python.org/downloads/))
- Stable Frame Rate
- (Python Virtual Environment) - Recommended

## Setup-Guide

#### 1.1 Install Pyton ([Download](https://www.python.org/downloads/))

#### 1.2 Download the python file

Download -> [fishing.py](fishing.py)

Download -> [getpos.py](getpos.py)

#### 1.3 Create a Virtual Environment using Venv

```
python -m venv fishing-env #Create the Environment

fishing-env/bin/activate #Select the Environment
```

#### 1.4 Install all the Dependencies (Libaries)

<p>These Libaries are required to run the script. <br>
Install the following libaries using pip:</p>

```
pip install opencv-python numpy mss pynput pyautogui
```

your folder structure should now look like this

```
roblox-fishing-bot/
├── fishing.py       # Main automation script
├── getPos.py        # To get the position of the fishing rectangle
└── fishing-env/     # Folder for the Virtual environment
```

#### 2.1 Position yourself (IN GAME)

Your positioning is very important, your position should have the following properties:

- Corner, so you don't fall off. The Railing can be used for this
- The Character should **NOT** be in the the climbing state
- Move your camera so there is space for the cursor to be on the water
- Move the camera so in addition the floor is below the fishing rectangle

This is an example positioning
  ![Example positioning](../screenshots/fishing.png)

#### 2.2 Place rod

Place the fishing rod in **slot NR 8**

#### 2.3 Start casting

Position mouse and throw the fishing rod

#### 2.4 Run getPos.py

Now run the script getPos.py using the following command:

```
python getPos.py
```

This script will tell you when to place the cursor in the corners of the rectangle
You will have to copy and paste the output of the script into **Line 9** of the fishing.py script.
The output should look something like this: `monitor = {"top": 550, "left": 3000, "width": 200, "height": 340}`

#### 2.4 run the fishing script

to run the script execute the following command:

```
python fishing.py
```

This script will do all the clicking and rod casting for you

---

Made by ChatGPT and SparklingSausage (https://github.com/sparklingSausage) aka. Skill5791
