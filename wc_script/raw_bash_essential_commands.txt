
#Compte recursivement le nombre de mots en excluant les README.md

find . -name '*' ! -name 'README.md' |xargs wc -w


# Checkout at a specific date
git checkout `git rev-list -1 --before="Jan 17 2014" master`
