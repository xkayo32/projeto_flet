from flet import TextField, UserControl, TextButton, TextStyle, TextDecoration, Container, Column, icons, Alignment, Row, WEB_BROWSER, app, colors, ScrollMode, GridView, Image, ImageFit, ImageRepeat, border_radius, ThemeMode, MainAxisAlignment, CrossAxisAlignment
from .partials.menu import Menu


class Home(UserControl):
    def build(self):
        # self.carousel = GridView(horizontal=True)
        self.carousel = Row(
            [Container(width=150, height=150, bgcolor=colors.RED) for _ in range(5)])
        return Column([Menu(), Container(self.carousel, bgcolor=colors.LIGHT_GREEN_ACCENT)], alignment=Alignment(0, 0))
