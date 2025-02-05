import flet as ft


class LoginScreen(ft.Container):


    def __init__(self, view):
        super().__init__()
        self.view = view

        header = ft.Text(
            "Skincare Diary", font_family= "AlbertSans", 
            theme_style=ft.TextThemeStyle.DISPLAY_LARGE
        )

        self.loginTextfield = ft.TextField(
            hint_text="Usuário", 
            border= ft.InputBorder.OUTLINE, border_color= view.WHITE,
            border_radius= ft.border_radius.all(10),
            filled= True, fill_color= view.WHITE,
            width=400 
        )

        self.passwordTextfield = ft.TextField(
            hint_text="Senha", 
            password=True, can_reveal_password=True, 
            border= ft.InputBorder.OUTLINE, border_color= view.WHITE,
            border_radius= ft.border_radius.all(10),
            filled= True, fill_color= view.WHITE, 
            width=400
        )
        
        loginButton = ft.FilledButton(
            text="Entrar", 
            on_click= self.validate_login,
            style=ft.ButtonStyle(
                bgcolor= {"": view.ROSEQUARTZ, "hovered": view.PALESALMON},
                color= { "": view.WHITE}, 
                padding=ft.Padding(40, 10, 40, 10),
                text_style= ft.TextStyle(size= 24)
            )
        )
        
        registerButton = ft.FilledButton(
            text="Cadastre-se aqui", 
            on_click= view.go_to_register_screen,
            style= ft.ButtonStyle(
                bgcolor= ft.colors.TRANSPARENT, 
                color= view.LIGHTGRAY, 
                overlay_color= ft.colors.TRANSPARENT, 
                text_style= ft.TextStyle(
                    size= 18, decoration= ft.TextDecoration.UNDERLINE,
                    weight= ft.FontWeight.W_600
                )
            )
        )
        
        self.loginFailLabel = ft.Column()

        columnContainer = ft.Column(
            controls= [
                header, self.loginTextfield, self.passwordTextfield, 
                loginButton, registerButton, self.loginFailLabel
            ],
            alignment= ft.MainAxisAlignment.CENTER, 
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            expand= True, spacing= 20
        )

        mainContainer = ft.Container(
            content= columnContainer, 
            alignment= ft.alignment.center, 
            margin= ft.margin.only(top= 140),
            expand= True,
            bgcolor= view.BEIGE
        )

        self.content = mainContainer

    def validate_login(self, e):
        login = self.loginTextfield.value
        password = self.passwordTextfield.value

        self.view.controller.validate_login(login, password)

    def login_fail_text(self, message):
        self.loginFailLabel.controls.clear()

        self.loginFailLabel.controls.append(
            ft.Text(
                "Erro ao logar: " + message, 
                font_family= "AlbertSans",
                theme_style= ft.TextThemeStyle.TITLE_MEDIUM,
                color= "#996A65",
                weight= ft.FontWeight.BOLD
                )
        )
        self.page.update()