python test.py
git config --global user.email "cfeteira@gmail.com"
git config --global user.name "cfeteira"
git config --global credential.helper cache
git config --global credential.helper "cache --timeout=999999999"
git init
git remote add origin https://github.com/websistemath/torredecontrolo.git
git add *
git status
git commit -m "commit com o test.sh"
git push origin main
PAUSE