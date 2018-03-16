# Python-Online-Ordering-System

## Getting Started 

### Git clone this repository and do 
```
cd microblog/venv
pip3 install
```

### Activate virtual environment
```
source venv/bin/activate
export FLASK_APP=microblog.py
```

### Running Flask without debug mode
```

export FLASK_DEBUG=0
flask run
```

### Running Flask with debug mode
```
export FLASK_DEBUG=1
flask run
```

### Git Command
#### Reset local repository branch like the remote repository HEAD:
```
git fetch origin
git reset --hard origin/branch_name
```


## Workflow

Setup:

1. In the terminal/Shell, go to the directory where you want to place the team project, then use the following command to clone our project:

	`git clone https://github.com/whuang001/cts.git`

2. change directory to `cts` or `coding-turk-system`then use the following command to see local branch:

	`git branch`

3. you should only see a *master* branch. Now, run following command to see all remote branch:

	`git branch -r`

4. then fetch the develop branch and your own branch:

	`git fetch origin develop:develop`

	`git fetch origin your_branch:your_branch`

5. use `git branch` to see all local branch, you should see your branch, develop branch and the master branch.

6. go to the develop branch by doing `git checkout develop`, set upstream branch:

	`git branch --set-upstream-to origin/develop`

	and got to your branch do the same thing again:

	`git branch --set-upstream-to origin/your_branch`

---

How to work?

- Your branch belongs to your self, here is where you work. **However, do not work on either develop branch or master branch.**

	1. Use `git checkout your_branch` to switch to your branch. Use `git branch` to see where you are.

- When you finish a model (design and implementation, including testing), you have to merge your code to the develop branch, by doing the following things:

	1. `git checkout develop`

	2. `git pull`

	3. `git merge your_branch`

	4. `git push`. If conflict happen, solve conflict and commit, then do `git push`
	
- You can update your branch to match develop branch anytime

	1. `git checkout develop`
	
	2. `git pull`
	
	3. `git checkout your_branch`
	
	4. `git merge develop`