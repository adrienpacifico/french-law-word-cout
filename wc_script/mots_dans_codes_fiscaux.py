# -*- coding: utf-8 -*-

import os, sys, logging, shutil, ntpath
execution_directory = os.getcwd()
#os.system("pdflatex " +  "-output-directory='/Users/adrienpacifico/.tmp_latex'" + " "  + '"' + tex_file + '"' )


#TODO : allows for relatives path.

cgi_path = "/Users/adrienpacifico/Informatique/loi_versionne_sous_git/textes_de_lois/codes-juridiques-francais/codes-en-vigueur/code-general-des-impots-cgi"


#os.chdir("/Users/adrienpacifico/Informatique/loi_versionne_sous_git/textes_de_lois/codes-juridiques-francais/codes-en-vigueur/code-general-des-impots-cgi")


import re
import subprocess


last_line_re = re.compile('\s*(?P<n>\d+)\s+total$')


output = subprocess.check_output(["find . -type f -name '*.md' | xargs wc -w"],cwd = cgi_path, shell = True)
last_line = output.rstrip().split("\n")[-1]
match = last_line_re.match(last_line)
words_count = int(match.group('n'))

output = subprocess.check_output(["find . -type f -name 'README.md' | xargs wc -w"],cwd = cgi_path, shell = True)
last_line = output.rstrip().split("\n")[-1]
match = last_line_re.match(last_line)
readme_words_count = int(match.group('n'))

print "program output:", words_count - readme_words_count

#print 'float_print', float(out[-15:-6])




#import ipdb
#ipdb.set_trace()
#find . -name '*' ! -name 'README.md' |xargs wc -w
