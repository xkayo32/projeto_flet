from flet import TextField, Text, UserControl, TextButton, TextStyle,TextDecoration, Container,Column,icons, Alignment
import re



class Login(UserControl):
    
    def build(self):
        self.email = TextField(hint_text='Email',on_change=self.__on_change,icon=icons.EMAIL_ROUNDED)
        self.password = TextField(hint_text='Password',password=True,on_submit=self.__check_login,icon=icons.LOCK_ROUNDED)
        self.login = TextButton(text='Login',on_click=self.__check_login,icon=icons.LOGIN)
        
        return Column(
            controls=[
                Container(self.email),
                Container(self.password),
                Container(self.login,alignment=Alignment(1,0))
            ],
            spacing=10,
            width=500
        )
        
    def __on_change(self,event):
        if not self.__validate_email(event.control.value):
            self.email.error_text = 'Invalid email'
            self.email.error_style = TextStyle(decoration=TextDecoration.UNDERLINE)
        else:
            self.email.error_text = ''
            self.email.error_style = None
        self.update()
    
    def __check_login(self,event):
        if event.control.value:
            print('Login success')
        else:
            print('Login failed')
    
    @staticmethod
    def __validate_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)