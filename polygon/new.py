#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
"""

============================

    @author       : Deping Huang
    @mail address : xiaohengdao@gmail.com
    @date         : 2019-12-22 22:06:11
    @project      : 65537
    @version      : 1.0
    @source file  : new.py

============================
"""
from mytools import MyCommon
class New(MyCommon):
    """docstring for new"""
    def __init__(self):
        super(New, self).__init__()
    def printLine(self,fp,line):
        """
        docstring for printLine
        """
        seperateNum = 12
        if line[0] == "a":
                fp.write(line+"\n")
        else:
            line = line.split(" ")
            # print(line)
            if len(line) < (seperateNum + 2):
                fp.write("%s\n"%(" ".join(line)))
            else:
                fp.write("%s\\\\\n"%(" ".join(line[:(seperateNum+2)])))
                line = line[(seperateNum+2):-1]
                num = len(line) // seperateNum
                for i in range(num+1):
                    ii = i*seperateNum
                    jj = ii + seperateNum
                    if jj >= len(line):
                        fp.write("& & %s \\\\ \n"%(" ".join(line[ii:])))
                    else:
                        fp.write("& & %s \\\\ \n"%(" ".join(line[ii:jj])))

        return

    def testPrintLine(self,line):
        """
        docstring for testPrintLine
        """
        seperateNum = 14
        if line[0] == "a":
                print(line+"\n")
        else:
            line = line.split(" ")
            print(line)
            if len(line) < (seperateNum + 2):
                print("%s\n"%(" ".join(line)))
            else:
                print("%s\\\\\n"%(" ".join(line[:(seperateNum+2)])))
                line = line[(seperateNum+2):-1]

                num = len(line) // seperateNum
                print("new line",line,len(line),num)
                for i in range(num+1):
                    ii = i*seperateNum
                    jj = ii + seperateNum
                    if jj >= len(line):
                        print("& & %s \\\\ \n"%(" ".join(line[ii:])))
                    else:
                        print("& & %s \\\\ \n"%(" ".join(line[ii:jj])))

        return


    def test(self):
        """
        docstring for test
        """
        data = self.loadStrings("new.tex")
        self.testPrintLine(data[193])
        return
    def run(self):
        """
        docstring for run
        """
        data = self.loadStrings("new.tex")
        # print(data)
        begin = "\\begin{eqnarray*}\n"
        end = "\\end{eqnarray*}\n"
        fp = open("65537.tex","w")

        prefix = """
        \\documentclass[twocolumn]{article}
        \\usepackage{amsmath,amssymb,amsfonts}
        \\usepackage{geometry}
        \\geometry{left=0.5cm,right=0.5cm,top=1.0cm,bottom=1.5cm}
        \\allowdisplaybreaks[4]
        \\begin{document}
          \\title{Polygon-65537}
          \\author{Xiaohengye}
          \\date{\\today}
          \\maketitle
        """

        lineNum = 20
        fp.write(prefix+"\n")
        fp.write(begin)
        for i,line in enumerate(data):
            print(i)
            # print a line 
            self.printLine(fp,line)

            if (i+1) % lineNum == 0:
                fp.write(end)
                fp.write(begin)
        fp.write(end)
        fp.write("\\end{document}")
        fp.close()

        return

new = New()
new.run()

