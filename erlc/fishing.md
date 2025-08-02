# ERLC FISHING

This is Script for Roblox ERLC (Emergency Response: Liberty County) Fishing

Made by ChatGPT and SparklingSausage (https://github.com/sparklingSausage) aka. Skill5791

## How the Fishing works:

A rounded rectangle appears on the right of the screen. It is red with a white area.
To catch the fish you have to bring the bar into the green area by clicking. Once the bar is inside the green area the character starts pulling.
This is done until the fish is directly in front of you. Then it is marked as fished and it's being equipped.

## Fishing mechanic Flowchart:

- Equip fishing rod
- aim at water and press
- catch fish by keeping bar in green area

## The script does the following:

When a fish is being caught it tracks the green area using the gray arrow right next to it (easier to track).
Then it tracks the white bar that has to stay in the green area.
It's spaming left click until the white bar is inside the green area.

## Script mechanic Flowchart:

- Track green area
- Click as needed
- once fish is caught (detected by dissapearing rectangle)
- press slot for fishing rod
- cast fishing rod again
- cycle restart

## How to Start:

- Equip the rod on slot NR. 8
- Position the character at a spot where it won't move [e.g. in the corner of the railing](screenshots/fishing.png)
- make sure below the area of the rectangle (red-green rectangle) isn't something that might trigger the color detection [(white or gray colors.)](screenshots/fishing.png)
- equip rod
- cast the rod
- start the script
- move mouse to a place where the fishing should be (water)
