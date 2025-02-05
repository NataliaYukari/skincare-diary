import flet as ft
from models.user import User

class RegisterScreen(ft.Container):


    def __init__(self, view):
        super().__init__()
        self.view = view

        title = ft.Text(
            "Novo cadastro", font_family= "AlbertSans", 
            theme_style= ft.TextThemeStyle.DISPLAY_SMALL
        )

        blankSpace = ft.Text(" ", theme_style= ft.TextThemeStyle.DISPLAY_SMALL)

        nameLabel = ft.Text(
            "Nome de usuário", font_family= "AlbertSans", 
            theme_style= ft.TextThemeStyle.HEADLINE_SMALL
        )

        self.nameTextfield = ft.TextField(
            width= 400, 
            border= ft.InputBorder.OUTLINE, border_color= view.WHITE,
            border_radius= ft.border_radius.all(10),
            filled= True, fill_color= view.WHITE
        )

        passwordLabel = ft.Text(
            "Senha", font_family= "AlbertSans", 
            theme_style= ft.TextThemeStyle.HEADLINE_SMALL
        )

        self.newPasswordTextfield = ft.TextField(
            width= 400, password=True, can_reveal_password=True, 
            border= ft.InputBorder.OUTLINE, border_color= view.WHITE,
            border_radius= ft.border_radius.all(10),
            filled= True, fill_color= view.WHITE
        )

        emailLabel = ft.Text(
            "E-mail", font_family= "AlbertSans", 
            theme_style= ft.TextThemeStyle.HEADLINE_SMALL
        )

        self.emailTextfield = ft.TextField(
            width= 400, 
            border= ft.InputBorder.OUTLINE, border_color= view.WHITE,
            border_radius= ft.border_radius.all(10), 
            filled= True, fill_color= view.WHITE
        )

        returnButtonContainer = ft.Container(
            content= view.return_button(view.return_to_login), padding= ft.Padding(220, 10, 10, 10)
        )

        birthdayLabel = ft.Text(
            "Data de aniversário", font_family= "AlbertSans", 
            theme_style= ft.TextThemeStyle.HEADLINE_SMALL
        )
        
        self.birthdayTextfield = ft.TextField(
            width= 400, hint_text= "dd/mm/aaaa", 
            hint_style= ft.TextStyle(
                color= "#878787", weight= ft.FontWeight.W_400
            ), 
            border= ft.InputBorder.OUTLINE, border_color= view.WHITE,
            border_radius= ft.border_radius.all(10), 
            filled= True, fill_color= view.WHITE
        )

        skinTypeLabel = ft.Text(
            "Tipo de pele", font_family= "AlbertSans", 
            theme_style= ft.TextThemeStyle.HEADLINE_SMALL
        )
        
        self.skinTypeDropdown = ft.Dropdown(
            width= 400, 
            options= [
                ft.dropdown.Option("Oleosa"),
                ft.dropdown.Option("Seca"),
                ft.dropdown.Option("Normal"),
                ft.dropdown.Option("Mista")
            ],
            bgcolor= view.WHITE, 
            border= ft.InputBorder.OUTLINE, border_color= view.WHITE,
            border_radius= ft.border_radius.all(10),
            filled= True, fill_color= view.WHITE, 
            text_style= ft.TextStyle(
                weight= ft.FontWeight.W_400,
                color = ft.colors.BLACK, size= 16
            )
        )

        sensitivity = ft.Text(
            "Pele com sensibilidade?", font_family= "AlbertSans", 
            theme_style= ft.TextThemeStyle.HEADLINE_SMALL
        )
        
        self.sensitivityCheckbox = ft.Checkbox(
            value= False, fill_color= view.WHITE, 
            check_color= view.ROSEQUARTZ, active_color= view.ROSEQUARTZ, 
            border_side= ft.BorderSide(color= view.WHITE, width= 1),
            scale= 2.3 
        )

        checkboxContainer = ft.Container(
            content= self.sensitivityCheckbox,
            margin = ft.margin.only(top= 8, right= 0, bottom= 0, left= 0)
        )

        registerButton = ft.FilledButton(
            text= "Cadastrar",
            on_click= self.create_user,
            style= ft.ButtonStyle(
                bgcolor= {"": view.ROSEQUARTZ, "hovered": view.PALESALMON},
                color= view.WHITE,
                padding= ft.Padding(50, 0, 50, 10),
                text_style= ft.TextStyle(size= 22)
            )
        )

        registerButtonContainer = ft.Container(
            content= registerButton, padding= ft.Padding(0, 24, 230, 10)
        )

        leftColumn = ft.Column(
            controls= [
                title, nameLabel, self.nameTextfield, passwordLabel, 
                self.newPasswordTextfield, emailLabel, 
                self.emailTextfield, returnButtonContainer
            ],
            alignment= ft.MainAxisAlignment.CENTER, 
            horizontal_alignment= ft.CrossAxisAlignment.START, 
            spacing= 20
        )

        rightColumn = ft.Column(
            controls= [
                blankSpace, birthdayLabel, self.birthdayTextfield, skinTypeLabel, 
                self.skinTypeDropdown, sensitivity, 
                checkboxContainer, registerButtonContainer
            ],
            alignment= ft.MainAxisAlignment.CENTER, 
            horizontal_alignment= ft.CrossAxisAlignment.START, 
            spacing= 19
        )

        centralRow = ft.Row(
            controls= [leftColumn, rightColumn], 
            alignment= ft.MainAxisAlignment.CENTER, 
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 100
        )

        mainColumnContainer = ft.Container(
            content= centralRow, 
            alignment= ft.alignment.center, 
            padding= ft.padding.symmetric(horizontal= 50, vertical= 50),
            bgcolor= view.BEIGE
        )

        self.content = mainColumnContainer

    def create_user(self, e):
        username = self.nameTextfield.value
        password = self.newPasswordTextfield.value
        email = self.emailTextfield.value
        birthday = self.birthdayTextfield.value
        skinType = self.skinTypeDropdown.value
        sensitivity = self.sensitivityCheckbox.value

        userData = User(username, password, email, 
                         birthday, skinType, sensitivity)

        self.view.controller.validate_user_data(userData)

    def reset_fields(self):
        self.nameTextfield.value = ""
        self.newPasswordTextfield.value = ""
        self.emailTextfield.value = ""
        self.birthdayTextfield.value = ""
        self.skinTypeDropdown.value = ""
        self.sensitivityCheckbox.value = False

        self.view.page.update()