'''
This module is important because it gives direct access to some arguments that
are in use inside the main_script.py script, unleashing a large organization level.
'''
#Dictionary that defines the position of the labels( The tuple that defines the position have the format (x_%, y_%)):
pos = {
    'Login' : {
        'title' : (0.5, 0.1),
        'user_label' : (0.25, 0.25),
        'user_entry' : (0.5, 0.33),
        'password_label' : (0.25, 0.46),
        'password_entry' : (0.5, 0.54),
        'hide_box' : (0.22, 0.61),
        'login_button' : (0.5, 0.7),
        'error_label' : (0.5, 0.78),
        'create_button' : (0.5, 0.87),
        'img1' : (0.18, 0.1),
        'img2' : (0.82, 0.1)
        },
    'Register' : {
        'title' : (0.5, 0.05),
        'user_label' : (0.3, 0.15),
        'user_entry' : (0.5, 0.22),
        'password_label' : (0.3, 0.3),
        'password_entry' : (0.5, 0.37),
        'passwordC_label' : (0.41, 0.46),
        'passwordC_entry' : (0.5, 0.53),
        'email_label' : (0.24, 0.61),
        'email_entry' : (0.5, 0.68),
        'phone_label' : (0.35, 0.77),
        'phone_entry' : (0.5, 0.84),
        'hide_label' : (0.27, 0.43),
        'button' : (0.5, 0.94),
        'error' : (0.5, 0.89)
        },
    'Error' : {
        'button' : (0.5, 0.6),
        'label' : (0.5, 0.3),
        'img1' : (0.04, 0.3),
        'img2' : (0.96, 0.3)
        },
    'Delete' : {
        'left_button' : (0.33, 0.3), #both buttons should have same y position.
        'right_button' : (0.66, 0.3),
        'text' : (0.5, 0.1),
        'box' : (0.5, 1.5),
        'del' : (0.5, 1.5),
        'msg' : (0.5, 0.75),
        'att' : (0.5, 0.55),
        'final_position_del_y' : 0.85,
        'final_position_box_y' : 0.6
        },
    'Store': {
        'title' : (0.5, 0.1),
        'user_label' : (0.25, 0.4),
        'user_entry' : (0.5, 0.47),
        'password_label' : (0.25, 0.55),
        'password_entry' : (0.5, 0.62),
        'hide' : (0.22, 0.68),
        'button' : (0.5, 0.78),
        'error' : (0.5, 0.87),
        'platform_label' : (0.25, 0.25),
        'platform_entry' : (0.5, 0.32)
        },
    'Option': {
        'title' : (0.5, 0.1),
        'button1' : (0.5, 0.25),
        'button2' : (0.5, 0.37),
        'button3' : (0.5, 0.49),
        'button4' : (0.5, 0.61),
        'button5' : (0.5, 0.73),
        'box' : (0.35, 1.5),
        'pw_copy' : (0.75, 1.5),
        'pw_hide' : (0.5, 1.5),
        'pw_label' : (0.5, 1.5),
        'pw_label_final_y' : 0.85,
        'pw_hide_final_y' : 0.85,
        'pw_copy_final_y' : 0.95,
        'pw_box_final_y' : 0.95
        },
    'Success': {
        'button' : (0.5, 0.6),
        'label' : (0.5, 0.3)
        },
    'Show': {
        'left_button' : (0.33, 0.2), #both buttons should have the same y coordinate
        'right_button' : (0.66, 0.2),
        'title' : (0.5, 0.1),
        'data' : (0.5, 0.6),
        'box' : (-1 ,0.3),
        'data_final_y' : 0.7,
        'box_final_y' : 0.5
        },
    'Delete_Account_Confirm' : {
        'title_question' : (0.5, 0.1),
        'attention_label' : (0.5, 0.3),
        'msg_label' : (0.5, 0.55),
        'yes_button' : (0.33, 0.8),
        'cancel_button' : (0.66, 0.8),
        },
    'Delete_Data_Confirm' : {
        'title_question' : (0.5, 0.1),
        'attention_label' : (0.5, 0.3),
        'msg_label' : (0.5, 0.55),
        'yes_button' : (0.33, 0.8),
        'cancel_button' : (0.66, 0.8)
        }
    }
pattern_style = {
    'main_color' : 'mediumspringgreen',
    'main_font' : 'cascadia code semibold',
    'border_button_color' : 'black',
    'error_color' : 'red',
    'button_hover_color' : 'limegreen',
    'button_label_color' : 'black'
    }

window_size = {
    'Login' : (500, 600),
    'Register' : (600, 750),
    'Error' : (500, 150),
    'Delete' : (500, 300),
    'Store' : (500, 600),
    'Option' : (400, 500),
    'Success' : (400, 150),
    'Show' : (500, 700),
    'Delete_Account_Confirm' : (650, 300),
    'Delete_Data_Confirm' : (650, 300)
}
