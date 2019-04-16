import os
def test():
    newfile = "./homeposition.txt"
    if not os.path.exists(newfile):
        f = open(newfile,'w')
        print newfile
        f.close()
        print newfile + " created."
    else:
        print newfile + " already existed."
        fo = open(newfile, 'r+')
        line=fo.readline()
        line = line.strip()
        homeposition=line
        print "homeposition ", (homeposition)
        fo.close()
    return

test()