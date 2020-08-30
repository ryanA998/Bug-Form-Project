#Bug Form Report Final Version
#Author: Ryan Arendt
#Last Edited: 8/28/2020

#Class Structure. 
#Form
#   -Entry Element 
#       -SingleLine 
#       -Multi Line
#       -Checkbox Element
#   -Submit
#   -Cancel 
#   -Timestamp


from tkinter import *
from tkinter import filedialog
from datetime import *


class Form:
    def __init__(self, root, label_text, x_pos, y_pos, description):
        self.root = root
        self.label_text = label_text
        self.x_pos = x_pos 
        self.y_pos = y_pos 
        self.description = description

        self.bg_color = "black"
        self.fg_color = "green"
        self.font = "systemfixed"
        self.font_size = 10

        self.border_width = 1.5
        self.highlight = 1.5


class Entry_Element(Form):
    def __init__(self, root, label_text, x_pos, y_pos, description):
        
        Form.__init__(self, root, label_text, x_pos, y_pos, description)
        
        self.label = Label(self.root,bg=self.bg_color, fg=self.fg_color, text=self.label_text)
        self.label.place(x=self.x_pos, y=self.y_pos)
        self.label.configure(font=(self.font, self.font_size))
        

class Single_Entry(Entry_Element):
    def __init__(self, root, label_text, x_pos, y_pos, description):
        Entry_Element.__init__(self, root, label_text, x_pos, y_pos, description)

        self.entry_padx = 140
        self.text_data = ""
        self.relief = FLAT
    
        self.entry_box = Entry(self.root, bg=self.bg_color, fg=self.fg_color, borderwidth=self.border_width)
        self.entry_box.place(x=self.x_pos+self.entry_padx, y=self.y_pos)
        self.entry_box.config(font=(self.font, self.font_size),highlightbackground=self.fg_color, 
        insertbackground=self.fg_color, highlightthickness=self.highlight, highlightcolor = self.fg_color,relief=self.relief)

    
    def get_data(self):

        self.text_data = self.entry_box.get()

    def clear_data(self):
        self.entry_box.delete(0, END)


class Multi_Entry(Entry_Element):
    def __init__(self, root, label_text, x_pos, y_pos, description, height, width):
        Entry_Element.__init__(self, root, label_text, x_pos, y_pos, description)
        self.height = height
        self.width = width

        self.padx = 6
        self.pady = 10
        self.wrap = WORD
        self.y_offset = 25 
        self.text_data = ""
        self.y_offest = 25
        self.relief = FLAT

        self.text_box = Text(self.root, height=self.height, borderwidth=self.border_width,
        width=self.width, wrap=self.wrap, padx=self.padx, 
        pady = self.pady, bg=self.bg_color, fg=self.fg_color)

        self.text_box.configure(font=(self.font, self.font_size), insertbackground=self.fg_color,
        highlightbackground=self.fg_color, highlightthickness=self.highlight, 
        highlightcolor = self.fg_color, relief=self.relief)

        self.text_box.place(x=self.x_pos, y=self.y_pos+self.y_offest)

    def get_data(self):
        self.text_data = self.text_box.get("1.0", 'end-1c')

    
    def clear_data(self):
        self.text_box.delete(1.0, END)


class CheckBox(Entry_Element):
    def __init__(self, root, label_text, x_pos, y_pos, discription, check_text):
        Entry_Element.__init__(self, root, label_text, x_pos, y_pos, discription)

        self.check_text = check_text
        self.checked_val = IntVar()
        self.is_checked = 0 
        self.x_offset = 70
        self.hover_color = "#3da513"

        self.check_box = Checkbutton(root, text=self.check_text, variable=self.checked_val, bg=self.bg_color, fg=self.fg_color,
        bd=0.2, highlightbackground=self.bg_color, onvalue=1, 
        offvalue=0, height=1, width=5,selectcolor="black", activebackground=self.hover_color)

        self.check_box.place(x=self.x_pos+self.x_offset, y=self.y_pos)


    def get_data(self):
        self.is_checked = self.checked_val.get()

    
    def clear_data(self):
        self.check_box.deselect()


class Submit_Button(Form):
    def __init__(self, root, label_text, x_pos, y_pos, discription, form_elements):
        Form.__init__(self, root, label_text, x_pos, y_pos, discription)

        self.form_elements = form_elements
        self.btn_width = 15 
        self.btn_text = "Sumbit"

        self.hover_color = "#3da513"
        self.box_border = 0.2

        self.button = Button(self.root, text=self.btn_text, width=self.btn_width, bg=self.bg_color, fg=self.fg_color,
                            borderwidth=self.border_width,highlightbackground=self.fg_color,
                            activebackground = self.hover_color, bd=self.box_border,
                            command=lambda:self.get_form_data(self.form_elements))
        
        self.button.place(x=self.x_pos, y=self.y_pos)


    def get_form_data(self, form_info):
        
        for obj in form_info:
            
            if obj.description == "Time_Stamp":
                obj.update_cur_time()
            
            else:
                obj.get_data()
                obj.clear_data()


class Cancel_Button(Form):
    def __init__(self, root, label_text, x_pos, y_pos, discription):
        Form.__init__(self, root, label_text, x_pos, y_pos, discription)

        self.btn_text = "Cancel"
        self.btn_width = 15
        self.hover_color = "#3da513"
        self.box_border = 0.2

        self.button = Button(self.root, text=self.btn_text, width=self.btn_width, bg=self.bg_color, 
            fg=self.fg_color, borderwidth=self.border_width, highlightbackground=self.fg_color,
            activebackground = self.hover_color, bd=self.box_border, command=self.root.quit)

        self.button.place(x=self.x_pos, y=self.y_pos)


class Time_Stamp(Form):
    def __init__(self, root,  label_text, x_pos, y_pos, description):
        Form.__init__(self, root, label_text, x_pos, y_pos, description)

        self.time_stamp = self.get_cur_time()
        self.time_text = Label(root, text=self.time_stamp, bg=self.bg_color, fg=self.fg_color)
        self.time_text.place(x=self.x_pos, y=self.y_pos)

        self.time_text.configure(font=(self.font, self.font_size))


    def get_cur_time(self):
        cur_time = datetime.now()
        return datetime.strftime(cur_time,'%A, %B %d, %I:%M %p')


    def update_cur_time(self):
        self.time_text.config(text=self.get_cur_time())



