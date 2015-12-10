
#Compte recursivement le nombre de mots en excluant les README.md

find . -name '*' ! -name 'README.md' |xargs wc -w
