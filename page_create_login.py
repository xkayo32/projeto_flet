from flet import UserControl, TextField, TextButton, Column, Container, Alignment, icons
from sqlalchemy.orm import Session
from cript_keys import decrypt_key, encrypt_key
from models import Cliente, engine


class CreateUser(UserControl):
    def build(self) -> Column:
        self.name = TextField(
            hint_text='Name', icon=icons.PERSON)
        self.email = TextField(
            hint_text='Email', on_change=self.__check_email, icon=icons.EMAIL_ROUNDED)
        self.password = TextField(hint_text='Password', password=True,
                                  on_submit=self.__check_password, icon=icons.LOCK_ROUNDED, disabled=True)

        return Column(
            controls=[
                Container(self.name),
                Container(self.password),
                Container(self.email),
                Container(TextButton(
                    text='Save', on_click=self.__create_user, icon=icons.PERSON_ADD))
            ],
            spacing=10,
            width=500
        )

    def __check_email(self, event):
        if self.email.value:
            with Session(engine) as session:
                cliente = session.query(Cliente).filter_by(
                    email=self.email.value).first()
                if cliente:
                    self.email.error_text = 'Email already in use'
                    self.password.disabled = True
                else:
                    self.email.error_text = ''
                    self.password.disabled = False
        else:
            self.email.error_text = ''
        self.update()

    def __check_password(self, event):
        if self.password.value:
            if len(self.password.value) < 8:
                self.password.error_text = 'Password must be at least 8 characters'
            else:
                self.password.error_text = ''
        else:
            self.password.error_text = ''
        self.update()

    def __create_user(self, event):
        if self.name.value and self.email.value and self.password.value:
            with Session(engine) as session:
                cliente = Cliente(
                    name=self.name.value,
                    email=self.email.value,
                    password=encrypt_key(self.password.value)
                )
                session.add(cliente)
                session.commit()
                print('User created')
        else:
            print('Invalid fields')
