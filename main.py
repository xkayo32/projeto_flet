import flet as ft
from page_login import Login

class Main:
    def __init__(self) -> None:
        ft.app(self.main,view=ft.WEB_BROWSER)
        
    def main(self,page:ft.Page):
        page.title = 'Login'
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.add(Login())

if __name__ == '__main__':
    Main()