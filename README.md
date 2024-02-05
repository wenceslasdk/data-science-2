# Data Science 2 – NMFP436
Lectures: Václav Kozmík, Marek Teller
Practicals: Karel Kozmík, Ondřej Týbl

This repository contains materials to the Data Science 2 - NMFP436 course.

## Practicals plan

| Date | Topic | Lecturer |
| -------- | ------- | ------- |
| 20.2 | Intro + Git    | Karel
| 27.2. | Python Intro | Karel
| 5.3. | Data Science Basics I | Karel
| 12.3. | Data Science Basics II | Karel
| 19.3. | Decision Trees I | Karel
| 26.3. | Decision Trees II | Karel
| 2.4. | Decision Trees III | Karel
| 9.4. | Neural Networks I | Ondřej
| 16.4. | Neural Networks II | Ondřej
| 23.4. | Neural Networks III | Ondřej
| 30.4. | Neural Networks IV | Ondřej
| 7.5. | Hyperparameters Optimization | Ondřej 
| 14.5. | University Holiday | no practicals
| 21.5. | Clustering | Ondřej

To receive the course credit, students must successfully work out two home assignments, 
one will be focused on decision trees and the other one on neural networks. 
There are only two assignments, but they will be complex and require considerable amount of work. 
Deatils will be published later in the semester.

## How to set-up your python environment

The following instructions will guide you to set-up everything needed to run the course code. Long story short, we use virtual environment managed by poetry running on python3.10 to install all dependencies from the lock file provided.

### 1) Get the course repository

- fork the repository e.g. by clicking 'Fork' on the repository page [repository page], use the default 'data-science-2' name for your version of the repository
- clone the new directory into your chosen destination, e.g. I opened command line/terminal and typed (the first line contains path to the directory where to place the new repository and 'ondratybl' is my GitHub name)
```sh
cd C:\Users\tyblondr
git clone https://github.com/ondratybl/data-science-2.git
```
- in my example the course repository would be
```sh
C:\Users\tyblondr\data-science-2
```

### 2) Install python

- specific python version 3.10 is needed, so follow even if you have already some other version
- to check what python version do you have on your computer (if any) type
```sh
where python
```
in command line on windows, or
```sh
which python
```
in terminal on linux/mac.

> Note: running `python --version` might give you just one of the versions if you have already more of them

- install python 3.10.9 by downloading [python for windows], [python for mac] or by using your package manager on linux and make sure that you select both

> Note: you may be asked during the installation if you want to install luncher for all users and if you want to add python.exe to PATH. We recommend doing so but it is not necessary for the steps below.

- check the path of your python installation as above (either 'where' or 'which' commands), you will get a list of paths and the correct one is the one containing python310, i.e. in my case the python.exe file is stored in

```sh
C:\Users\tyblondr\AppData\Local\Programs\Python\Python310
```

### 3) Create virtual environment

- open command line/terminal and navigate to the course directory, i.e. following my example in step 1) I would do
```sh
cd C:\Users\tyblondr\data-science-2
```
- create the virtual environment by (use your own path from step 2) instead of 'C:\Users\tyblondr\AppData\Local\Programs\Python\Python310')
```sh
C:\Users\tyblondr\AppData\Local\Programs\Python\Python310\python -m venv .venv
```

> Note: if you do not have any other python installation you do not need to specify the path above you simply type `python -m venv .venv` but we want to be sure that we use the correct version for compatibility

### 4) Create potry project

- activate the virtual environment by typing
```sh
.venv\Scripts\activate.bat
```
in command line on windows, or
```sh
source .venv\bin\activate
```
in terminal on linux/mac.
- install poetry by typing
```sh
pip install poetry
```
- install remaining packages using poetry (we use --no-root to indicate that the environment itself already exists)
```sh
poetry install --no-root
```
- close command line/terminal

### 5) Test

- the following procedure shall be repeated any time you want to work
- open command line/terminal and move to the course diretory as in step 3), i.e. in my example it would be
```sh
cd C:\Users\tyblondr\data-science-2
```
- activate the virtual environment by typing
```sh
.venv\Scripts\activate.bat
```
in command line on windows, or
```sh
source .venv\bin\activate
```
in terminal on linux/mac.
- open jupyter lab by
```sh
jupyter lab
```
- congratulations you have set-up project: its home repository is called data-science-2, its virtual environment is called .venv and it is located in a subdirectory (i.e. data-science-2/.venv)

   [repository page]: <https://github.com/wenceslasdk/data-science-2>
   [python for windows]: <https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe>
   [python for mac]: <https://www.python.org/ftp/python/3.10.9/python-3.10.9-macos11.pkg>
