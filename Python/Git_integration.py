"""
Title: Managing Git Repositories using Python
Date: 04/01/2024
Author: Lyra "Archivist" Hawkins
"""

# Documentation for git package:
# https://gitpython.readthedocs.io/en/stable/

import git
from git import Repo

## Initialise a new repository with a .git directory
# `git init new_repo`
new_repo = git.Repo.init('new_repo')

## Open an existing repository on the disk, pass to the Repo() obj initialiser
my_repo = git.Repo('existing_repo')

# clone a remote repo via HTTPS
git.Repo.clone_from('https://github.com/Archivist-Ember/CookBook/Python','')
# clone via ssh
git.Repo.clone_from()

# Cloning a local repo
# Load existing repo
my_repo = git.Repo('existing_repo')
# create copy of existing repo
my_repo.clone('/path/to/clone_of_existing_repo')

## Working with Repositories
my_repo = git.Repo('some_repo')

# Check for changes
if my_repo.is_dirty(untracked_files=True):
	print('Repository has been altered')

# Access the difference and see changes
repo = Repo('my_repo')
diff = repo.git.diff(repo.head.commit.tree)
print(diff)

# Add and commit files
my_repo = git.Repo('some_repo')
# list the files to stage
repo.index.add(['.gitignore','README.md','codefile.py'])
# add commit message
repo.index.commit('Message included with commit')

## Work with remote Repositories

repo = git.Repo('test_repo')

# List remotes
print('Remotes:')
for remote in repo.remotes:
	print(f'- {remote.name} {remote.url}')

# create new remote
try:
	remote = repo.create_remote('origin', url='git@github.com:Archivist-Ember/test_repo')
except git.exc.GitCommandError as error:
	print(f'Error creating remote: {error}')

# Ref a remote by name as part of obj
print(f'Remote name: {repo.remotes.origin.name}')
print(f'Remote URL: {repo.remotes.origin.url}')

# Delete remote
repo.delete_remote('myremote')

# Pull from remote repo
print(repo.remotes.origin.pull())
# Push changes
print(repo.remotes.origin.push())

## Create and switch Branches

repo = git.Repo.init('my_new_repo')

# list branches
for branch in repo.branches:
	print(branch)


# create new branch
repo.git.branch('new_branch')
# You need to check out the branch after creating it if you want to use it
repo.git.checkout('new_branch')

# checkout master branch again
repo.git.checkout('master')