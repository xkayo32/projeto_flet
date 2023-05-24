from flet import TextField, UserControl, TextButton, TextStyle, TextDecoration, Container, Column, icons, Alignment, Row
import re
from models import Cliente, Session, session, engine
from cript_keys import decrypt_key


class Login(UserControl):

    def build(self) -> Column:
        """
        This function builds a login form with email and password fields and a login button.
        :return: The `build` method is returning a `Column` widget that contains a `TextField` for email
        input, a `TextField` for password input (with the `password` attribute set to `True` to hide the
        input), and a `TextButton` for submitting the login information. The `Column` widget is set to have
        a spacing of 10 and a width of 500.
        """
        self.email = TextField(
            hint_text='Email', on_change=self.__on_change, icon=icons.EMAIL_ROUNDED)
        self.password = TextField(hint_text='Password', password=True,
                                  on_submit=self.__check_login, icon=icons.LOCK_ROUNDED)
        self.login = TextButton(
            text='Login', on_click=self.__check_login, icon=icons.LOGIN)
        self.create_login = TextButton(
            text='Create Login', on_click=lambda _: self.page.go('/create_login'), icon=icons.PERSON_ADD)
        return Column(
            controls=[
                Container(self.email),
                Container(self.password),
                Container(Row([self.create_login, self.login]),
                          alignment=Alignment(1, 0))
            ],
            spacing=10,
            width=500
        )

    def __on_change(self, event):
        """
        This function validates an email input and displays an error message if it is invalid.

        :param event: The "event" parameter is an object that represents the event that triggered the
        function. It contains information about the event, such as the type of event, the control that
        triggered the event, and any data associated with the event. In this case, it is likely an event
        that is triggered when the
        """
        if not self.__validate_email(event.control.value):
            self.email.error_text = 'Invalid email'
            self.email.error_style = TextStyle(
                decoration=TextDecoration.UNDERLINE)
        else:
            self.email.error_text = ''
            self.email.error_style = None
        self.update()

    def __check_login(self, event):
        """
        This function checks if the email value is present and prints either "Login success" or "Login
        failed".

        :param event: The event parameter is likely an object that represents the event that triggered the
        function. It is not used in the function body, so it's hard to say exactly what type of event it is
        without more context. However, based on the function name and the fact that it checks for a
        non-empty email
        """
        if self.email.value:
            with Session(engine) as session:
                cliente = session.query(Cliente).filter_by(
                    email=self.email.value).first()
                if cliente:
                    password = decrypt_key(cliente.password)
                    if password == self.password.value:
                        print('Login success')
                    else:
                        self.email.error_text = 'Invalid password'
                else:
                    self.email.error_text = 'Invalid email'
        else:
            print('Login failed')
        self.update()

    @staticmethod
    def __validate_email(email):
        """
        The function takes an email as input and is likely used to validate whether the email is in a
        correct format. However, the function body is missing so it's unclear what specific validation
        checks are being performed.

        :param email: The "email" parameter is a string that represents an email address that needs to be
        validated. The function likely checks if the email address is in a valid format according to certain
        rules and returns a boolean value indicating whether the email is valid or not
        """
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)
