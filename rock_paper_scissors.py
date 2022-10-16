import tkinter
import tkinter.messagebox
import random

class Something:
    def __init__(self):
        # page structure size and resizable parametr.
        self.main_page = tkinter.Tk()
        self.main_page.title('.')
        self.main_page.geometry('125x140+700+200')
        self.main_page.resizable(0, 0)
        self.main_page.iconbitmap('')
        # creating four frames for count choice answers and buttons
        self.count_frame = tkinter.Frame(self.main_page)
        self.choice_frame = tkinter.Frame(self.main_page)
        self.answer_frame = tkinter.Frame(self.main_page)
        self.button_frame = tkinter.Frame(self.main_page)
        # when stating text which means : count. .
        self.count_label1 = tkinter.Label(self.count_frame, text='Count',
                                          bg='#6fd19d', fg='Black', width=10)
        # creating a new count system which gave win counts to self.count and then calculating win amount.
        self.count = tkinter.StringVar()
        self.count_label = tkinter.Label(self.count_frame, textvariable=self.count,
                                         bg='#6fd19d', fg='Black', width=10)
        # pack
        self.count_label.pack(side='right')
        self.count_label1.pack(side='right')
        # creating new strutctures to checkbuttons
        self.ch_var1 = tkinter.IntVar()
        self.ch_var2 = tkinter.IntVar()
        self.ch_var3 = tkinter.IntVar()
        # set position 0 , which means the checkbutton isn't activated.
        self.ch_var1.set(0)
        self.ch_var2.set(0)
        self.ch_var3.set(0)
        # creating new checkbuttons.
        self.choice_rock = tkinter.Checkbutton(self.choice_frame, text='Rock',
                                               variable=self.ch_var1, width=20,
                                               bg='#6fd19d', fg='Black', activebackground='#5fcf93')
        self.choice_paper = tkinter.Checkbutton(self.choice_frame, text='Paper',
                                                variable=self.ch_var2, width=20,
                                                bg='#6fd19d', fg='Black', activebackground='#5fcf93')
        self.choice_scissors = tkinter.Checkbutton(self.choice_frame, text='Scissors',
                                                   variable=self.ch_var3, width=20,
                                                   bg='#6fd19d', fg='Black', activebackground='#5fcf93')
        # pack
        self.choice_rock.pack(side='top')
        self.choice_paper.pack(side='top')
        self.choice_scissors.pack(side='top')
        # show result when each game is over.
        self.result = tkinter.StringVar()
        self.restul_label = tkinter.Label(self.answer_frame, textvariable=self.result,
                                          bg='#6fd19d', fg='Black', width=20)
        # pack
        self.restul_label.pack(side='right')
        # creating buttons to play game and to leave the game.
        self.play_button = tkinter.Button(self.button_frame, command=self.calc,
                                          bg='#6fd19d', fg='Black', width=12, activebackground='#5fcf93',
                                          text='Play')
        self.quite_button = tkinter.Button(self.button_frame, command=self.main_page.destroy,
                                           bg='#6fd19d', fg='Black', width=12, activebackground='#5fcf93',
                                           text='Quit')
        # pack
        self.play_button.pack(side='right')
        self.quite_button.pack(side='right')
        # pack
        self.count_frame.pack()
        self.choice_frame.pack()
        self.answer_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()
# create new function to calculate who won and to add count
    def calc(self):
        if self.count.get() == '':
            count = 0
        elif self.result.get() == 'you won':
            count = self.count.get()
        else:
            count = self.count.get()

        int_count = int(count)
        # random number . 1 = rock. 2 = paper, 3 = scissors
        pc_answer = random.randint(1, 3)
        # get a value
        rock = self.ch_var1.get()
        paper = self.ch_var2.get()
        scissors = self.ch_var3.get()
        # If a user chooses more than one answer, the program will give him an error message.
        if rock == 1 and paper == 1 and scissors == 1:
            tkinter.messagebox.showerror('Error', 'please choose one element ')
        elif rock == 1 and scissors == 1 or rock == 1 and paper == 1 or paper == 1 and scissors == 1:
            tkinter.messagebox.showerror('Error', 'please choose one element ')
        else:
            # game.
            if rock == 1 and pc_answer == 1 or paper == 1 and pc_answer == 2 or scissors == 1 and pc_answer == 3:
                int_count += 0
                self.result.set('draw')
                self.count.set(int_count)
            elif rock == 1 and pc_answer == 2:
                int_count += 0
                self.result.set('pc won')
                self.count.set(int_count)
            elif rock == 1 and pc_answer == 3:
                int_count += 1
                self.result.set('you won')
                self.count.set(int_count)
            elif paper == 1 and pc_answer == 1:
                int_count += 1
                self.result.set('you won')
                self.count.set(int_count)
            elif paper == 1 and pc_answer == 3:
                int_count += 0
                self.result.set('pc won')
                self.count.set(int_count)
            elif scissors == 1 and pc_answer == 1:
                int_count += 0
                self.result.set('pc won')
                self.count.set(int_count)
            elif scissors == 1 and pc_answer == 2:
                int_count += 1
                self.result.set('you won')
                self.count.set(int_count)

something = Something()