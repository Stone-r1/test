import tkinter
import tkinter.messagebox


class AverageScore:
    def __init__(self):
        self.main_window = tkinter.Tk()
        # frames
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.result_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        # labels
        self.test1_label = tkinter.Label(self.test1_frame, text='test 1 score: ')
        self.test2_label = tkinter.Label(self.test2_frame, text='test 2 score: ')
        self.test3_label = tkinter.Label(self.test3_frame, text='test 3 score: ')
        # entry's
        self.test1_entry = tkinter.Entry(self.test1_frame, width=15)
        self.test2_entry = tkinter.Entry(self.test2_frame, width=15)
        self.test3_entry = tkinter.Entry(self.test3_frame, width=15)
        # pack
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')
        # create new label to average result
        self.result_label = tkinter.Label(self.result_frame, text='average score: ')
        self.avg = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.result_label, textvariable=self.avg)
        # pack
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')
        # create find and quit buttons
        self.calculate_button = tkinter.Button(self.button_frame, text='find', command=self.calc_average)
        self.quit_button = tkinter.Button(self.button_frame, text='quit', command=self.main_window.destroy)
        # pack
        self.calculate_button.pack(side='left')
        self.quit_button.pack(side='left')
        # pack all frames
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.result_frame.pack()
        self.button_frame.pack()
        # run main loop
        tkinter.mainloop()

    # function to calculate average amount and return it
    def calc_average(self):

        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())

        self.average = (self.test1 + self.test2 + self.test3) / 3.0

        self.avg.set(self.average)

test_avg = AverageScore()