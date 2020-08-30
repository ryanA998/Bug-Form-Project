#Bug Form Final Version (V 1.60)
#Author: Ryan Arendt
#Last Edited: 8/28/2020

#Description: 
#       The goal of this program is to create a standardized form in which a programmer
#       can enter bugs. Its use should be as a quick and easy documentation tool that allows 
#       you to catalog bugs and their solution as you go, vs. trying to remember what happened 
#       at a later time. The program should use TKinter to create a GUI with single-line entries, 
#       multi-line entries, checkbox and button elements. When the submit button is pressed, 
#       the contents of the form elements should be saved to a text file. 



from form_elements import *


WINDOW_SIZE = "500x600"

form_dict = {

    "FileName": {"x_pos": 10,   "y_pos": 60,    "description": "Bug_File",      "label": "File Name:"},
    "Location": {"x_pos": 10,   "y_pos": 100,   "description": "Location",      "label": "Location in Code:"},
    "Descript": {"x_pos": 10,   "y_pos":140,    "description": "Description",   "height": 6, "width": 58, "label":"Description:"},
    "Solution": {"x_pos": 10,   "y_pos":310,    "description": "Solution",      "height": 4, "width": 58, "label":"Solution:"},
    "Swatted":  {"x_pos": 10,   "y_pos": 450,   "description": "Checkbox",      "label": "YES"},
    "Tested":   {"x_pos": 10,   "y_pos": 470,   "description": "Checkbox",      "label": "YES"},
    "Resolved": {"x_pos": 10,   "y_pos": 490,   "description": "Checkbox",      "label": "YES"},
    "TimeStamp":{"x_pos": 125,  "y_pos": 20,    "description": "Time_Stamp",    "label": "Time"},
    "Submit":   {"x_pos": 75,   "y_pos": 540,   "description": "Submit",        "label": "Sumbit"},
    "Cancel":   {"x_pos": 250,  "y_pos": 540,   "description": "Cancel",        "label": "Cancel"},
}

def main():

    root = Tk()

    root.geometry(WINDOW_SIZE)
    root.configure(background="black")
    root.title("Bug Form")

    single_line_entries = gen_single_lines(root)
    multi_line_entries = gen_multi_lines(root)
    check_boxes = gen_checkboxes(root)
    time_stamp = gen_time_stamp(root)
    
    form_data = [time_stamp, single_line_entries[0], single_line_entries[1],
    multi_line_entries[0], multi_line_entries[1], check_boxes[0], check_boxes[1], check_boxes[2]]
    
    buttons = gen_buttons(root, form_data)
    
    root.mainloop()

    str_data = extract_form_data(form_data)
    
    append_file(single_line_entries[0].text_data, str_data)

def gen_buttons(win_root, data_list): 

    submit = Submit_Button(win_root, form_dict["Submit"]["label"], 
    form_dict["Submit"]["x_pos"],form_dict["Submit"]["y_pos"],form_dict["Submit"]["description"],
    data_list)

    cancel_btn = Cancel_Button(win_root, form_dict["Cancel"]["label"],
    form_dict["Cancel"]["x_pos"],form_dict["Cancel"]["y_pos"],form_dict["Cancel"]["description"])

    return [submit, cancel_btn]


def gen_time_stamp(win_root):

    return Time_Stamp(win_root, form_dict["TimeStamp"]["label"],form_dict["TimeStamp"]["x_pos"],
    form_dict["TimeStamp"]["y_pos"],form_dict["TimeStamp"]["description"])


def gen_single_lines(win_root):
    single_line_keys = ["FileName", "Location"]
    single_line_data = []
    
    for name in single_line_keys: 
        cur_entry = Single_Entry(win_root, form_dict[name]["label"],form_dict[name]["x_pos"], 
            form_dict[name]["y_pos"],form_dict[name]["description"])
        single_line_data.append(cur_entry)

    return single_line_data


def gen_multi_lines(win_root):
    multi_line_keys = ["Descript","Solution"]
    multi_line_data = []
    
    for name in multi_line_keys: 
        cur_entry = Multi_Entry(win_root, form_dict[name]["label"],form_dict[name]["x_pos"],
            form_dict[name]["y_pos"], form_dict[name]["description"],
            form_dict[name]["height"],form_dict[name]["width"])
        multi_line_data.append(cur_entry)

    return multi_line_data

def gen_checkboxes(win_root): 
    check_box_keys = ["Swatted", "Tested", "Resolved"]
    check_box_data = []
    
    for name in check_box_keys: 
        cur_el = CheckBox(win_root, name, form_dict[name]["x_pos"],form_dict[name]["y_pos"],
        form_dict[name]["description"],form_dict[name]["label"])
        check_box_data.append(cur_el)
    
    return check_box_data

 
def append_file(file_name, form_info):

    if file_name.isalnum():
        my_file = open(file_name, 'a')
        my_file.write(form_info)
        my_file.close()
    
    else: 
        print("Invalid File Name")


def print_form_data(form_objects):
    """This function is used soley for testing.
    """
    for obj in form_objects:
        
        if(obj.description == "Time_Stamp"):
            print(obj.time_stamp)

        elif(obj.description == "Checkbox"):
            print(obj.label_text, obj.is_checked)
        
        else:
            print(obj.label_text, obj.text_data)


def extract_form_data(form_objects):
    """ This function gets the relevant data from each form element in the window and formats it
        it a nice way to eventually be saved into a text file. 
    """

    form_str = ""

    for obj in form_objects:
        temp_str = ""

        if(obj.description == "Time_Stamp"):
            temp_str += rep_char("-",25) + "Date/Time:" + obj.time_stamp + rep_char("-",25) +"\n"
            form_str += temp_str


        elif(obj.description == "Checkbox"):
            temp_str += (obj.label_text + "\n" + " " + str(obj.is_checked)) + "\n"
            form_str += temp_str
        
        else:
            temp_str += obj.label_text + "\n" 
            temp_str += rep_char("-",50)+"\n" + obj.text_data + "\n"
            form_str += temp_str
        
        form_str += "\n"

    form_str += "\n"


    return form_str


def rep_char(c, n): 
    """This function repeates a certain character (c) a given number of 
        times (n). THis is needed for creating headers and other formating 
        tasks when saving the form data to a text file.
    """
    char_str = ""

    for i in range(0, n): 
        char_str += c
    
    return char_str


if __name__ == "__main__":
    main()