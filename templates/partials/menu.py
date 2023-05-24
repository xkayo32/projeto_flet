from flet import UserControl, Image, Text, TextField, Column, Row, Container, TextButton, Alignment, icons, Dropdown, dropdown, TextStyle, TextDecoration
import os
import base64


class Menu(UserControl):

    def build(self):
        self.static_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '../..', 'static'))
        self.logo = Image(src_base64=self.imagem_para_base64(os.path.join(self.static_path,
                          'img/logo_pymazon.png')))
        self.location = Text('DF')
        self.div_location = Container(
            Column([Text('Delivetery to'), self.location], alignment=Alignment(0, 0)))
        self.category = Container(Dropdown(width=200, options=[dropdown.Option('Books'), dropdown.Option('Electronics'), dropdown.Option(
            'Computers'), dropdown.Option('Home'), dropdown.Option('Garden'), dropdown.Option('Tools'), dropdown.Option('Grocery')], on_change=lambda _: print('changed'), label="All", expand=1))
        self.search = TextField(hint_text='Search here',
                                suffix_icon=icons.SEARCH)
        self.profile = TextButton('Hello, User', disabled=True)
        self.div_profile = Container(Column([self.profile, TextButton(
            'Sign in', on_click=lambda _: self.page.go('/login'))], alignment=Alignment(0, 0)))
        self.returns_orders = Container(Text('Returns \n& Orders'))
        self.cart = Container(TextButton(
            'Cart', on_click=lambda _: self.page.go('/cart'), icon=icons.SHOPPING_CART))
        return Container(Row(
            [Container(self.logo, expand=1), Container(self.div_location, expand=1), self.category, Container(
                self.search, expand=4), Container(self.div_profile, expand=1), Container(self.returns_orders, expand=1), Container(self.cart, expand=1)],
            height=75, spacing=1
        ), bgcolor='#232f3e')

    @staticmethod
    def imagem_para_base64(caminho_imagem):
        with open(caminho_imagem, "rb") as imagem_arquivo:
            imagem_bytes = imagem_arquivo.read()
            imagem_base64 = base64.b64encode(imagem_bytes).decode("utf-8")
            return imagem_base64
