import os
import sys
from subprocess import Popen, CREATE_NEW_CONSOLE
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

base_path = sys._MEIPASS
# base_path = os.path.dirname(__file__)
rel_path = os.path.join("ffmpeg","ffmpeg.exe")
ffmpeg_path = os.path.join(base_path,rel_path)


def directory_gui():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("","Select file to trim")
    inputFile = filedialog.askopenfilename()
    root.update()
    return inputFile


class window2:
    def __init__(self, master1):
        self.panel2 = tk.Frame(master1)
        self.panel2.grid()
        self.button2 = tk.Button(self.panel2, text = "Trim", command = self.panel2.quit)
        self.button2.grid()
        vcmd = (master1.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.label1 = tk.Label(self.panel2, text="Start Minute").grid()
        self.start = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd)
        self.start.grid()
        self.label1 = tk.Label(self.panel2, text="End Minute").grid()
        self.end = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd)
        self.end.grid()

    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False



def trim_gui():
    root1 = tk.Tk()
    win2 = window2(root1)
    root1.mainloop()
    params = [win2.start.get(), win2.end.get()]
    return params


def trim_video(inFile, params):
    try:
        start = int(params[0])*60
        end = int(params[1])*60
        print(start, end)
    except:
        exit()

    outFile = os.path.join(os.path.dirname(inFile), os.path.splitext(inFile)[0]+"_trimmed.mp4")
    ffmpeg_cmd = '{0} -ss {1} -to {2}  -i {3} -c copy {4}'
    # print(ffmpeg_cmd.format(ffmpeg_path, start, end, inFile, outFile))
    subProc = Popen(ffmpeg_cmd.format(ffmpeg_path, start, end, inFile, outFile), shell=False, bufsize=0, creationflags=CREATE_NEW_CONSOLE)
    return


if __name__ == '__main__':
    inputVideo = directory_gui()
    params = trim_gui()
    trim_video(inputVideo, params)
