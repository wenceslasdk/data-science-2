# Data Science 2 – NMFP436
Lectures: Václav Kozmík, Ondřej Týbl, Karel Kozmík
Practicals: Karel Kozmík, Ondřej Týbl

This repository contains materials to the Data Science 2 - NMFP436 course.
## Lectures plan
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

## We use git to store all course files
- course repo: https://github.com/wenceslasdk/data-science-2
- What is Git and why we use it?
  - https://en.wikipedia.org/wiki/Git
  - Version control, collaboration (branches), backup

## How to set-up your python environment

The following instructions will guide you to set-up everything needed to run the course code. Long story short, we use virtual environment managed by poetry running on python3.10 to install all dependencies from the lock file provided.

### 1) Install PyCharm Professional and git

- go to: https://www.jetbrains.com/shop/eform/students
- fill in the form to get the license, you can use your @cuni.cz email or ISIC
- go to: https://git-scm.com/downloads
- install git

### 2) Set up GitHub
- Create an account 
- Create a fork of the course repo
  - https://docs.github.com/en/get-started/quickstart/fork-a-repo
  - A fork enables you to commit your own changes into your separate repo (not the shared one owned by teachers)

### 3) Get the course files - several options ordered by level of recommendation

#### 3.1) Use PyCharm integrated version control
- PyCharm has an integration to GitHub
- Click File -> Project from Version Control (or in the startup window you will see something like "Clone repository" or "VCS")
- Clone your repository by selecting it in the version control and create a project from this folder
- Do not clone the repository into a cloud folder! Use 'users/<me>/repos/data-science-2' foe example
- This will create a project without any Interpreter
- In the bottom right, click on the <No Interpreter>, select "Add New Interpreter" -> "Add Local Interpreter"
- Create a new virtual environment with Python 3.10 (if not present, it will be downloaded)

#### 3.2) Manually 
- Using the command line, clone your forked repository
```sh
cd C:\Users\tyblondr
git clone https://github.com/wenceslasdk/data-science-2.git
```
- in my example the course repository would be `C:\Users\tyblondr\data-science-2`

- now to create the Project
- open PyCharm and click 'New Project'
- set 'Name' to 'data-science-2' and 'Location' to the parent directory of your cloned repository from 2), i.e. in the example above we would set 'Location' to '\Users\tyblondr'
- choose 'Python version' as 'Python 3.10' (will be downloaded and installed if it does not exist yet on your computer)
- click 'Create' and choose 'Create from Existing Resources' if you are asked 


#### 2.3 Download the repository .zip from GitHub
- if everything fails, you can always just download the files
- click on the button <> Code, then Download ZIP


### 4) Install dependencies
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

### 5) Run Jupyter
- You can run Jupyter directly inside PyCharm
- Alternatively you can run Jupyter Lab by typing this into the terminal:
```sh
jupyter lab
```

### Keeping the fork updated
  - https://docs.github.com/en/github/collaborating-with-pull-requests/working-with-forks/syncing-a-fork
  - web UI “Fetch and Merge”
  - other option (“Configure a remote for a fork” using “Terminal” (git remote add upstream https://github.com/wenceslasdk/data-science-2.git), pull from upstream)
