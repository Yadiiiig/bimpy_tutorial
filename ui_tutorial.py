# ui_tutorial.py

import bimpy, sys, os, warnings

# This is just for me because I get warnings
# You can delete this if you don't get any warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

# Initialising bimpy UI (init(x, y, name))
ctx = bimpy.Context()
ctx.init(1000, 1000, "Tutorial")

# Variables to handle booleans
is_first_button_pressed = False
start_popup = False
open_new_window = False

# Here we declare all variables we'll need
first_input_text = bimpy.String()
popup_text = bimpy.String()
text_for_next_window = bimpy.String()

# Creating a mainloop to run the program
if __name__ == "__main__":
    # Checking if ctx should get closed or not
    while (not ctx.should_close()):
        # Using this ctx (context of the window) let's draw this
        with ctx:

            # Let's create window
            # Setting the windows position
            bimpy.set_next_window_pos(bimpy.Vec2(20, 20), bimpy.Condition.Once)
            # Setting the window size
            bimpy.set_next_window_size(bimpy.Vec2(600, 600), bimpy.Condition.Once)
            # Setting the window title
            bimpy.begin("Connection-setup")

            ### Basic printing what you write from an input: ###
            
            # This will always show the text you put inside the input box (Explanation of .value at line 59)
            bimpy.text(first_input_text.value)

            # First we put a "title" which will show up behind the input box
            # Then we put in a variable that we can find on line: 
            # Then we declare how much chars are allowed to get filled in
            bimpy.input_text('Text', first_input_text, 100)
            # This means we'll add something next to the previous object
            bimpy.same_line()
            # This is how a button works
            if bimpy.button("Show"):
                print(first_input_text.value)
                is_first_button_pressed = True

            # It's also possible to show it after a button press:
            if is_first_button_pressed:
                bimpy.text("This is the text: ")
                bimpy.same_line()
                # You always need to use .value otherwiese you'll show the memory adress
                bimpy.text(first_input_text.value)
            
            ### Example of a popup

            bimpy.input_text("Text for popup", popup_text, 100)
            if bimpy.button("Show popup with text"):
                start_popup = True
            
            # Only run this if start_popup is True
            if start_popup:
                # This is a content window
                bimpy.set_next_window_content_size(bimpy.Vec2(400, 100))
                # Start the popup
                bimpy.open_popup("Popup")
                # Enable the popup
                if bimpy.begin_popup_modal("Popup"):
                    bimpy.text("This is a popup")
                    bimpy.text("Fun fact I made this myself xdxp")
                    bimpy.text("Oh yeh here is the text:")
                    bimpy.same_line()
                    bimpy.text(popup_text.value)
                    bimpy.text("Want to close it?")
                    if bimpy.button("Yes"):
                        print("Yes")
                        # To close the popup back again
                        start_popup = False
            
            ### Opening another window

            bimpy.text("Let's open another window with some custom text")
            bimpy.input_text("Text for window", text_for_next_window, 100)
            if bimpy.button("Open next window"):
                print("Opening next window")
                open_new_window = True

            bimpy.end()

            if open_new_window:
                bimpy.set_next_window_pos(bimpy.Vec2(700, 20), bimpy.Condition.Once)
                bimpy.set_next_window_size(bimpy.Vec2(200, 100), bimpy.Condition.Once)
                bimpy.begin(text_for_next_window.value)
                bimpy.text("hey")
                bimpy.text("Close it?")
                bimpy.same_line()
                if bimpy.button("close"):
                    open_new_window = False

                bimpy.end()


