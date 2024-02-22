# Git

## Basic usage and setup

1. What is Git and why we use it?
   - https://en.wikipedia.org/wiki/Git
   - Version control, collaboration (branches), backup
2. GitHub repository for this course
   - https://github.com/wenceslasdk/data-science-2
   - All students create a GitHub account
3. Git client with a nice GUI
   - https://www.sourcetreeapp.com/
   - Download and install Sourcetree 
   - Need to install Git, Mercurial is not needed
   - Add account into Sourcetree 
     - Tools -> Options -> Authentication -> Add
     - Select Github, click “Refresh OAuth Token” -> log in -> Authorize
	 - I usually use Credentials Manager
4. Creating a fork of the repository
   - https://docs.github.com/en/get-started/quickstart/fork-a-repo
   - Add repository to Sourcetree
     - Remote -> GitHub account -> data-science-2 -> clone
     - Choose location -> clone
5. Keeping the fork updated
   - https://docs.github.com/en/github/collaborating-with-pull-requests/working-with-forks/syncing-a-fork
   - web UI “Fetch and Merge”
   - other option (“Configure a remote for a fork” using “Terminal” (git remote add upstream https://github.com/wenceslasdk/data-science-2.git), pull from upstream)
6.	Create a branch


## Practical examples
1. Update changes from the upstream
   - Teacher to fill in the lines below, commit and push the changes

         Number of students present: 30
         Weather outside: cannot see
   
   - Students pull the changes
   - Merge into your branch

2. Make changes in your own repository 
   - Students to fill the lines below, commit and push the changes
   
         Year of study: 4
         Number of lectures today: 0

# Other tools

Useful (but not mandatory and not covered) tools for development - help with Git integration, virtual environment creation etc.

- PyCharm
- VSCode