def readfile():
	global homeposition
	newfile = "./home_position.txt"
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
def writefile(position):
	newfile = "./home_position.txt"
	if not os.path.exists(newfile):
		f = open(newfile,'w')
		print newfile
		f.close()
		print newfile + " created."
	else:
		print newfile + " already existed."
		fo = open(newfile, 'wr')
		fo.write(position)
		fo.close()
	return



import time
import matplotlib.pyplot as plt
import numpy as np
filepath = 'C:\\Users\\Yuan\Documents\jimmy\\robot\\trackstar\\test_python'
with open(filepath) as fp:
   line = fp.readlines()
   line=line[1:][:];
   cnt = 0
   tmp_cnt = 0;
   row = len(line);
   col = 3;
   tmp_list = [[0 for x in range(col)] for y in range(row)];
   fig = plt.gcf()
   fig.show()
   fig.canvas.draw()
   while True:
       tmp_cnt=0;
       for lin in line:
           tmp_list[tmp_cnt][0] = tmp_cnt;
           tmp_list[tmp_cnt][1]=lin.split("    ")[3];
           tmp_list[tmp_cnt][2] = lin.split("    ")[4];
           tmp_cnt=tmp_cnt+1;
           print("Line {}: {}".format(cnt, lin.split("    ")[3]))

       if cnt%1000 == 0:
           plt.plot(tmp_list[:][0], tmp_list[:][1])
           fig.canvas.draw();

           print "End : %s" % time.ctime()
       line = fp.readlines()
       row = len(line);
       #tmp_list = [[0 for x in range(col)] for y in range(row)]
       cnt += 1