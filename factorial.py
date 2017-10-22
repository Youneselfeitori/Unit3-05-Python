#Created by: Younes Elfeitori
#Created on: Oct 2017
#Created for : ICS3U
# This program calculates the factorial for any number 

import ui


def calculate_touch_up_inside(sender):
    
    # input
    input = int(view['input_number_textfield'].text)
    
    # process
    if input >= 0:
        input_answer = 1
        while input >= 1 :
            input_answer = input_answer * (input)
            input = input - 1                        
    
        # output
        view['answer_label'].text="The answer is: " + str(input_answer)
    else:
        view['answer_label'].text="Enter a number greater than or equal to 0"

view = ui.load_view()
view.present('sheet')
