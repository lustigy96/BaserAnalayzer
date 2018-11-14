#!/usr/bin/env python
import subprocess
from subprocess import Popen, PIPE

MAX_OVERLAP=0.5 #precent
#MIN_OVERLAP=1

FILE_IN_NAME="lola"
PATH_BASER_FILES="C:\Users\YAEL\ProjectCSE\BASER\\"
PATH_DNABASER_PROGRAM="C:\Users\YAEL\DNABASER\\"

#this function takes the string and put in to #parts files with MAX overlap in the DEFINES
#this is the prepration to the DNA-BASER: 0 to T, 1 to A
def sepString2files(string, parts, name,ind):
    part = 0;
    sub_string = [];

    while(part<parts):
        start = part*(len(string)/parts)
        end = (part+1) * (len(string)/ parts)
        sub_string.append((string[start:end].replace("1","A")).replace("0","T"))
        part += 1
    for i in range(len(sub_string)-1): #the overlap is implenebted here
        f=open(PATH_BASER_FILES+"in\\"+name+str(ind)+".fa","w")
        f.write(">gi|1\n"+sub_string[i]+(sub_string[i+1])[0:int(MAX_OVERLAP*len(sub_string[i+1]))])
        f.close()
        ind += 1
    f = open(PATH_BASER_FILES + "in\\" + name + str(ind) + ".fa", "w")
    f.write(">gi|1\n" + sub_string[-1])
    f.close()



#this function (for now) only return true for "the same" and otherwise- false.
#we will put here the real statistics, but we need to learn the structure of the output
def baser_statistics(source, f_out):
    res_lines=f_out.readlines();
    res_cont=[];
    for i in range(1,len(res_lines)):
        res_cont.append(res_lines[i])
    (res_cont.replace("A","1")).replace("T","1")
    for r,s in zip(res_cont,source):
        if r!=s:
            return False
    return True



longString="110001101111111010011100111000011001110111111100111100001110101011011111111001110111111011011100111111001111100011100011111000011010101101100110100011000101101101110010011000011101000111100111101101101001111010111001011101101110101111100111110011110010011100111101100110010011001011100010110010111100111101110110111011011101100111111000011001011110011110010011011101110100111001011100101110110111100111100111110101110100111100001111001111011111000011110100111000011001101101111110010111011001110100110100011100101101111111011111010001100110110010111110001101100111011111001001111001111001111101101110"
debugString=longString[0:200]
sepString2files(string=debugString, parts=3, name=FILE_IN_NAME, ind=1)

#subprocess.call([r"C:\Users\YAEL\DNABASER\DNABaserConsole.exe", "--inputfolder="+PATH_BASER_FILES+"in", "--outputfolder="+PATH_BASER_FILES+"out"])
#print "len: " +str(len(longString))

#process = Popen([r"C:\Users\YAEL\DNABASER\DNABaserConsole.exe", "--inputfolder="+PATH_BASER_FILES+"in", "--outputfolder="+PATH_BASER_FILES+"out"], stdout=PIPE)
#(output) = process.communicate()
#print output
