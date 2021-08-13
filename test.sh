#!/bin/bash
python test.py
git config --global credential.helper cache
git config --global credential.helper "cache --timeout=999999999"
git init
git remote add origin https://github.com/websistemath/torredecontrolo.git
git add *
git status
git commit -m "commit" -m "abriu se o test.sh"
git push origin main
read websitemath
read Algoritmo15
