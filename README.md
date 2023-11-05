# first_webScrapping
This is my first approach to Web Scrapping concept

***

Everyting runs on Ubuntu 22.04.3 LTS (GNU/Linux 5.15.90.1-microsoft-standard-WSL2 x86_64).

## How to:

Make sure to have python Virtualenv installed.

To activate environment: `source env/bin/activate` on your terminal (inside this repository).

Then to install required packages: `pip install -r requirements.txt`

Important: to implement data base insertion through mysql connection it is necessary to open "librosDB.sql" file and execute. It'll create Data Base and tables which are used to make the insertion of the data scrapped.

## General view:

There is two parts of the same exercise.

Notebook main.ipynb contains the step-by-step approach.

For the second part, scrapping_script.py was added. It contains the automatic data insertion into a Local MySQL Data Base.