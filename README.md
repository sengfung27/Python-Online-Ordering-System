# Python-Online-Ordering-System

## Getting Started 
### Make sure you have at least Python 2.7 in you local machine
```
pip install -r venv/bin/requirement.txt

```

### Activate virtual environment
```
source venv/bin/activate
export FLASK_APP=microblog.py
```

### Running Flask
```
flask run
```

### Git Command
#### Reset local repository branch like the remote repository HEAD:
```
git fetch origin
git reset --hard origin/branch_name
```
#### Create branch on local and remote
```
git checkout -b name_branch
git push origin name_branch
```
#### Delete branch on local and remote
```
git checkout master 
git branch -d name_branch_local
git push origin --delete name_branch_remote

```
#### Set Upstream
On your local branch
`git branch --set-upstream-to origin/your_branch`
On your master branch
`git branch --set-upstream-to origin/master`

## Workflow

Setup:

1. In the terminal/Shell, go to the directory where you want to place the team project, then use the following command to clone our project:

	`git clone https://github.com/sengfung27/Python-Online-Ordering-System.git`

2. change directory to `microblog` then use the following command to see local branch:

	`git branch`

3. you should only see a *master* branch. Now, run following command to see all remote branch:

	`git branch -r`

4. then fetch your own branch:

	`git fetch origin your_branch:your_branch`

5. use `git branch` to see all local branch, you should see your branch and the master branch.

6. go to your branch by doing `git checkout your_branch`, set upstream branch:

	`git branch --set-upstream-to origin/your_branch`

---

How to work?

- Your branch belongs to your self, here is where you work. **However, do not work on master branch.**
	 To switch to your branch. Use `git checkout your_branch`
	 Use `git branch` to see where you are.

- When you finish a model (design and implementation, including testing), you have to merge your code to the develop branch, by doing the following things:

	1. `git checkout master`

	2. `git pull`

	3. `git merge your_branch`

	4. `git push`. If conflict happen, solve conflict and commit, then do `git push`
	

