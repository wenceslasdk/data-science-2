# Data Science 2 – NMFP436
Lectures: Václav Kozmík, Ondřej Týbl
Practicals: Karel Kozmík, Ondřej Týbl

This repository contains materials to the Data Science 2 - NMFP436 course.

## Practicals plan

| Date | Topic | Lecturer |
| -------- | ------- | ------- |
| TODO | Intro + Git    | Karel
| TODO | Python Intro | Karel
| TODO | Data Science Basics I | Karel
| TODO | Data Science Basics II | Karel
| TODO | Decision Trees I | Karel
| TODO | Decision Trees II | Karel
| TODO | Decision Trees III | Karel
| TODO | Neural Networks I | Ondřej
| TODO | Neural Networks II | Ondřej
| TODO | Neural Networks III | Ondřej
| TODO | Neural Networks IV | Ondřej
| TODO | Hyperparameters Optimization | Ondřej 
| TODO | University Holiday | no practicals
| TODO | Clustering | Ondřej

To receive the course credit, students must successfully work out two home assignments, 
one will be focused on decision trees and the other one on neural networks. 
There are only two assignments, but they will be complex and require considerable amount of work. 
Details will be published later in the semester.

## How to set-up your python environment

The following instructions will guide you to set-up everything needed to run the course code. Long story short, we use virtual environment managed by poetry running on python3.10 to install all dependencies from the lock file provided.

### 1) Install PyCharm Professional

- TODO

### 2) Get the course repository

- fork the repository e.g. by clicking 'Fork' on the repository page [repository page], use the default 'data-science-2' name for your version of the repository
- clone the new directory into your chosen destination, e.g. I opened command line/terminal and typed (the first line contains path to the directory where to place the new repository and 'ondratybl' is my GitHub name)
```sh
cd C:\Users\tyblondr
git clone https://github.com/wenceslasdk/data-science-2.git
```
- in my example the course repository would be
```sh
C:\Users\tyblondr\data-science-2
```

### 2) Create project

- open PyCharm and click 'New Project'
- set 'Name' to 'data-science-2' and 'Location' to the parent directory of your cloned repository from 2), i.e. in the example above we would set 'Location' to '\Users\tyblondr'
- choose 'Python version' as 'Python 3.10.9' (will be downloaded and installed if it does not exist yet on your computer)
- click 'Create' and choose 'Create from Existing Resources' if you are asked 

### 3) Install dependencies

- open Terminal in PyCharm (one of the icons in the left-down corner)
- install poetry by typing
```sh
pip install poetry
```
- install remaining packages using poetry (we use --no-root to indicate that the environment itself already exists)
```sh
poetry install --no-root
```

**_Note for Conda Users:_** If you are using conda on your system, it will probably happen that your PyCharm terminal will be always opened with both base and the project virtual env being activated. This should not be a problem but we advice to    double-check that 'which python' points to the python within the project and not the one in your conda installation.

TODO: 1) aby to fungovalo bez warnings, tak poetry.lock by vůbec neměl bejt v tom github repo protože ten lock by se měl pak vytvářet ideálně až lokálně, protože je hodně system-specific 2) můžeš to pak vyzkoušet i na win? nemělo by to fungovat tipuju protože jsem neřešil ty system-specific packages v pyproject.toml, takže asi bude potřeba něco z toho file vyhodit, klidně můžem probrat spolu 3) mohl bys prosím projít svoje cvika, že ten kód funguje? neprocházel jsem to celé
