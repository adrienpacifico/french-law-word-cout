# -*- coding: utf-8 -*-

import os, sys, logging, shutil, ntpath
execution_directory = os.getcwd()
#os.system("pdflatex " +  "-output-directory='/Users/adrienpacifico/.tmp_latex'" + " "  + '"' + tex_file + '"' )
a = os.system("find . -name '*' ! -name 'README.md' |xargs wc -w")

#TODO : allows for relatives path.

cgi_path = "/Users/adrienpacifico/Informatique/loi_versionne_sous_git/textes_de_lois/codes-juridiques-francais/codes-en-vigueur/code-general-des-impots-cgi"


os.chdir("/Users/adrienpacifico/Informatique/loi_versionne_sous_git/textes_de_lois/codes-juridiques-francais/codes-en-vigueur/code-general-des-impots-cgi")


import subprocess

proc = subprocess.Popen(["find . -name '*' ! -name 'README.md' |xargs wc -w"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print "program output:", out
print 'float_print', float(out[-15:-6])




#import ipdb
#ipdb.set_trace()
#find . -name '*' ! -name 'README.md' |xargs wc -w
