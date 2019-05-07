
import matplotlib.pyplot as plt
plt.ion()
class DynamicUpdate():
    #Suppose we know the x range
    min_x = 0
    max_x = 100

    def on_launch(self):
        #Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[], '-')
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        #self.ax.set_xlim(self.min_x, self.max_x)
        #Other stuff
        #self.ax.grid()
    def on_running(self, xdata, ydata):
        #Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        #Need both of these in order to rescale
        #self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    #Example
    def __call__(self):
        import numpy as np
        import time
        self.on_launch()
        xdata = []
        ydata = []
        import time
        import matplotlib.pyplot as plt
        import numpy as np
        filepath = 'C:\\Users\\Yuan\Documents\jimmy\\robot\\trackstar\\test_python2'
        with open(filepath) as fp:
            line = fp.readlines()
            line = line[-1];
            cnt = 0
            tmp_cnt = 0;
            row = 1;
            col = 3;
            tmp_list = [[0 for x in range(col)] for y in range(row)];
            fig = plt.gcf()
            fig.show()
            fig.canvas.draw()
            while True:
                time.sleep(1);
                #tmp_cnt = 0;
                if len(line)==0:
                    time.sleep(5)
                #for lin in line:
                tmp_list[0][0] = tmp_cnt;
                tmp_list[0][1] = line.split("    ")[3];
                tmp_list[0][2] = line.split("    ")[4];
                tmp_cnt = tmp_cnt + 1;
                xdata.append(tmp_list[:][0]);
                ydata.append(tmp_list[:][2]);
                # xdata.append(tmp_cnt);
                # ydata.append(tmp_list[tmp_cnt][2]);
                self.on_running(xdata, ydata)
                print("cnt  {}, Line: {},{}".format(cnt, len(line),lin))
               # xdata.removeall();
                #ydata.removeall();

                #time.sleep(1)
                line = fp.readlines();
                line = line[-1];
                row = len(line);
                tmp_list = [[0 for x in range(col)] for y in range(row)]
                cnt += 1
        return xdata, ydata

d = DynamicUpdate()
d()