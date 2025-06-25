import customtkinter as ctk
import SQL_CRUD
from PIL import Image
import pyperclip
import pw_generator
import args

class Entry:

    def __init__(self, window, width, height, placeholder,
                 posx, posy, text_color,
                 font_size, font_style, border_width, border_color, background_color):
        self.width = width
        self.background_color = background_color
        self.height = height
        self.placeholder = placeholder
        self.posx = posx
        self.posy = posy
        self.text_color = text_color
        self.font_size = font_size
        self.font_style = font_style
        self.border_width = border_width
        self.border_color = border_color
        self.entry = ctk.CTkEntry(window,
                                fg_color = self.background_color,
                                width = self.width,
                                height = self.height,
                                text_color = self.text_color,
                                placeholder_text = self.placeholder,
                                font = (self.font_style, self.font_size),
                                border_width = self.border_width,
                                border_color = self.border_color)
        self.entry.place(relx = posx, rely = posy, anchor = 'center')

class Label:

    def __init__(self, window, text,
                 posx, posy, text_color,
                 font_size, font_style):
        self.text = text
        self.posx = posx
        self.posy = posy
        self.text_color = text_color
        self.font_size = font_size
        self.font_style = font_style
        self.label = ctk.CTkLabel(window,
                                text_color = self.text_color,
                                text = self.text,
                                font = (self.font_style, self.font_size))
        self.label.place(relx = self.posx, rely = self.posy, anchor = 'center')

class Img:

    def __init__(self, window, width, height, path, posx, posy):
        self.window = window
        self.width = width
        self.height = height
        self.path = path
        self.posx = posx
        self.posy = posy
        self.IMG = ctk.CTkImage(light_image = Image.open(self.path), size = (self.width, self.height))
        self.my_image = ctk.CTkLabel(self.window,
                                     text = '',
                                     image = self.IMG)
        self.my_image.place(relx = self.posx, rely = self.posy, anchor = 'center')

class Window:

    #This constructor defines the basic window
    def __init__(self, width, height, icon_path, title):
        self.root = ctk.CTk()
        self.root.geometry(f'{width}x{height}')
        self.root.title(title)
        self.root.iconbitmap(icon_path)
        self.root.resizable(False, False)

    #Method that will open the window linked to the object
    def open_window(self):
        self.root.mainloop()

class Login_Window(Window):

    id_user = None
    user = None
    green_card_login = False
    #(500, 650)
    def __init__(self, width, height, icon_path, title, **kwargs):
        super().__init__(width, height, icon_path, title) #Here, self.root is the window for the self object from this class
        self.error = Label(window = self.root,
                           text = kwargs['error_label_text'],
                           posx = kwargs['error_label_posx'],
                           posy = kwargs['error_label_posy'],
                           text_color = kwargs['error_label_color'],
                           font_size = kwargs['font_error'],
                           font_style = kwargs['font_style_label'])
        #Defining the title label
        self.title = Label(window = self.root,
                      text = kwargs['text_title'],
                      posx = kwargs['posx_title'],
                      posy = kwargs['posy_title'],
                      text_color = kwargs['color_label'],
                      font_size = kwargs['font_size_title_label'],
                      font_style = kwargs['font_style_label'])
        #Defining the username label
        self.username = Label(window = self.root,
                         text = kwargs['text_user'],
                         posx = kwargs['posx_user'],
                         posy = kwargs['posy_user'], 
                         text_color= kwargs['color_label'],
                         font_size = kwargs['font_size_otherwise_label'],
                         font_style = kwargs['font_style_label'])
        #Defining the username entry
        self.entry_user = Entry(window = self.root,
                           placeholder = kwargs['entry_user_placeholder'],
                           posx = kwargs['entry_user_posx'],
                           posy = kwargs['entry_user_posy'],
                           text_color = kwargs['color_entry'],
                           font_size = kwargs['font_size_entry'],
                           font_style = kwargs['font_style_entry'],
                           width = kwargs['width_entry'],
                           height = kwargs['height_entry'],
                           border_color = kwargs['border_color_entry'],
                           border_width = kwargs['border_width_entry'],
                           background_color = kwargs['bgcolor_entry'])
        #Defining the password label
        self.password_label = Label(window = self.root,
                         text = kwargs['text_password'],
                         posx = kwargs['posx_password'],
                         posy = kwargs['posy_password'], 
                         text_color= kwargs['color_label'],
                         font_size = kwargs['font_size_otherwise_label'],
                         font_style = kwargs['font_style_label'])
        #Defining the password entry
        self.entry_password = Entry(window = self.root,
                           placeholder = kwargs['entry_user_placeholder'],
                           posx = kwargs['entry_password_posx'],
                           posy = kwargs['entry_password_posy'],
                           text_color = kwargs['color_entry'],
                           font_size = kwargs['font_size_entry'],
                           font_style = kwargs['font_style_entry'],
                           width = kwargs['width_entry'],
                           height = kwargs['height_entry'],
                           border_color = kwargs['border_color_entry'],
                           border_width = kwargs['border_width_entry'],
                           background_color = kwargs['bgcolor_entry'])
        self.hide_control = ctk.StringVar(value = 'off')
        #defining the hiding password system button
        self.hide = ctk.CTkCheckBox(self.root,
                                    text = 'show password',
                                    onvalue = 'on',
                                    offvalue = 'off',
                                    variable = self.hide_control,
                                    command = self.hide_method,
                                    checkbox_height = kwargs['checkbox_size'],
                                    checkbox_width = kwargs['checkbox_size'],
                                    fg_color = args.pattern_style['main_color'],
                                    hover_color = args.pattern_style['main_color'],
                                    border_color = args.pattern_style['main_color'],
                                    text_color = args.pattern_style['main_color'])
        self.hide.place(relx = kwargs['pos_hide_x'], rely = kwargs['pos_hide_y'], anchor = 'center')
        #defining the submmit button
        self.button = ctk.CTkButton(self.root,
                                    text = kwargs['button_text'],
                                    fg_color = kwargs['color_of_button'],
                                    command = self.check,
                                    width = kwargs['button_width'],
                                    height = kwargs['button_height'],
                                    font = (kwargs['font_style_button'], kwargs['font_size']),
                                    hover_color = kwargs['hover_color_button'],
                                    text_color = kwargs['button_text_color'],
                                    border_color = kwargs['border_color'],
                                    border_width = kwargs['border_w'])
        self.button.place(relx = kwargs['button_posx'], rely = kwargs['button_posy'], anchor = 'center')
        if kwargs['green_card_register']:
            self.IMG1 = Img(self.root, width = 70, height = 70, path = 'images/lock.png', posx = kwargs['img1x'], posy = kwargs['img1y'])
            self.IMG2 = Img(self.root, width = 70, height = 70, path = 'images/lock.png', posx = kwargs['img2x'], posy = kwargs['img2y'])
            self.button = ctk.CTkButton(self.root,
                                        text = kwargs['button_text_create'],
                                        fg_color = kwargs['color_of_button'],
                                        width = kwargs['button_width'],
                                        height = kwargs['button_height'],
                                        font = (kwargs['font_style_button'], kwargs['font_size']),
                                        hover_color = kwargs['hover_color_button'],
                                        text_color = kwargs['button_text_color'],
                                        command = self.call,
                                        border_color = kwargs['border_color'],
                                        border_width = kwargs['border_w'])
            self.button.place(relx = kwargs['button_posx_create'], rely = kwargs['button_posy_create'], anchor = 'center')
        
    #Defining the hidden password symbol
    def hide_method(self):
        if self.hide_control.get() == 'on':
            self.entry_password.entry.configure(show = '*')
        else:
            self.entry_password.entry.configure(show = '')

    #This method will check if the input register is in the database or not
    def check(self):
        if SQL_CRUD.check_user(self.entry_user.entry.get()):
            if SQL_CRUD.check_cross_data(self.entry_user.entry.get(), self.entry_password.entry.get()):
                Login_Window.user = self.entry_user.entry.get()
                Login_Window.id_user = SQL_CRUD.catch_id(self.entry_user.entry.get())
                self.root.destroy()
                Login_Window.green_card_login = True
            else:
                self.error.label.configure(text = "Error: Wrong password!")
        else:
            self.error.label.configure(text = "Error: The user doesn't exist!")
    #This method will call the login window when we click at the create button
    def call(self):
        self.register = Register_Window(args.window_size['Register'][0], args.window_size['Register'][1], 'Ico_Files/for_test.ico',
                                        'Password Management System ErickDev',
                                        text_title = 'REGISTER AN ACCOUNT',
                                        posx_title = args.pos['Register']['title'][0],
                                        posy_title = args.pos['Register']['title'][1], 
                                        color_label = args.pattern_style['main_color'],
                                        font_size_title_label = 40,
                                        font_style_label = args.pattern_style['main_font'],
                                        text_user = 'Username',
                                        posx_user = args.pos['Register']['user_label'][0],
                                        posy_user = args.pos['Register']['user_label'][1],
                                        font_size_otherwise_label = 30,
                                        entry_user_placeholder = 'Type the username here',
                                        entry_user_posx = args.pos['Register']['user_entry'][0],
                                        entry_user_posy = args.pos['Register']['user_entry'][1],
                                        color_entry = 'white', font_size_entry = 20,
                                        font_style_entry = args.pattern_style['main_font'],
                                        width_entry = 400,
                                        height_entry = 50,
                                        text_password = 'Password',
                                        posx_password = args.pos['Register']['password_label'][0],
                                        posy_password = args.pos['Register']['password_label'][1],
                                        entry_password_posx = args.pos['Register']['password_entry'][0],
                                        entry_password_posy = args.pos['Register']['password_entry'][1],
                                        entry_PW_placeholder = 'Type your password here',
                                        text_passwordC = 'Confirm Password',
                                        posx_passwordC = args.pos['Register']['passwordC_label'][0],
                                        posy_passwordC = args.pos['Register']['passwordC_label'][1],
                                        entry_passwordC_posx = args.pos['Register']['passwordC_entry'][0],
                                        entry_passwordC_posy = args.pos['Register']['passwordC_entry'][1],
                                        email = 'Email',
                                        posx_email = 0.24,
                                        posy_email = 0.61,
                                        entry_email_posy = args.pos['Register']['email_entry'][1],
                                        entry_email_posx = args.pos['Register']['email_entry'][0],
                                        entry_email_placeholder = 'Type your email here',
                                        phone_text = 'Phone Number',
                                        posx_phone = args.pos['Register']['phone_label'][0],
                                        posy_phone = args.pos['Register']['phone_label'][1],
                                        entry_phone_placeholder = 'Type your phone number here',
                                        entry_phone_posx = args.pos['Register']['phone_entry'][0],
                                        entry_phone_posy = args.pos['Register']['phone_entry'][1],
                                        pos_hide_x = args.pos['Register']['hide_label'][0],
                                        pos_hide_y = args.pos['Register']['hide_label'][1],
                                        button_text = 'REGISTER',
                                        color_of_button = args.pattern_style['main_color'],
                                        hover_color = args.pattern_style['button_hover_color'],
                                        button_width = 300, button_height = 50,
                                        font_style_button = args.pattern_style['main_font'],
                                        font_size_button = 30,
                                        button_text_color = args.pattern_style['button_label_color'], 
                                        button_posx = args.pos['Register']['button'][0],
                                        button_posy = args.pos['Register']['button'][1],
                                        border_width_entry = 4,
                                        border_color_entry = args.pattern_style['main_color'],
                                        bgcolor_entry = 'black',
                                        checkbox_size = 20,
                                        error_posx = args.pos['Register']['error'][0],
                                        error_posy = args.pos['Register']['error'][1],
                                        border_w = 4,
                                        border_color = args.pattern_style['border_button_color'])
        self.register.open_window()

class Store_Window(Login_Window):

    def __init__(self, width, height, icon_path, title, id_user, **kwargs):
        super().__init__(width, height, icon_path, title,
                         font_size_title_label = kwargs['font_size_title_label'],
                         font_size_otherwise_label = kwargs['font_size_otherwise_label'],
                         font_style_label = kwargs['font_style_label'],
                         text_title = kwargs['text_title'],
                         posx_title = kwargs['posx_title'],
                         posy_title = kwargs['posy_title'],
                         color_label = kwargs['color_label'],
                         text_user = kwargs['text_user'],
                         posx_user = kwargs['posx_user'],
                         posy_user = kwargs['posy_user'],
                         entry_user_placeholder = kwargs['entry_user_placeholder'],
                         entry_user_posx = kwargs['entry_user_posx'],
                         entry_user_posy = kwargs['entry_user_posy'],
                         color_entry = kwargs['color_entry'],
                         bgcolor_entry = kwargs['bgcolor_entry'],
                         border_color_entry = kwargs['border_color_entry'],
                         border_width_entry = kwargs['border_width_entry'],
                         font_style_entry = kwargs['font_style_entry'],
                         hover_color_button = kwargs['hover_color_button'],
                         font_size_entry = kwargs['font_size_entry'],
                         width_entry = kwargs['width_entry'],
                         height_entry = kwargs['height_entry'],
                         text_password = kwargs['text_password'],
                         posx_password = kwargs['posx_password'],
                         posy_password = kwargs['posy_password'],
                         entry_password_posx = kwargs['entry_password_posx'],
                         entry_password_posy = kwargs['entry_password_posy'],
                         pos_hide_x = kwargs['pos_hide_x'],
                         pos_hide_y = kwargs['pos_hide_y'],
                         button_text = kwargs['button_text'],
                         button_text_create = kwargs['button_text_create'],
                         color_of_button = kwargs['color_of_button'],
                         button_width = kwargs['button_width'],
                         button_height = kwargs['button_height'],
                         font_size = kwargs['font_size'],
                         font_style_button = kwargs['font_style_button'],
                         button_text_color = kwargs['button_text_color'],
                         button_posx = kwargs['button_posx'],
                         button_posy = kwargs['button_posy'],
                         checkbox_size = kwargs['checkbox_size'],
                         button_posy_create = kwargs['button_posy_create'],
                         error_label_text = kwargs['error_label_text'],
                         error_label_color = kwargs['error_label_color'],
                         error_label_posx = kwargs['error_label_posx'],
                         error_label_posy = kwargs['error_label_posy'],
                         font_error = kwargs['font_error'],
                         green_card_register = False,
                         border_color = None,
                         border_w = None,
                         img1x = None,
                         img2x = None,
                         img2y = None,
                         img1y = None,
                         button_posx_create = None)
        self.id_user = id_user
        #Defining the platform label
        self.platform = Label(window = self.root,
                         text = kwargs['text_plat'],
                         posx = kwargs['posx_plat'],
                         posy = kwargs['posy_plat'], 
                         text_color= kwargs['color_label'],
                         font_size = kwargs['font_size_otherwise_label'],
                         font_style = kwargs['font_style_label'])
        #Defining the entry platfomr
        self.entry_platform = Entry(window = self.root,
                           placeholder = kwargs['entry_user_placeholder'],
                           posx = kwargs['entry_plat_posx'],
                           posy = kwargs['entry_plat_posy'],
                           text_color = kwargs['color_entry'],
                           font_size = kwargs['font_size_entry'],
                           font_style = kwargs['font_style_entry'],
                           width = kwargs['width_entry'],
                           height = kwargs['height_entry'],
                           border_color = kwargs['border_color_entry'],
                           border_width = kwargs['border_width_entry'],
                           background_color = kwargs['bgcolor_entry'])

    def check(self):
        try:
            SQL_CRUD.insert_data(plat = self.entry_platform.entry.get(),
                                user = self.entry_user.entry.get(),
                                pw = self.entry_password.entry.get(),
                                id_user = self.id_user)
        except:
            self.error.label.configure(text = "Error: can't insert the data.\n Perhaps, you're repeating data.")
        else:
            self.success = Success(icon_path='Ico_Files/for_test.ico', title = 'Success PMS', text = 'DATA STORED SUCCESFULLY')
            self.success.open_window()
        '''An exception should rise when the user tries to store
        repeated username and platform because of a constraint
        in the database(present in the file basics_structure.sql'''

class Register_Window(Window):
    #(600, 750)
    def __init__(self, width, height, icon_path, title, **kwargs):
        super().__init__(width, height, icon_path, title)
        self.title = Label(window = self.root,
                      text = kwargs['text_title'],
                      posx = kwargs['posx_title'],
                      posy = kwargs['posy_title'],
                      text_color = kwargs['color_label'],
                      font_size = kwargs['font_size_title_label'],
                      font_style = kwargs['font_style_label'])
        self.username = Label(window = self.root,
                         text = kwargs['text_user'],
                         posx = kwargs['posx_user'],
                         posy = kwargs['posy_user'], 
                         text_color= kwargs['color_label'],
                         font_size = kwargs['font_size_otherwise_label'],
                         font_style = kwargs['font_style_label'])
        self.entry_user = Entry(window = self.root,
                           placeholder = kwargs['entry_user_placeholder'],
                           posx = kwargs['entry_user_posx'],
                           posy = kwargs['entry_user_posy'],
                           text_color = kwargs['color_entry'],
                           font_size = kwargs['font_size_entry'],
                           font_style = kwargs['font_style_entry'],
                           width = kwargs['width_entry'],
                           height = kwargs['height_entry'],
                           border_color = kwargs['border_color_entry'],
                           border_width = kwargs['border_width_entry'],
                           background_color = kwargs['bgcolor_entry'])
        self.password_label = Label(window = self.root,
                         text = kwargs['text_password'],
                         posx = kwargs['posx_password'],
                         posy = kwargs['posy_password'], 
                         text_color= kwargs['color_label'],
                         font_size = kwargs['font_size_otherwise_label'],
                         font_style = kwargs['font_style_label'])
        self.entry_password = Entry(window = self.root,
                           placeholder = kwargs['entry_PW_placeholder'],
                           posx = kwargs['entry_password_posx'],
                           posy = kwargs['entry_password_posy'],
                           text_color = kwargs['color_entry'],
                           font_size = kwargs['font_size_entry'],
                           font_style = kwargs['font_style_entry'],
                           width = kwargs['width_entry'],
                           height = kwargs['height_entry'],
                           border_color = kwargs['border_color_entry'],
                           border_width = kwargs['border_width_entry'],
                           background_color = kwargs['bgcolor_entry'])
        self.password_label_confirm = Label(window = self.root,
                         text = kwargs['text_passwordC'],
                         posx = kwargs['posx_passwordC'],
                         posy = kwargs['posy_passwordC'], 
                         text_color= kwargs['color_label'],
                         font_size = kwargs['font_size_otherwise_label'],
                         font_style = kwargs['font_style_label'])
        self.entry_password_confirm = Entry(window = self.root,
                           placeholder = kwargs['entry_PW_placeholder'],
                           posx = kwargs['entry_passwordC_posx'],
                           posy = kwargs['entry_passwordC_posy'],
                           text_color = kwargs['color_entry'],
                           font_size = kwargs['font_size_entry'],
                           font_style = kwargs['font_style_entry'],
                           width = kwargs['width_entry'],
                           height = kwargs['height_entry'],
                           border_color = kwargs['border_color_entry'],
                           border_width = kwargs['border_width_entry'],
                           background_color = kwargs['bgcolor_entry'])
        self.email = Label(window = self.root,
                         text = kwargs['email'],
                         posx = kwargs['posx_email'],
                         posy = kwargs['posy_email'], 
                         text_color= kwargs['color_label'],
                         font_size = kwargs['font_size_otherwise_label'],
                         font_style = kwargs['font_style_label'])
        self.entry_email = Entry(window = self.root,
                           placeholder = kwargs['entry_email_placeholder'],
                           posx = kwargs['entry_email_posx'],
                           posy = kwargs['entry_email_posy'],
                           text_color = kwargs['color_entry'],
                           font_size = kwargs['font_size_entry'],
                           font_style = kwargs['font_style_entry'],
                           width = kwargs['width_entry'],
                           height = kwargs['height_entry'],
                           border_color = kwargs['border_color_entry'],
                           border_width = kwargs['border_width_entry'],
                           background_color = kwargs['bgcolor_entry'])
        self.error_label = Label(window = self.root,
                                 text = '',
                                 posx = kwargs['error_posx'],
                                 posy = kwargs['error_posy'],
                                 text_color = args.pattern_style['error_color'],
                                 font_size = 13,
                                 font_style = 'arial')
        self.phone = Label(window = self.root,
                         text = kwargs['phone_text'],
                         posx = kwargs['posx_phone'],
                         posy = kwargs['posy_phone'], 
                         text_color= kwargs['color_label'],
                         font_size = kwargs['font_size_otherwise_label'],
                         font_style = kwargs['font_style_label'])
        self.entry_phone = Entry(window = self.root,
                           placeholder = kwargs['entry_phone_placeholder'],
                           posx = kwargs['entry_phone_posx'],
                           posy = kwargs['entry_phone_posy'],
                           text_color = kwargs['color_entry'],
                           font_size = kwargs['font_size_entry'],
                           font_style = kwargs['font_style_entry'],
                           width = kwargs['width_entry'],
                           height = kwargs['height_entry'],
                           border_color = kwargs['border_color_entry'],
                           border_width = kwargs['border_width_entry'],
                           background_color = kwargs['bgcolor_entry'])
        self.hide_control = ctk.StringVar(value = 'off')
        self.hide = ctk.CTkCheckBox(self.root,
                                        text = 'show password',
                                        onvalue = 'on',
                                        offvalue = 'off',
                                        variable = self.hide_control,
                                        command = self.hide_method,
                                        checkbox_height = kwargs['checkbox_size'],
                                        checkbox_width = kwargs['checkbox_size'],
                                        fg_color = args.pattern_style['main_color'],
                                        hover_color = args.pattern_style['main_color'],
                                        border_color = args.pattern_style['main_color'],
                                        text_color = args.pattern_style['main_color']
                                        )
        self.hide.place(relx = kwargs['pos_hide_x'], rely = kwargs['pos_hide_y'], anchor = 'center')
        self.button = ctk.CTkButton(self.root,
                                        text = kwargs['button_text'],
                                        fg_color = kwargs['color_of_button'],
                                        hover_color = kwargs['hover_color'],
                                        command = self.send,
                                        width = kwargs['button_width'],
                                        height = kwargs['button_height'],
                                        font = (kwargs['font_style_button'], kwargs['font_size_button']),
                                        text_color = kwargs['button_text_color'],
                                        border_width = kwargs['border_w'],
                                        border_color = kwargs['border_color'])
        self.button.place(relx = kwargs['button_posx'], rely = kwargs['button_posy'], anchor = 'center')

    def hide_method(self):
        if self.hide_control.get() == 'on':
            self.entry_password.entry.configure(show = '*')
            self.entry_password_confirm.entry.configure(show = '*')
        else:
            self.entry_password.entry.configure(show = '')
            self.entry_password_confirm.entry.configure(show = '')
    #This method will insert input new data to the database
    def send(self):
        self.no_problem = False
        try:
            username = self.entry_user.entry.get()
            pw = self.entry_password.entry.get()
            pw_confirm = self.entry_password_confirm.entry.get()
            email = self.entry_email.entry.get()
            phone = self.entry_phone.entry.get()
            if '' in (username, pw, pw_confirm, email, phone):
                self.error_label.label.configure(text = "ERROR: You've forgotten to fill a box")
            elif pw != pw_confirm:
                self.error_label.label.configure(text = "ERROR: confirmation password doesn't match")
            elif not phone.isdigit():
                self.error_label.label.configure(text = 'ERROR: Phone number must be numeric, nothing else')
            elif username in SQL_CRUD.all_users_name():
                self.error_label.label.configure(text = 'ERROR: This username already exist')
            else:
                self.no_problem = True
                SQL_CRUD.insert_user(username, pw, email, phone)
        except:
            self.error_label.label.configure(text = "ERROR: Can't insert the data. Try again")
        else:
            if self.no_problem == True:
                self.root.destroy() #Closes the register window
                self.success = Success('Ico_Files/for_test.ico', 'Password Management System ErickDev', text = "YOU'VE REGISTERED SUCCESFULLY")
                self.success.open_window()

class Success(Window):

    def __init__(self, icon_path, title,  text, msg_size = 20, border_w = 4, border_color = args.pattern_style['border_button_color']):
        super().__init__(args.window_size['Success'][0], args.window_size['Success'][1], icon_path, title)
        self.mesage = Label(self.root,
                posx = args.pos['Success']['button'][0],
                posy = args.pos['Success']['button'][1],
                text_color = args.pattern_style['main_color'],
                text = text,
                font_size = 20,
                font_style = args.pattern_style['main_font'])
        ok_button = ctk.CTkButton(self.root,
                                        width = 40,
                                        height = 40,
                                        font = (args.pattern_style['main_font'], msg_size),
                                        fg_color = args.pattern_style['main_color'],
                                        hover_color = args.pattern_style['button_hover_color'],
                                        text = 'OK',
                                        text_color = args.pattern_style['button_label_color'],
                                        command = self.close_success_window,
                                        border_width = border_w,
                                        border_color = border_color)
        ok_button.place(relx = args.pos['Success']['label'][0], rely = args.pos['Success']['label'][1], anchor = 'center')

    def close_success_window(self):
        self.root.destroy()

class Error_Window(Window):

    def __init__(self, width, height, icon_path, title, text, **kwargs):
        super().__init__(width, height, icon_path, title)
        self.label = Label(self.root,
                    posx = kwargs['pos_x_label'],
                    posy = kwargs['pos_y_label'],
                    text_color = args.pattern_style['error_color'],
                    text = text,
                    font_size = 20,
                    font_style = args.pattern_style['main_font'])
        self.button = ctk.CTkButton(self.root,
                                        width = 40,
                                        height = 40,
                                        font = (args.pattern_style['main_font'], 20),
                                        fg_color = 'tomato',
                                        hover_color = 'orangered',
                                        text = 'OK',
                                        text_color = args.pattern_style['button_label_color'],
                                        command = self.close,
                                        border_width = kwargs['border_w'],
                                        border_color = kwargs['border_color'])
        self.button.place(relx = kwargs['pos_x_button'], rely = kwargs['pos_y_button'], anchor = 'center')
        self.IMG1 = Img(self.root, width = 20, height = 20, path = 'images/Error.png', posx = kwargs['img1x'], posy = kwargs['img1y'])
        self.IMG1 = Img(self.root, width = 20, height = 20, path = 'images/Error.png', posx = kwargs['img2x'], posy = kwargs['img2y'])

    def close(self):
        self.root.destroy()

class Show_Window(Window):

    def __init__(self, width, height, icon_path, title, id_user, **kwargs):
        super().__init__(width, height, icon_path, title)
        self.label = Label(self.root,
                           text = kwargs['text'],
                           text_color = kwargs['pattern_color'],
                           font_size = kwargs['text_font_size'],
                           font_style = kwargs['text_font_size'],
                           posx = kwargs['text_posx'],
                           posy = kwargs['text_posy'])
        self.lbutton = ctk.CTkButton(self.root,
                                     width = kwargs['wbutton'],
                                     height = kwargs['hbutton'],
                                     text = 'SINGULAR DATA',
                                     text_color = args.pattern_style['button_label_color'],
                                     fg_color = kwargs['pattern_color'],
                                     command = self.singular,
                                     font = (kwargs['font_style'] ,kwargs['button_text_font_size']),
                                     hover_color = kwargs['button_hover_color'],
                                     border_width = kwargs['border_w'],
                                     border_color = kwargs['border_color'])
        self.lbutton.place(relx = kwargs['left_button_posx'], rely = kwargs['button_posy'], anchor = 'center')
        self.rbutton = ctk.CTkButton(self.root,
                                     width = kwargs['wbutton'],
                                     height = kwargs['hbutton'],
                                     text = 'EVERY DATA',
                                     text_color = args.pattern_style['button_label_color'],
                                     fg_color = kwargs['pattern_color'],
                                     command = self.every,
                                     font = (kwargs['font_style'] ,kwargs['button_text_font_size']),
                                     hover_color = kwargs['button_hover_color'],
                                     border_width = kwargs['border_w'],
                                     border_color = kwargs['border_color'])
        self.rbutton.place(relx = kwargs['right_button_posx'], rely = kwargs['button_posy'], anchor = 'center')
        if  kwargs['green_card']:
            self.data_posx = kwargs['data_posx']
            self.data_posy = kwargs['data_posy']
            self.txt = ctk.CTkTextbox(self.root,
                                        fg_color = 'black',
                                        width = kwargs['box_width'],
                                        height = kwargs['box_height'],
                                        font = (kwargs['font_style'], kwargs['data_size']),
                                        border_width = 5,
                                        border_color = kwargs['pattern_color'])
            self.txt.place(relx = self.data_posx, rely = self.data_posy, anchor = 'center')
        self.box_posx = kwargs['box_posx']
        self.box_posy = kwargs['box_posy']
        self.id_user = id_user
        self.basic_values = SQL_CRUD.plat_name(self.id_user)
        self.val = ['| '*15]
        self.val_extra = [f'{data[0]:<10} | {data[1]:^10}' for data in self.basic_values]
        self.val.extend(self.val_extra)

        self.box = ctk.CTkComboBox(self.root,
                                   values = self.val,
                                   width = 400,
                                   height = 50,
                                   dropdown_fg_color = 'black',
                                   dropdown_text_color = 'white',
                                   font = (args.pattern_style['main_font'], 20),
                                   dropdown_font = (args.pattern_style['main_font'], 20),
                                   command = self.choose,
                                   fg_color = 'black',
                                   button_color = kwargs['pattern_color'],
                                   button_hover_color = kwargs['button_hover_color'],
                                   border_color = kwargs['pattern_color'])
        self.box.place(relx = self.box_posx, rely = self.box_posy, anchor = 'center')
        self.data_final_y = args.pos['Show']['data_final_y']
        self.box_final_y = args.pos['Show']['box_final_y']

    def singular(self):
        #y position of the text box goes from 0.6 to 0.7
        if self.data_posy < self.data_final_y:
            self.data_posy += 0.005
            self.txt.place(relx = self.data_posx, rely = self.data_posy, anchor = 'center')
            self.txt.after(30, self.singular)
        if self.box_posx < self.box_final_y:
            self.box_posx += 0.005
            self.box.place(relx = self.box_posx, rely = self.box_posy, anchor = 'center')
            self.box.after(30, self.singular)

    def choose(self, arg):
        if len(self.txt.get(0.0, 'end')) > 0:
            self.txt.delete(0.0, 'end')
        friend_list = arg.split()
        friend_list.remove('|')
        text = ''
        #Our friend_list has the platform as first item and username as second item
        all_data = SQL_CRUD.plat_name_pw(self.id_user)
        if len(all_data) != 0:
            for data in all_data:
                if friend_list[0] == data[0] and friend_list[1] == data[1]:
                    text += f'Platform: {data[0]}\nUsername: {data[1]}\nPassword: {data[2]}\n' + '.'*40 + '\n'
        else:
            text += 'There is no data available'
        self.txt.insert('end', text)

    def every(self):
        if len(self.txt.get(0.0, 'end')) > 0:
            self.txt.delete(0.0, 'end')
        text = ''
        all_data = SQL_CRUD.plat_name_pw(self.id_user)
        if len(all_data) != 0:
            for data in all_data:
                text += f'Platform: {data[0]}\nUsername: {data[1]}\nPassword: {data[2]}\n' + '.'*40 + '\n'
        else:
            text += 'There is no data available'
        self.txt.insert('end', text)

class Delete_Window(Show_Window):

    option = None #Delete everything: 1(Delete something: 0)

    def __init__(self, width, height, icon_path, title, id_user, **kwargs):
        super().__init__(width, height, icon_path, title, id_user,
                         left_button_posx = kwargs['left_button_posx'],
                         right_button_posx = kwargs['right_button_posx'],
                         button_posy = kwargs['button_posy'],
                         text = kwargs['text'],
                         pattern_color = kwargs['pattern_color'],
                         text_font_size = kwargs['text_font_size'],
                         text_posx = kwargs['text_posx'],
                         text_posy = kwargs['text_posy'],
                         data_posx = None,data_posy = None,
                         font_style = kwargs['font_style'], 
                         data_size = None,
                         box_width = kwargs['box_width'],
                         box_height = kwargs['box_height'],
                         button_hover_color = kwargs['button_hover_color'],
                         wbutton = kwargs['wbutton'],
                         hbutton = kwargs['hbutton'],
                         button_text_font_size = kwargs['button_text_font_size'],
                         box_posy = kwargs['box_posy'],
                         box_posx = kwargs['box_posx'],
                         green_card = False,
                         border_w = None,
                         border_color = None)
        self.font_style = kwargs['font_style']
        self.msg_text = kwargs['msg_text']
        self.pattern_color = kwargs['pattern_color']
        self.button_hover_color = kwargs['button_hover_color']
        self.border_w = kwargs['border_w']
        self.border_color = kwargs['border_color']
        self.delx = kwargs['delx']
        self.dely = kwargs['dely']
        self.msg_x = kwargs['msg_x']
        self.msg_y = kwargs['msg_y']
        self.att_x = kwargs['att_x']
        self.att_y = kwargs['att_y']
        self.final_position_del_y = kwargs['final_position_del_y']
        self.final_position_box_y = kwargs['final_position_box_y']
        self.del_button = ctk.CTkButton(self.root,
                                        text = 'DELETE',
                                        font = (kwargs['font_style'], 20),
                                        text_color = args.pattern_style['button_label_color'],
                                        hover_color = self.button_hover_color,
                                        fg_color = self.pattern_color,
                                        width = kwargs['del_width'],
                                        height = kwargs['del_height'],
                                        command = self.confirm,
                                        border_width = self.border_w,
                                        border_color = self.border_color)
        self.del_button.place(relx = self.delx, rely = self.dely)
        self.att = ctk.CTkLabel(self.root,
                                text = 'ATTENTION',
                                text_color = args.pattern_style['error_color'],
                                font = (self.font_style, 40))
        self.att.place(relx =  self.att_x, rely = self.att_y, anchor = 'center')
        self.msg = ctk.CTkLabel(self.root,
                                text = self.msg_text,
                                text_color = 'white',
                                font = (self.font_style, 20))
        self.msg.place(relx = self.msg_x, rely = self.msg_y, anchor = 'center')
    
    def singular(self):
        Delete_Window.option = 0
        if self.att_x > -1.5 and self.msg_x > -1.5:
            self.att_x -= 0.05
            self.msg_x -= 0.05
            self.att.place(relx = self.att_x, rely = self.att_y, anchor = 'center')
            self.msg.place(relx = self.msg_x, rely = self.msg_y, anchor = 'center')
            self.root.after(10, self.singular)
        elif self.box_posy > self.final_position_box_y:
            self.box_posy -= 0.05
            self.box.place(relx = self.box_posx, rely = self.box_posy, anchor = 'center')
            self.box.after(10, self.singular)
        elif self.dely > self.final_position_del_y:
            self.dely -= 0.05
            self.del_button.place(relx = self.delx, rely = self.dely, anchor = 'center')
            self.del_button.after(10, self.singular)

    def every(self):
        Delete_Window.option = 1
        self.confirm()

    def confirm(self):
        self.root_confirm = ctk.CTk()
        self.root_confirm.geometry(f'{args.window_size['Delete_Data_Confirm'][0]}x{args.window_size['Delete_Data_Confirm'][1]}')
        self.root_confirm.resizable(False, False)
        self.root_confirm.iconbitmap('Ico_Files/for_test.ico')
        self.root_confirm.title('PMS delete confirmation')
        self.label = ctk.CTkLabel(self.root_confirm,
                           text = 'ARE YOU SURE YOU WANT TO DELETE THE DATA?',
                           font = (self.font_style, 25),
                           text_color = self.pattern_color)
        self.label.place(relx = args.pos['Delete_Data_Confirm']['title_question'][0], rely = args.pos['Delete_Data_Confirm']['title_question'][1], anchor = 'center')
        self.attention = ctk.CTkLabel(self.root_confirm,
                                text = 'ATTENTION',
                                text_color = args.pattern_style['error_color'],
                                font = (self.font_style, 50))
        self.attention.place(relx = args.pos['Delete_Data_Confirm']['attention_label'][0], rely = args.pos['Delete_Data_Confirm']['attention_label'][1], anchor = 'center')
        self.msg_ = ctk.CTkLabel(self.root_confirm,
                                text = self.msg_text,
                                text_color = 'white',
                                font = (self.font_style, 20))
        self.msg_.place(relx = args.pos['Delete_Data_Confirm']['msg_label'][0], rely = args.pos['Delete_Data_Confirm']['msg_label'][1], anchor = 'center')
        self.yes_ = ctk.CTkButton(self.root_confirm,
                                 text = 'YES',
                                 command = self.yes,
                                 text_color = args.pattern_style['button_label_color'],
                                 fg_color = self.pattern_color,
                                 hover_color = self.button_hover_color,
                                 font = (self.font_style, 30),
                                 border_color = self.border_color,
                                 border_width = self.border_w)
        self.yes_.place(relx = args.pos['Delete_Data_Confirm']['yes_button'][0], rely = args.pos['Delete_Data_Confirm']['yes_button'][1], anchor = 'center')
        self.cancel_ = ctk.CTkButton(self.root_confirm,
                                 text = 'CANCEL',
                                 command = self.cancel,
                                 text_color = args.pattern_style['button_label_color'],
                                 fg_color = self.pattern_color,
                                 hover_color = self.button_hover_color,
                                 font = (self.font_style, 30),
                                 border_color = self.border_color,
                                 border_width = self.border_w)
        self.cancel_.place(relx = args.pos['Delete_Data_Confirm']['cancel_button'][0], rely = args.pos['Delete_Data_Confirm']['cancel_button'][1], anchor = 'center')
        self.root_confirm.mainloop()

    def yes(self):
        if Delete_Window.option == 0:
            self.plat_user_list = self.box.get().split()
            self.plat_user_list.remove('|')
            SQL_CRUD.delete_pw(id_user = self.id_user,
                               platform = self.plat_user_list[0],
                               username = self.plat_user_list[1])
            self.root_confirm.destroy()
        if Delete_Window.option == 1:
            SQL_CRUD.delete_all(self.id_user)
            self.root_confirm.destroy()
        self.success = Success('Ico_Files/for_test.ico', 'Password Management System ErickDev', text = 'PASSWORD DELETED SUCCESFULLY')
        self.success.open_window()
        
    def cancel(self):
        self.root_confirm.destroy()

class Option_Window(Window):

    gen_clicked = 'off'

    def __init__(self, width, height, icon_path, title, id_user, **kwargs):
        super().__init__(width, height, icon_path, title)
        self.id_user = id_user
        self.font_style = kwargs['font_style']
        self.pattern_color = kwargs['pattern_color']
        self.hover_color = kwargs['hover_color']
        self.border_w = kwargs['border_w']
        self.border_color = kwargs['border_color']
        self.pw_labelx = args.pos['Option']['pw_label'][0]
        self.pw_labely = args.pos['Option']['pw_label'][1]
        self.pw_hidex = args.pos['Option']['pw_hide'][0]
        self.pw_hidey = args.pos['Option']['pw_hide'][1]
        self.pw_copy_x = args.pos['Option']['pw_copy'][0]
        self.pw_copy_y = args.pos['Option']['pw_copy'][1]
        self.checkboxx = args.pos['Option']['box'][0]
        self.checkboxy = args.pos['Option']['box'][1]
        self.pw_label_final_y = args.pos['Option']['pw_label_final_y']
        self.pw_copy_final_y = args.pos['Option']['pw_copy_final_y']
        self.pw_hide_final_y = args.pos['Option']['pw_hide_final_y']
        self.pw_box_final_y = args.pos['Option']['pw_box_final_y']
        self.label = Label(self.root,
                           text = kwargs['text'],
                           posx = kwargs['posx_label'],
                           posy = kwargs['posy_label'],
                           font_size = kwargs['font_size_label'],
                           font_style = self.font_style,
                           text_color = self.pattern_color)
        self.store_ = ctk.CTkButton( self.root,
                                    text = 'Store Data',
                                    text_color = kwargs['button_text_color'],
                                    fg_color = self.pattern_color,
                                    width = kwargs['width_button'],
                                    height = kwargs['height_button'],
                                    command = self.store,
                                    hover_color = self.hover_color,
                                    font = (self.font_style, kwargs['font_size']),
                                    border_width = self.border_w,
                                    border_color = self.border_color)
        self.store_.place(relx = kwargs['posx_button1'], rely = kwargs['posy_button1'], anchor = 'center')
        self.access_ = ctk.CTkButton(self.root,
                                    text = 'Access Data',
                                    text_color = kwargs['button_text_color'],
                                    fg_color = self.pattern_color,
                                    width = kwargs['width_button'],
                                    height = kwargs['height_button'],
                                    command = self.access,
                                    hover_color = self.hover_color,
                                    font = (self.font_style, kwargs['font_size']),
                                    border_width = self.border_w,
                                    border_color = self.border_color)
        self.access_.place(relx = kwargs['posx_button2'], rely = kwargs['posy_button2'], anchor = 'center')
        self.delete_data_ = ctk.CTkButton(self.root,
                                   text = 'Delete Data',
                                   text_color = kwargs['button_text_color'],
                                   fg_color = self.pattern_color,
                                   width = kwargs['width_button'],
                                   height = kwargs['height_button'],
                                   command = self.delete_data,
                                   hover_color = self.hover_color,
                                   font = (self.font_style, kwargs['font_size']),
                                   border_width = self.border_w,
                                   border_color = self.border_color)
        self.delete_data_.place(relx = kwargs['posx_button3'], rely = kwargs['posy_button3'], anchor = 'center')
        self.delete_account = ctk.CTkButton(self.root,
                                   text = 'Delete Account',
                                   text_color = kwargs['button_text_color'],
                                   fg_color = self.pattern_color,
                                   width = kwargs['width_button'],
                                   height = kwargs['height_button'],
                                   command = self.delete_ac_confirmation,
                                   hover_color = self.hover_color,
                                   font = (self.font_style, kwargs['font_size']),
                                   border_width = self.border_w,
                                   border_color = self.border_color)
        self.delete_account.place(relx = kwargs['posx_button4'], rely = kwargs['posy_button4'], anchor = 'center')
        self.gen_ = ctk.CTkButton(self.root,
                                  text = 'Generate',
                                  text_color = args.pattern_style['button_label_color'],
                                  fg_color = self.pattern_color,
                                  width = kwargs['width_button'],
                                  height = kwargs['height_button'],
                                  command = self.gen,
                                  font = (self.font_style, kwargs['font_size']),
                                  border_width = self.border_w,
                                  border_color = self.border_color,
                                  hover_color = self.hover_color)
        self.gen_.place(relx = kwargs['posx_button5'], rely = kwargs['posy_button5'], anchor = 'center')
        self.pw_label = ctk.CTkLabel(self.root,
                                     text = '',
                                     font = (self.font_style, 20),
                                     text_color = self.pattern_color)
        self.pw_label.place(relx = self.pw_labelx, rely = self.pw_labely, anchor = 'center')
        self.pw_hide = ctk.CTkLabel(self.root,
                                     text = f'password: {'*'*16}',
                                     font = (self.font_style, 20),
                                     text_color = self.pattern_color)
        self.pw_hide.place(relx = self.pw_hidex, rely = self.pw_hidey, anchor = 'center')
        self.copy_ = ctk.CTkButton(self.root,
                                 text = 'COPY',
                                 font = (self.font_style, 20),
                                 text_color = args.pattern_style['button_label_color'],
                                 fg_color = self.pattern_color,
                                 command = self.copy,
                                 border_color = self.border_color,
                                 border_width = self.border_w/2,
                                 width = 50,
                                 height = 20,
                                 hover_color = self.hover_color)
        self.copy_.place(relx = self.pw_copy_x, rely = self.pw_copy_y, anchor = 'center')
        self.control_ = ctk.StringVar(value = 'on')
        self.checkbox = ctk.CTkCheckBox(self.root,
                                        text = 'password hidden',
                                        variable = self.control_,
                                        onvalue = 'on',
                                        offvalue = 'off',
                                        command = self.control,
                                        fg_color = self.pattern_color,
                                        text_color = self.pattern_color,
                                        font = (self.font_style, 20),
                                        corner_radius = 100,
                                        width = 20,
                                        height = 20,
                                        hover_color = self.hover_color)
        self.checkbox.place(relx = self.checkboxx, rely = self.checkboxy, anchor = 'center')

    def store(self):
        self.store_window = Store_Window(args.window_size['Store'][0], args.window_size['Store'][1], 'Ico_Files/for_test.ico', 'Password Management System ErickDev', self.id_user,
                                         font_size_title_label = 60,
                                         font_size_otherwise_label = 30,
                                         font_style_label = args.pattern_style['main_font'],
                                         text_title = 'STORE',
                                         posx_title = args.pos['Store']['title'][0],
                                         posy_title = args.pos['Store']['title'][1],
                                         color_label = args.pattern_style['main_color'],
                                         text_user = 'Username', posx_user = args.pos['Store']['user_label'][0],
                                         posy_user = args.pos['Store']['user_label'][1],
                                         entry_user_placeholder = 'Type your username here',
                                         entry_user_posx = args.pos['Store']['user_entry'][0],
                                         entry_user_posy = args.pos['Store']['user_entry'][1],
                                         color_entry = 'white',
                                         bgcolor_entry = 'black',
                                         border_color_entry = args.pattern_style['main_color'],
                                         border_width_entry = 4,
                                         font_style_entry = args.pattern_style['main_font'],
                                         hover_color_button = args.pattern_style['button_hover_color'],
                                         font_size_entry = 20,
                                         width_entry = 400,
                                         height_entry = 50,
                                         text_password = 'Password',
                                         posx_password = args.pos['Store']['password_label'][0],
                                         posy_password = args.pos['Store']['password_label'][1],
                                         entry_password_posx = args.pos['Store']['password_entry'][0],
                                         entry_password_posy = args.pos['Store']['password_entry'][1],
                                         pos_hide_x = args.pos['Store']['hide'][0],
                                         pos_hide_y = args.pos['Store']['hide'][1],
                                         button_text = 'SUBMIT',
                                         button_text_create = 'CREATE ACCOUNT',
                                         color_of_button = args.pattern_style['main_color'],
                                         button_width = 332,
                                         button_height = 50,
                                         font_size = 40,
                                         font_style_button = args.pattern_style['main_font'],
                                         button_text_color = args.pattern_style['button_label_color'],
                                         button_posx = args.pos['Store']['button'][0],
                                         button_posy = args.pos['Store']['button'][1],
                                         checkbox_size = 20,
                                         button_posy_create = None,
                                         error_label_text = '',
                                         error_label_color = args.pattern_style['error_color'],
                                         error_label_posx = args.pos['Store']['error'][0],
                                         error_label_posy = args.pos['Store']['error'][1],
                                         font_error = 20, 
                                         text_plat = 'Platform',
                                         posx_plat = args.pos['Store']['platform_label'][0],
                                         posy_plat = args.pos['Store']['platform_label'][0],
                                         entry_plat_posx = args.pos['Store']['platform_entry'][0],
                                         entry_plat_posy = args.pos['Store']['platform_entry'][1])
        self.store_window.open_window()
        
    def access(self):
        self.show_window = Show_Window(args.window_size['Show'][0], args.window_size['Show'][1], 'Ico_Files/for_test.ico', 'Password Management System ErickDev',
                                       id_user = self.id_user,
                                       left_button_posx = args.pos['Show']['left_button'][0],
                                       right_button_posx = args.pos['Show']['right_button'][0],
                                       button_posy = args.pos['Show']['left_button'][1],
                                       text = 'CHOOSE AN OPTION',
                                       pattern_color = args.pattern_style['main_color'],
                                       text_font_size = 40, text_posx = args.pos['Show']['title'][0],
                                       text_posy = args.pos['Show']['title'][1],
                                       data_posx = args.pos['Show']['data'][0],
                                       data_posy = args.pos['Show']['data'][1],
                                       font_style = args.pattern_style['main_font'],
                                       data_size = 15,
                                       box_width = 400,
                                       box_height = 400,
                                       button_hover_color = args.pattern_style['button_hover_color'],
                                       wbutton = 100,
                                       hbutton = 50,
                                       button_text_font_size = 20,
                                       box_posy = args.pos['Show']['box'][1],
                                       box_posx = args.pos['Show']['box'][0],
                                       green_card = True,
                                       border_w = 4,
                                       border_color = args.pattern_style['border_button_color'])
        self.show_window.open_window()

    def delete_data(self):
        self.delete_window = Delete_Window(args.window_size['Delete'][0], args.window_size['Delete'][1], 'Ico_Files/for_test.ico', 'Password Management System ErickDev',
                                           id_user = self.id_user,
                                           left_button_posx = args.pos['Delete']['left_button'][0],
                                           right_button_posx = args.pos['Delete']['right_button'][0],
                                           button_posy = args.pos['Delete']['right_button'][1],
                                           text = 'CHOOSE AN OPTION',
                                           pattern_color = args.pattern_style['main_color'],
                                           text_font_size = 40, 
                                           text_posx = args.pos['Delete']['text'][0],
                                           text_posy = args.pos['Delete']['text'][1],
                                           font_style = args.pattern_style['main_font'],
                                           box_width = 400,
                                           box_height = 400,
                                           button_hover_color = args.pattern_style['button_hover_color'],
                                           wbutton = 100,
                                           hbutton = 50,
                                           button_text_font_size = 20,
                                           box_posy = args.pos['Delete']['box'][1],
                                           box_posx = args.pos['Delete']['box'][0],
                                           delx = args.pos['Delete']['del'][0],
                                           dely = args.pos['Delete']['del'][1],
                                           msg_x = args.pos['Delete']['msg'][0],
                                           msg_y = args.pos['Delete']['msg'][1],
                                           att_x = args.pos['Delete']['att'][0],
                                           att_y = args.pos['Delete']['att'][1],
                                           del_width = 100,
                                           del_height = 50,
                                           msg_text = "Be careful, once you've\n deleted a set of data, you\n won't be able to recover it",
                                           border_w = 4,
                                           border_color = args.pattern_style['border_button_color'],
                                           final_position_del_y = args.pos['Delete']['final_position_del_y'],
                                           final_position_box_y = args.pos['Delete']['final_position_box_y'])
        self.delete_window.open_window()

    def delete_ac_confirmation(self):
        self.root_confirm = ctk.CTk()
        self.root_confirm.geometry(f'{args.window_size['Delete_Account_Confirm'][0]}x{args.window_size['Delete_Account_Confirm'][1]}')
        self.root_confirm.resizable(False, False)
        self.root_confirm.iconbitmap('Ico_Files/for_test.ico')
        self.root_confirm.title('PMS delete confirmation')
        self.msg_text = 'Be carefule, if you delete your\n account there will not be\n any way to recover it back'
        self.label = ctk.CTkLabel(self.root_confirm,
                           text = 'ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT?',
                           font = (self.font_style, 25),
                           text_color = self.pattern_color)
        self.label.place(relx = args.pos['Delete_Account_Confirm']['title_question'][0], rely = args.pos['Delete_Account_Confirm']['title_question'][1], anchor = 'center')
        self.attention = ctk.CTkLabel(self.root_confirm,
                                text = 'ATTENTION',
                                text_color = args.pattern_style['error_color'],
                                font = (self.font_style, 50))
        self.attention.place(relx = args.pos['Delete_Account_Confirm']['attention_label'][0], rely = args.pos['Delete_Account_Confirm']['attention_label'][1], anchor = 'center')
        self.msg = ctk.CTkLabel(self.root_confirm,
                                text = self.msg_text,
                                text_color = 'white',
                                font = (self.font_style, 20))
        self.msg.place(relx = args.pos['Delete_Account_Confirm']['msg_label'][0], rely = args.pos['Delete_Account_Confirm']['msg_label'][1], anchor = 'center')
        self.yes_ = ctk.CTkButton(self.root_confirm,
                                 text = 'YES',
                                 command = self.yes,
                                 text_color = args.pattern_style['button_label_color'],
                                 fg_color = self.pattern_color,
                                 hover_color = self.hover_color,
                                 font = (self.font_style, 30),
                                 border_width = self.border_w,
                                 border_color = self.border_color)
        self.yes_.place(relx = args.pos['Delete_Account_Confirm']['yes_button'][0], rely = args.pos['Delete_Account_Confirm']['yes_button'][1], anchor = 'center')
        self.cancel_ = ctk.CTkButton(self.root_confirm,
                                 text = 'CANCEL',
                                 command = self.cancel,
                                 text_color = args.pattern_style['button_label_color'],
                                 fg_color = self.pattern_color,
                                 hover_color = self.hover_color,
                                 font = (self.font_style, 30),
                                 border_width = self.border_w,
                                 border_color = self.border_color)
        self.cancel_.place(relx = args.pos['Delete_Account_Confirm']['cancel_button'][0], rely = args.pos['Delete_Account_Confirm']['cancel_button'][1], anchor = 'center')
        self.root_confirm.mainloop()

    def cancel(self):
        self.root_confirm.destroy()
    
    def yes(self):
        SQL_CRUD.delete_user(Login_Window.user)
        self.root.destroy()
        self.root_confirm.destroy()
        self.success = Success('Ico_Files/for_test.ico', 'Password Management System ErickDev', text = 'USER DELETED SUCCESFULLY')
        self.success.open_window()
    
    def gen(self):
        if Option_Window.gen_clicked == 'off':
            Option_Window.gen_clicked = 'on'
            self.gen_.configure(state = 'disabled')
        if self.pw_labely > self.pw_label_final_y and self.pw_hidey > self.pw_hide_final_y:
            self.pw_labely -= 0.01
            self.pw_hidey -= 0.01
            self.pw_label.place(relx = self.pw_labelx, rely = self.pw_labely, anchor = 'center')
            self.pw_hide.place(relx = self.pw_hidex, rely = self.pw_hidey, anchor = 'center')
            self.root.after(10, self.gen)
        elif self.pw_copy_y > self.pw_copy_final_y and self.checkboxy > self.pw_box_final_y:
            self.pw_copy_y -= 0.01
            self.checkboxy -= 0.01
            self.copy_.place(relx = self.pw_copy_x, rely = self.pw_copy_y, anchor = 'center')
            self.checkbox.place(relx = self.checkboxx, rely = self.checkboxy, anchor = 'center')
            self.root.after(10, self.gen)
        else:
            self.new_pw = pw_generator.new_password(16)
            self.pw_label.configure(text = f'password: {self.new_pw}')

    def copy(self):
        pyperclip.copy(self.new_pw)

    def control(self):
        if self.control_.get() == 'on':
            self.checkbox.configure(text = 'password hidden')
            self.pw_hide.configure(text = f'password: {'*'*16}')
        else:
            self.checkbox.configure(text = 'hide password')
            self.pw_hide.configure(text = '')
        
if __name__ == '__main__':
    if SQL_CRUD.connected():
        SQL_CRUD.create()
        login = Login_Window(args.window_size['Login'][0], args.window_size['Login'][1], 'Ico_Files/for_test.ico', 'Password Management System ErickDev',
                             font_size_title_label = 60,
                             font_size_otherwise_label = 30,
                             font_style_label = args.pattern_style['main_font'],
                             text_title = 'WELCOME',
                             posx_title = args.pos['Login']['title'][0],
                             posy_title = args.pos['Login']['title'][1],
                             color_label = args.pattern_style['main_color'],
                             text_user = 'Username',
                             posx_user = args.pos['Login']['user_label'][0],
                             posy_user = args.pos['Login']['user_label'][1],
                             entry_user_placeholder = 'Type your username here',
                             entry_user_posx = args.pos['Login']['user_entry'][0],
                             entry_user_posy = args.pos['Login']['user_entry'][1],
                             color_entry = 'white',
                             bgcolor_entry = 'black',
                             border_color_entry = args.pattern_style['main_color'],
                             border_width_entry = 4,
                             font_style_entry = args.pattern_style['main_font'],
                             hover_color_button = args.pattern_style['button_hover_color'],
                             font_size_entry = 20,
                             width_entry = 400,
                             height_entry = 50,
                             text_password = 'Password',
                             posx_password = args.pos['Login']['password_label'][0],
                             posy_password = args.pos['Login']['password_label'][1],
                             entry_password_posx = args.pos['Login']['password_entry'][0],
                             entry_password_posy = args.pos['Login']['password_entry'][1],
                             pos_hide_x = args.pos['Login']['hide_box'][0],
                             pos_hide_y = args.pos['Login']['hide_box'][1],
                             button_text = 'SUBMIT',
                             button_text_create = 'CREATE ACCOUNT',
                             color_of_button = args.pattern_style['main_color'],
                             button_width = 332,
                             button_height = 50,
                             font_size = 40,
                             font_style_button = args.pattern_style['main_font'],
                             button_text_color = args.pattern_style['button_label_color'],
                             button_posx = args.pos['Login']['login_button'][0],
                             button_posy = args.pos['Login']['login_button'][1],
                             checkbox_size = 20,
                             button_posy_create = args.pos['Login']['create_button'][1],
                             button_posx_create = args.pos['Login']['create_button'][0],
                             error_label_text = '',
                             error_label_color = args.pattern_style['error_color'],
                             error_label_posx = args.pos['Login']['error_label'][0],
                             error_label_posy = args.pos['Login']['error_label'][1],
                             font_error = 20,
                             green_card_register = True,
                             border_w = 4,
                             border_color = args.pattern_style['border_button_color'],
                             img1x = args.pos['Login']['img1'][0],
                             img1y = args.pos['Login']['img1'][1],
                             img2x = args.pos['Login']['img2'][0],
                             img2y = args.pos['Login']['img2'][1])
        login.open_window()
        if Login_Window.green_card_login:
            option = Option_Window(args.window_size['Option'][0], args.window_size['Option'][1], 'Ico_Files/for_test.ico', 'Password Management System ErickDev', Login_Window.id_user,
                                   text = 'CHOOSE AN OPTION',
                                   posx_label = args.pos['Option']['title'][0],
                                   posy_label = args.pos['Option']['title'][1],
                                   posx_button1 = args.pos['Option']['button1'][0],
                                   posy_button1 = args.pos['Option']['button1'][1],
                                   posx_button2 = args.pos['Option']['button2'][0],
                                   posy_button2 = args.pos['Option']['button2'][1],
                                   posx_button3 = args.pos['Option']['button3'][0],
                                   posy_button3 = args.pos['Option']['button3'][1],
                                   posx_button4 = args.pos['Option']['button4'][0],
                                   posy_button4 = args.pos['Option']['button4'][1],
                                   font_size_label = 40,
                                   width_button = 300,
                                   height_button = 50,
                                   button_text_color = args.pattern_style['button_label_color'],
                                   pattern_color = args.pattern_style['main_color'],
                                   hover_color = args.pattern_style['button_hover_color'],
                                   font_size = 30,
                                   font_style = args.pattern_style['main_font'],
                                   border_w = 4,
                                   border_color = args.pattern_style['border_button_color'],
                                   posx_button5 = args.pos['Option']['button5'][0],
                                   posy_button5 = args.pos['Option']['button5'][1])
            option.open_window()
    else:
        cnct_error = Error_Window(args.window_size['Error'][0], args.window_size['Error'][1], 'Ico_Files/for_test.ico', 'PMS connection error', "ERROR: CAN'T CONNECT TO THE DATABASE",
                                  pos_x_button = args.pos['Error']['button'][0],
                                  pos_y_button = args.pos['Error']['button'][1],
                                  pos_x_label = args.pos['Error']['label'][0],
                                  pos_y_label = args.pos['Error']['label'][1],
                                  border_w = 4,
                                  border_color = args.pattern_style['border_button_color'],
                                  img1x = args.pos['Error']['img1'][0], img1y = args.pos['Error']['img1'][1],
                                  img2x = args.pos['Error']['img2'][0], img2y = args.pos['Error']['img2'][1])
        cnct_error.open_window()