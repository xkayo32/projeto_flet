from flet import TextField, UserControl, TextButton, TextStyle, TextDecoration, Container, Column, icons, Alignment, Row, WEB_BROWSER, app
from .partials.menu import Menu


class Home(UserControl):
    def build(self):
        return Column([Menu()], alignment=Alignment(0, 0))
