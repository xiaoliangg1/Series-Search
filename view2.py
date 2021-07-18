from tkinter import *
from tkinter import messagebox


class View:

    def __init__(self):
        self.Menu = None
        # Tk window for user to input the title of series
        self.Selection = None
        # Tk window for user selection
        self.user_inp = ''
        # string of user's series title
        self.select = []
        # list of episodes that user selected

    def menu(self):
        """Function create the Tk window for user to input their series
        title"""
        self.Menu = Tk()
        self.Menu.title('TV Show Search')
        message = Label(self.Menu, text='Enter the title of series:')
        self.user_inp = Entry(self.Menu)
        search_button = Button(self.Menu, text='Search', command=self.search)
        # Create button that run the function search() (function below) when
        # press

        message.grid(row=0, column=0)
        self.user_inp.grid(row=0, column=1)
        search_button.grid(row=1, column=0)
        # layout of Tk window

        self.Menu.mainloop()

        return self.user_inp
        # return user input title so control can pass it to model

    def add_value(self):
        w = self.total_list.get(ACTIVE)
        self.mylist.insert(END, w)
        self.total_list.delete(ACTIVE)
    
    def remove_value(self):
        y = self.mylist.get(ACTIVE)
        self.total_list.insert(END, y)
        self.mylist.delete(ACTIVE)
        
    def scrollbar(self, List_of_epi):
        """Function create a Tk window for episodes selection"""
        self.Selection = Tk()

        scrollbar = Scrollbar(self.Selection)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.total_list = Listbox(self.Selection,
                                  bg='linen',
                                  yscrollcommand=scrollbar.set,
                                  width=70)
        self.total_list.pack(side=LEFT, expand=1, fill=X)
        select = Button(self.Selection, text="Select", bg='gold',
                        command=self.select_choose)
        select.pack(side=RIGHT, fill=Y)
        # Create button that run the function select_choose()
        # (function below) when press
        self.mylist = Listbox(self.Selection, width=70, bg='linen')
        self.mylist.pack(side=RIGHT, expand=1, fill=X)
        # create two listboxs for episodes
        Button(self.Selection, text='Remove', bg='red',
               command=self.remove_value).pack(side=RIGHT, fill=BOTH)
        # removes the selected episode
        Button(self.Selection, text='Select Episode', bg='green3',
               command=self.add_value).pack(side=RIGHT, fill=BOTH)
        # adds the selected episode
        for i in List_of_epi:
            # put all the episodes that is found, which in a list
            # call List_of_epi, into the listbox
            string = 'Season: %s, Episodes: %s, Title: %s' \
                     % (i['Season'], i['Episodes'], i['Title'])
            self.total_list.insert(END, string)
            self.total_list.pack()

        scrollbar.config(command=self.total_list.yview)
        # display the listbox

        self.Selection.mainloop()

        return self.select
        # return user selections so can be use by control for download

    def select_choose(self):
        """Function for select button in Tk window Selection"""
        self.select = self.mylist.get(0, END)
        self.Selection.destroy()
        # storage all episodes that user select in listbox into a list in self
        # call select

    def save_choose(self):
        lis = []
        for i in range(len(self.select)):
            if self.total_list[i].get() == 1:
                lis.append(i)
        c.Check_correct_selection(lis)
        self.Selection.destroy()

    def search(self):
        """Function for search button in Tk window menu"""
        self.user_inp = self.user_inp.get()
        self.Menu.destroy()

    def error_NotFound(self):
        """Display the error message for series that is not fount."""
        window = Tk()
        window.withdraw()
        # To prevent Tk window show up when message box used
        messagebox.showinfo('Error', 'Title of input series is NOT IN DATABASE'
                                     ' or is TOO BOARD. Please Reenter.')
    def view_download(self):
        self.Dwindow = Tk()
        label_1 = Label(self.Dwindow, text='Filename')
        label_1.grid(row=1, column=0)
        self.filename = Entry(self.Dwindow, width=60)
        self.filename.grid(row=1, column=1)
        label_2 = Label(self.Dwindow, text='Path')
        label_2.grid(row=2, column=0)
        self.path = Entry(self.Dwindow, width=60)
        self.path.grid(row=2, column=1)
        #ac_path = os.path.join(str(path.get()), str(filename.get())+'.csv')
        s_button = Button(self.Dwindow, text='Submit'
                          , command=self.get_path)
        s_button.grid(row=3, column=0)
        self.Dwindow.mainloop()
        

        
    def get_path(self):
        path = self.path.get()
        print(path)
        filename = self.filename.get()
        print(filename)
        self.ac_path = os.path.join(str(path), str(filename)+'.csv')
        print(self.ac_path)
        self.Dwindow.destroy()


if __name__ == '__main__':
    x = View()
    x.error_NotFound()
