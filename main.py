import flet as ft
from templates.page_login import Login
from templates.page_create_login import CreateUser
from templates.page_home import Home


class Main:
    def __init__(self) -> None:
        ft.app(self.main, view=ft.WEB_BROWSER, port=5000)

    def main(self, page: ft.Page):
        page.title = 'Login'
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.LIGHT

        def route_change(route):
            page.views.clear()
            page.views.append(self.__create_view('/login', [Login()]))
            if page.route == '/':
                page.views.append(self.__create_view(
                    '/', [Home()]))
            elif page.route == '/create_login':
                page.views.append(self.__create_view(
                    '/create_login', [CreateUser()]))
            page.update()

        def view_pop(view):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop
        page.go(page.route)

    def __create_view(self, route: str, controls: list):
        """
        This function creates a view object with a specified route and list of controls.

        :param route: The route parameter is a string that represents the URL path for the view. It is the
        address that the user will enter in their browser to access the view
        :type route: str
        :param controls: The `controls` parameter is a list of `ft.Control` objects that define the user
        interface elements for the view. These controls can include buttons, text boxes, labels, and other
        interactive elements that allow the user to interact with the view. The `__create_view` method uses
        these controls to
        :type controls: list
        :return: an instance of the `View` class from the `ft` module, which is created using the `route`
        and `controls` arguments passed to the function.
        """
        return ft.View(route, controls)


if __name__ == '__main__':
    Main()
