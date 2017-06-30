# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-21 01:41:49
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-22 23:57:53
import os
if not os.path.exists("bin/"):
    os.mkdir("bin")
os.chdir("bin")
if not os.path.exists("images/"):
    os.mkdir("images")
os.system("cp ../ref.bib .")
os.system("cp ../../src/*.eps images/")
os.system('latex ../paper.tex')
os.system('bibtex paper')
os.system('latex ../paper.tex')
os.system('latex ../paper.tex')
os.system("dvipdft paper")
