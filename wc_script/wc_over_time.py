# -*- coding: utf-8 -*-

import os, sys, logging, shutil, ntpath, subprocess, collections
execution_directory = os.getcwd()
#os.system("pdflatex " +  "-output-directory='/Users/adrienpacifico/.tmp_latex'" + " "  + '"' + tex_file + '"' )
#a = os.system("find . -name '*' ! -name 'README.md' |xargs wc -w")

#TODO : allows for relatives path.

cgi_path = "/Users/adrienpacifico/Informatique/loi_versionne_sous_git/textes_de_lois/codes-juridiques-francais/codes-en-vigueur/code-general-des-impots-cgi"


os.chdir("/Users/adrienpacifico/Informatique/loi_versionne_sous_git/textes_de_lois/codes-juridiques-francais/codes-en-vigueur/code-general-des-impots-cgi")


import datetime
from datetime import date
import calendar

def add_months(sourcedate,months):
    month = sourcedate.month - 1 + months
    year = int(sourcedate.year + month / 12 )
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    return datetime.date(year,month,day)


words_by_date = collections.OrderedDict()
start_date = date(2011, 4, 2)
end_date = date(2015, 6, 2)
commit_date_list = []


commit_date = start_date
while end_date >= commit_date:
    commit_date = add_months(commit_date, 1)
    commit_date_list.append(commit_date.strftime("%Y-%m-%d"))



for commit_date in commit_date_list :
    print type(commit_date)
    print "=="*100
    print "git checkout `git rev-list -1 --before=" + '"' + commit_date + '"' + " master`"
    proc = subprocess.Popen(["git checkout `git rev-list -1 --before=" + '"' + commit_date + '"' + " master`"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    proc = subprocess.Popen(["find . -name '*' ! -name 'README.md' ! -name '.DS_Store' |xargs wc -w"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    print "program output:", out.split("\n")[-1]
    print 'float_print', float(out[-15:-6])
    words_by_date[commit_date] = float(out[-15:-6])

print words_by_date




#import ipdb
#ipdb.set_trace()




#find . -name '*' ! -name 'README.md' |xargs wc -w
