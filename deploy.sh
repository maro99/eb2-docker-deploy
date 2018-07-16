#!/usr/bin/env bash


#pipenv shell
pipenv lock --requirements > requirements.txt

git add requirements.txt
git add -f .secrets

eb deploy --profile fc-8th-eb --staged

git reset HEAD requirements.txt, .secrets

rm -f requirements.txt

#pipenv exit

#git add -A
#git reset HEAD requirements.txt
#git reset HEAD .secrets
#git commit -m 'Lets deploy'

