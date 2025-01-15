from controller import Controller
import flet as ft
from user import User
from entry import Entry
from skin_concerns import SkinConcerns



class View:
    
    def __init__(self):
        self.controller = None
        self.image_path = None

        self.BEIGE = "#F2F1E9"
        self.DEEPBEIGE = "#F0D2AB"
        self.ROSEQUARTZ = "#D9B7B4"
        self.PALESALMON = "#D9B4A7"
        self.WHITE = "#FFFFFF"
        self.DARKGRAY = "#736B6A"
        self.LIGHTGRAY = "#878787"

    def set_controller(self, controller):
        self.controller = controller

    def login_screen(self):
        header = ft.Text(
            "Skincare Diary", font_family= "AlbertSans", 
            theme_style=ft.TextThemeStyle.DISPLAY_LARGE
        )

        self.loginTextfield = ft.TextField(
            hint_text="Usuário", 
            border= ft.InputBorder.OUTLINE, border_color= self.WHITE,
            border_radius= ft.border_radius.all(10),
            filled= True, fill_color= self.WHITE,
            width=400 
        )

        self.passwordTextfield = ft.TextField(
            hint_text="Senha", 
            password=True, can_reveal_password=True, 
            border= ft.InputBorder.OUTLINE, border_color= self.WHITE,
            border_radius= ft.border_radius.all(10),
            filled= True, fill_color= self.WHITE, 
            width=400
        )
        
        loginButton = ft.FilledButton(
            text="Entrar", 
            on_click= self.validate_login,
            style=ft.ButtonStyle(
                bgcolor= {"": self.ROSEQUARTZ, "hovered": self.PALESALMON},
                color= { "": self.WHITE}, 
                padding=ft.Padding(40, 10, 40, 10),
                text_style= ft.TextStyle(size= 24)
            )
        )
        
        registerButton = ft.FilledButton(
            text="Cadastre-se aqui", 
            on_click= self.go_to_register_screen,
            style= ft.ButtonStyle(
                bgcolor= ft.colors.TRANSPARENT, 
                color= self.LIGHTGRAY, 
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
            alignment= ft.Alignment(0, 0), 
            expand= True,
            bgcolor= self.BEIGE
        )

        return mainContainer
    
    def validate_login(self, e):
        login = self.loginTextfield.value
        password = self.passwordTextfield.value

        self.controller.validate_login(login, password)

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
    
    def go_to_register_screen(self, e):
        self.controller.go_to_register_screen()

    def register_screen(self):

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
            border= ft.InputBorder.OUTLINE, border_color= self.WHITE,
            border_radius= ft.border_radius.all(10),
            filled= True, fill_color= self.WHITE
        )

        passwordLabel = ft.Text(
            "Senha", font_family= "AlbertSans", 
            theme_style= ft.TextThemeStyle.HEADLINE_SMALL
        )

        self.newPasswordTextfield = ft.TextField(
            width= 400, password=True, can_reveal_password=True, 
            border= ft.InputBorder.OUTLINE, border_color= self.WHITE,
            border_radius= ft.border_radius.all(10),
            filled= True, fill_color= self.WHITE
        )

        emailLabel = ft.Text(
            "E-mail", font_family= "AlbertSans", 
            theme_style= ft.TextThemeStyle.HEADLINE_SMALL
        )

        self.emailTextfield = ft.TextField(
            width= 400, 
            border= ft.InputBorder.OUTLINE, border_color= self.WHITE,
            border_radius= ft.border_radius.all(10), 
            filled= True, fill_color= self.WHITE
        )

        returnButtonContainer = ft.Container(
            content= self.return_button(self.return_to_login), padding= ft.Padding(220, 10, 10, 10)
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
            border= ft.InputBorder.OUTLINE, border_color= self.WHITE,
            border_radius= ft.border_radius.all(10), 
            filled= True, fill_color= self.WHITE
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
            bgcolor= self.WHITE, 
            border= ft.InputBorder.OUTLINE, border_color= self.WHITE,
            border_radius= ft.border_radius.all(10),
            filled= True, fill_color= self.WHITE, 
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
            value= False, fill_color= self.WHITE, 
            check_color= self.ROSEQUARTZ, active_color= self.ROSEQUARTZ, 
            border_side= ft.BorderSide(color= self.WHITE, width= 1),
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
                bgcolor= {"": self.ROSEQUARTZ, "hovered": self.PALESALMON},
                color= self.WHITE,
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
            bgcolor= self.BEIGE
        )

        self.page.clean()
        self.page.add(mainColumnContainer)
        self.page.update()

    def create_user(self, e):
        username = self.nameTextfield.value
        password = self.newPasswordTextfield.value
        email = self.emailTextfield.value
        birthday = self.birthdayTextfield.value
        skinType = self.skinTypeDropdown.value
        sensitivity = self.sensitivityCheckbox.value

        userData = User(username, password, email, 
                         birthday, skinType, sensitivity)

        self.controller.validate_user_data(userData)

    def main_screen(self):
        title = ft.Text(
            "Bem-vindo!", font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.DISPLAY_SMALL)
        
        createRoutineButton = ft.FilledButton(
            text= "Montar rotina",
            on_click= self.go_to_routine_form,
            width= 390,
            height= 50,
            style= ft.ButtonStyle(
                bgcolor= {"": self.ROSEQUARTZ, "hovered": self.PALESALMON},
                padding= ft.padding.all(10),
                shape= ft.RoundedRectangleBorder(radius= 15),
                text_style= ft.TextStyle(
                    size= 24, weight= ft.FontWeight.W_400
                )
            )
        )
    
        showRoutineButton = ft.FilledButton(
            text= "Ver rotina",
            on_click= self.go_to_recommended_routine_screen,
            width= 390,
            height= 50,
            style= ft.ButtonStyle(
                bgcolor= {"": self.PALESALMON, "hovered": self.ROSEQUARTZ},
                padding= ft.padding.all(10),
                shape= ft.RoundedRectangleBorder(radius= 15),
                text_style= ft.TextStyle(
                    size= 24, weight= ft.FontWeight.W_400
                )
            )
        )

        addNewEntryButton = ft.FilledButton(
            text= "Adicionar nova entrada",
            on_click= self.go_to_add_entry_screen,
            width= 390,
            height= 50,
            style= ft.ButtonStyle(
                bgcolor= {"": self.ROSEQUARTZ, "hovered": self.PALESALMON},
                padding= ft.padding.all(10),
                shape= ft.RoundedRectangleBorder(radius= 15),
                text_style= ft.TextStyle(
                    size= 24, weight= ft.FontWeight.W_400
                )
            )
        )
        showDiaryButton = ft.FilledButton(
            text= "Diário de progresso",
            on_click= self.go_to_diary_screen,
            width= 390,
            height= 50,
            style= ft.ButtonStyle(
                bgcolor= {"": self.PALESALMON, "hovered": self.ROSEQUARTZ},
                padding= ft.padding.all(10),
                shape= ft.RoundedRectangleBorder(radius= 15),
                text_style= ft.TextStyle(
                    size= 24, weight=ft.FontWeight.W_400
                )
            )
        )

        image = ft.Image(
            src= f"assets/images/produtos.jpg",
            width= 535,
            height= 660,
            fit= ft.ImageFit.CONTAIN
        )

        leftColumn = ft.Column(
            controls= [
                title, createRoutineButton, 
                showRoutineButton, addNewEntryButton, showDiaryButton
                ],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.START,
            spacing= 40
        )  

        row = ft.Row(
            controls= [leftColumn, image],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER
        )

        self.mainScreenContainer = ft.Container(
            content= row, 
            alignment= ft.alignment.center
        )
        
        self.page.clean()
        self.page.add(self.mainScreenContainer)
        self.page.update()

    def go_to_routine_form(self, e):
        self.controller.go_to_routine_form()

    def go_to_recommended_routine_screen(self, e):
        self.controller.go_to_recommended_routine_screen()

    def go_to_add_entry_screen(self, e):
        self.controller.go_to_add_entry_screen()

    def go_to_diary_screen(self, e):
        self.controller.go_to_diary_screen()

    def add_entry_screen(self):

        title = ft.Text(
            "Adicionar nova entrada", font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.DISPLAY_SMALL
        )

        dateLabel = ft.Text(
            "Data: ", font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.HEADLINE_SMALL
        )

        self.dateTextfield = ft.TextField(
            width= 390, 
            height= 40,
            border= ft.InputBorder.OUTLINE, border_color= self.WHITE,
            border_radius= ft.border_radius.all(10),
            filled= True, fill_color= self.WHITE
        )

        descriptionLabel = ft.Text(
            "Descrição: ", font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.HEADLINE_SMALL
        )

        self.descriptionTextfield = ft.TextField(
            multiline= True,
            min_lines= 10,
            width= 390,
            border= ft.InputBorder.OUTLINE, border_color= self.WHITE,
            border_radius= ft.border_radius.all(15),
            filled= True, fill_color= self.WHITE
        )

        filePicker = ft.FilePicker(on_result= self.entry_image_upload)

        imageUploadButton = ft.FilledButton(
            text= "Upload de foto",
            on_click= lambda _: filePicker.pick_files(),
            width=  240,
            height= 33,
            style= ft.ButtonStyle(
                bgcolor= self.DARKGRAY,
                shape= ft.RoundedRectangleBorder(radius= 12),
                text_style= ft.TextStyle(
                    size= 20, weight= ft.FontWeight.W_400
                )
            )
        )

        imageDeleteButton = ft.FilledButton(
            text= "Deletar foto",
            width= 190,
            height= 33,
            on_click= self.entry_image_delete,
            style= ft.ButtonStyle(
                bgcolor= self.LIGHTGRAY,
                shape= ft.RoundedRectangleBorder(radius= 12),
                text_style= ft.TextStyle(
                    size= 20, weight= ft.FontWeight.W_400
                )
            )
        )

        self.addImageContainer = ft.Container(
            content= None,
            width= 450,
            height= 375,
            bgcolor= self.WHITE, 
            border_radius= 10
        )

        addEntryButton = ft.FilledButton(
            text= "Adicionar",
            on_click= self.create_entry,
            style= ft.ButtonStyle(
                padding= ft.Padding(40, 10, 40, 10),
                bgcolor= {"": self.ROSEQUARTZ, "hovered": self.PALESALMON},
                text_style = ft.TextStyle(size= 22)
            )
        )

        leftColumn = ft.Column(
            controls= [
                title, dateLabel, self.dateTextfield, 
                descriptionLabel, self.descriptionTextfield
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.START,
            spacing= 15
        )

        imageButtonRow = ft.Row(
            controls = [imageUploadButton, imageDeleteButton],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER
        )

        rightColumn = ft.Column(
            controls= [ft.Container(height= 30), imageButtonRow, self.addImageContainer],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 15
        )

        buttonRow =  ft.Row(
            controls= [self.return_button(self.return_to_main), addEntryButton],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 60
        )

        mainRow = ft.Row(
            controls= [leftColumn, rightColumn],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 40
        )

        mainColumn = ft.Column(
            controls= [mainRow, buttonRow],
            horizontal_alignment= ft.MainAxisAlignment.CENTER,
            spacing= 40
        )

        mainContainer = ft.Container(
            content= mainColumn,
            alignment= ft.alignment.center,
            margin= ft.margin.only(top= 80)
        )

        self.page.clean()
        self.page.add(mainContainer)
        self.page.add(filePicker)
        self.page.update()

    def entry_image_upload(self, e):
        if e.files:
            self.image_path = e.files[0].path

        image = ft.Image(
            src= self.image_path, 
            width= 535,
            height= 660,
            fit= ft.ImageFit.CONTAIN
        )

        self.addImageContainer.content = image
        self.page.update()

    def entry_image_delete(self, e):
        self.addImageContainer.content = None
        self.page.update()

    def create_entry(self, e):
        date = self.dateTextfield.value
        description = self.descriptionTextfield.value
        image = self.image_path

        entryData = Entry(date, description, image)
        self.controller.create_entry(entryData)

    def  new_routine_screen(self):
        title = ft.Text(
            "Nova rotina", font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.DISPLAY_SMALL
        )

        subtitle = ft.Text(
            "Escolha suas 3 principais preocupações: ",
            font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.HEADLINE_MEDIUM
        )

        self.wrinklesCheckbox = ft.Checkbox(
            value= False,
            fill_color= self.WHITE,
            check_color= self.ROSEQUARTZ, active_color= self.ROSEQUARTZ,
            border_side= ft.BorderSide(color= self.WHITE, width= 1),
            scale= 1.5
        )

        self.acneCheckbox = ft.Checkbox(
            value= False,
            fill_color= self.WHITE,
            check_color= self.ROSEQUARTZ, active_color= self.ROSEQUARTZ,
            border_side= ft.BorderSide(color= self.WHITE, width= 1),
            scale= 1.5
        )

        self.poresCheckbox = ft.Checkbox(
        value= False,
        fill_color= self.WHITE,
        check_color= self.ROSEQUARTZ, active_color= self.ROSEQUARTZ,
        border_side= ft.BorderSide(color= self.WHITE, width= 1),
        scale= 1.5
        )

        self.pigmentationCheckbox = ft.Checkbox(
        value= False,
        fill_color= self.WHITE,
        check_color= self.ROSEQUARTZ, active_color= self.ROSEQUARTZ,
        border_side= ft.BorderSide(color= self.WHITE, width= 1),
        scale= 1.5
        )

        self.textureCheckbox = ft.Checkbox(
        value= False,
        fill_color= self.WHITE,
        check_color= self.ROSEQUARTZ, active_color= self.ROSEQUARTZ,
        border_side= ft.BorderSide(color= self.WHITE, width= 1),
        scale= 1.5
        )

        self.irritationCheckbox = ft.Checkbox(
        value= False,
        fill_color= self.WHITE,
        check_color= self.ROSEQUARTZ, active_color= self.ROSEQUARTZ,
        border_side= ft.BorderSide(color= self.WHITE, width= 1),
        scale= 1.5
        )

        self.dehydrationCheckbox = ft.Checkbox(
        value= False,
        fill_color= self.WHITE,
        check_color= self.ROSEQUARTZ, active_color= self.ROSEQUARTZ,
        border_side= ft.BorderSide(color= self.WHITE, width= 1),
        scale= 1.5
        )

        self.excessOilCheckbox = ft.Checkbox(
        value= False,
        fill_color= self.WHITE,
        check_color= self.ROSEQUARTZ, active_color= self.ROSEQUARTZ,
        border_side= ft.BorderSide(color= self.WHITE, width= 1),
        scale= 1.5
        )

        generateRoutineButton = ft.FilledButton(
            text= "Gerar rotina",
            on_click= self.generate_routine,
            style= ft.ButtonStyle(
                padding= ft.Padding(40, 10, 40, 10),
                bgcolor= {"": self.ROSEQUARTZ, "hovered": self.PALESALMON},
                text_style = ft.TextStyle(size= 22)
            )
        )

        leftColumn = ft.Column(
            controls= [
                title, subtitle,
                ft.Row([self.wrinklesCheckbox, 
                    ft.Text("Rugas/Linhas finas", 
                        theme_style= ft.TextThemeStyle.TITLE_LARGE)
                    ], 
                    spacing= 10
                ), 
                ft.Row([self.acneCheckbox,
                    ft.Text("Acne/Cravos",
                        theme_style= ft.TextThemeStyle.TITLE_LARGE)
                    ], 
                    spacing= 10
                ), 
                ft.Row([self.poresCheckbox,
                    ft.Text("Poros Dilatados",
                        theme_style= ft.TextThemeStyle.TITLE_LARGE)
                    ], 
                    spacing= 10
                ), 
                ft.Row([self.pigmentationCheckbox, 
                    ft.Text("Manchas, melasma, cicatrizes de acne",
                        theme_style= ft.TextThemeStyle.TITLE_LARGE)
                    ], 
                    spacing= 10
                )
            ],
            alignment= ft.MainAxisAlignment.START,
            horizontal_alignment= ft.CrossAxisAlignment.START,
            spacing= 20
        ) 

        rightColumn = ft.Column(
            controls= [
                ft.Container(height= 99),
                ft.Row([self.textureCheckbox, 
                    ft.Text("Textura irregular", 
                       theme_style= ft.TextThemeStyle.TITLE_LARGE)
                    ], 
                    spacing= 10
                ), 
                ft.Row([self.irritationCheckbox, 
                    ft.Text("Rosácea, irritação extrema",
                        theme_style= ft.TextThemeStyle.TITLE_LARGE)
                    ], 
                    spacing=10
                ),
                ft.Row([self.dehydrationCheckbox, 
                    ft.Text("Ressecamento, desidratação",
                        theme_style= ft.TextThemeStyle.TITLE_LARGE)
                    ], 
                    spacing= 10
                ), 
                ft.Row([self.excessOilCheckbox, 
                    ft.Text("Excesso de brilho, oleosidade",
                        theme_style= ft.TextThemeStyle.TITLE_LARGE)
                    ], 
                    spacing=10
                )
            ],
            alignment= ft.MainAxisAlignment.START,
            horizontal_alignment= ft.CrossAxisAlignment.START,
            spacing= 20
        )

        checkboxRow = ft.Row(
            controls= [leftColumn, rightColumn],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.START, 
            spacing= 20
        )

        buttonRow = ft.Row(
            controls= [self.return_button(self.return_to_main), generateRoutineButton],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 60
        )

        mainColumn = ft.Column(
            controls= [checkboxRow, buttonRow],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 60
        )

        mainContainer = ft.Container(
            content= mainColumn,
            alignment= ft.alignment.center,
            margin= ft.margin.only(top= 100)
        )

        self.page.clean()
        self.page.add(mainContainer)
        self.page.update()

    def generate_routine(self, e):
        wrinkles = self.wrinklesCheckbox.value
        acne = self.acneCheckbox.value
        pores = self.poresCheckbox.value
        pigmentation = self.pigmentationCheckbox.value
        texture = self.textureCheckbox.value
        irritation = self.irritationCheckbox.value
        dehydration = self.dehydrationCheckbox.value
        oil = self.excessOilCheckbox.value

        skinWorries = SkinConcerns(wrinkles, acne, pores, pigmentation, 
                                    texture, irritation, dehydration, oil)
        
        self.controller.generate_routine(skinWorries)

    def recommended_routine_screen(self, routine):
        title = ft.Text(
            "Ativos recomendados", font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.DISPLAY_SMALL
        )

        subtitle = ft.Text(
            "Com base nas suas escolhas, montamos a seguinte rotina: ",
            font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.HEADLINE_MEDIUM
        )

        morningLabel = ft.Row(
            [
                ft.Icon(name= ft.icons.SUNNY, color= ft.colors.BLACK, size= 30),
                ft.Text(
                    "Manhã: ", font_family= "AlbertSans", 
                    theme_style= ft.TextThemeStyle.HEADLINE_MEDIUM
                )
            ],
            spacing= 10
        )

        nightLabel = ft.Row(
            [
                ft.Icon(name= ft.icons.NIGHTLIGHT, color= ft.colors.BLACK, size= 30),
                ft.Text(
                    "Noite: ", font_family= "AlbertSans", 
                    theme_style= ft.TextThemeStyle.HEADLINE_MEDIUM
                )
            ],
            spacing= 10
        )

        cleanserAMLabel = ft.Row(
            [
                ft.Text(
                    "Limpeza: ", font_family= "AlbertSans",
                    theme_style= ft.TextThemeStyle.TITLE_LARGE,
                ),
                ft.Text(
                    routine.cleanser, 
                    theme_style= ft.TextThemeStyle.TITLE_MEDIUM
                )
            ],
            spacing= 10
        )
        treatmentAMLabel = ft.Row(
            [
                ft.Text(
                    "Tratamento: ", font_family= "AlbertSans",
                    theme_style= ft.TextThemeStyle.TITLE_LARGE
                    ),
                ft.Text(
                    routine.treatmentAM, 
                    theme_style= ft.TextThemeStyle.TITLE_MEDIUM
                )
            ],
            spacing= 10
        )
        moisturizerAMLabel = ft.Row(
            [
                ft.Text(
                    "Hidratação: ", font_family= "AlbertSans",
                    theme_style= ft.TextThemeStyle.TITLE_LARGE
                    ),
                ft.Text(
                    routine.moisturizerAM, 
                        theme_style= ft.TextThemeStyle.TITLE_MEDIUM
                )
            ],
            spacing= 10
        )        
        sunProtectionLabel = ft.Row(
            [
                ft.Text(
                    "Proteção solar: ", font_family= "AlbertSans", 
                    theme_style= ft.TextThemeStyle.TITLE_LARGE
                    ),
                ft.Text(
                    routine.sunscreen, 
                    theme_style= ft.TextThemeStyle.TITLE_MEDIUM
                )
            ],
            spacing= 10
        )

        cleanserPMLabel = ft.Row(
            [
                ft.Text(
                    "Limpeza: ", font_family= "AlbertSans",
                    theme_style= ft.TextThemeStyle.TITLE_LARGE
                    ),
                ft.Text(
                    "Cleansing oil + " + routine.cleanser, 
                    theme_style= ft.TextThemeStyle.TITLE_MEDIUM
                )
            ],
            spacing= 10
        )
        treatmentPMLabel = ft.Row(
            [
                ft.Text(
                    "Tratamento: ", font_family= "AlbertSans",
                    theme_style= ft.TextThemeStyle.TITLE_LARGE
                    ),
                ft.Text(
                    routine.treatmentPM,
                    theme_style= ft.TextThemeStyle.TITLE_MEDIUM
                )
            ],
            spacing= 10
        )
        moisturizerPMLabel = ft.Row(
            [
                ft.Text(
                    "Hidratação: ", font_family= "AlbertSans",
                    theme_style= ft.TextThemeStyle.TITLE_LARGE
                    ),
                ft.Text(
                    routine.moisturizerPM,
                    theme_style= ft.TextThemeStyle.TITLE_MEDIUM
                )
            ],
            spacing= 10
        )

        titleColumn = ft.Column(
            [title, subtitle],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.START
        )

        titleContainer = ft.Container(
            content= titleColumn,
            margin= ft.margin.only(left= 40)
        )

        leftColumn = ft.Column(
            [
                morningLabel, cleanserAMLabel, 
                treatmentAMLabel, moisturizerAMLabel, sunProtectionLabel
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.START,
            spacing= 20
        )

        rightColumn = ft.Column(
            [
                nightLabel, cleanserPMLabel, 
                treatmentPMLabel, moisturizerPMLabel
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.START,
            spacing= 20
        )

        mainRow = ft.Row(
            [leftColumn, rightColumn],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 100
        )

        buttonRow = ft.Row(
            [self.return_button(self.return_to_main)],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER
        )

        mainColumn = ft.Column(
            [titleContainer, mainRow, buttonRow],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.START,
            spacing= 60
        )

        mainContainer = ft.Container(
            content= mainColumn,
            margin= ft.margin.only(top= 100),
            alignment= ft.alignment.center
        )

        self.page.clean()
        self.page.add(mainContainer)
        self.page.update()

    def diary_screen(self, entries_list):
        
        title = ft.Text(
            "Diário de progresso", font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.DISPLAY_SMALL
        )

        self.entries = ft.GridView(
            auto_scroll= True, 
            runs_count= 4,
            max_extent= 250,
            spacing= 20,
            run_spacing= 20,
            #child_aspect_ratio= 2.5
        )

        titleEntriesColumn = ft.Column(
            [title, self.entries],
            alignment= ft.MainAxisAlignment.CENTER, 
            horizontal_alignment= ft.CrossAxisAlignment.START,
        )

        mainContainer = ft.Container(
            content = titleEntriesColumn,
            margin = ft.margin.only(top=80, left= 100, right= 100)
        )

        returnButtonContainer = ft.Container(
            content= self.return_button(self.return_to_main),
            alignment= ft.alignment.center
        )

        mainColumn = ft.Column(
            [mainContainer, returnButtonContainer],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.START,
            spacing= 30
        )

        self.add_button_to_diary_screen(entries_list)

        self.page.clean()
        self.page.add(mainColumn)
        self.page.update()

    def update_entry_screen(self):

        entryDate = "Data da entrada"
        description = "Descrição da pele"
        image = ft.Image(
            src= f"assets/images/produtos.jpg",
            width= 535,
            height= 660,
            fit= ft.ImageFit.CONTAIN
        )

        title = ft.Text(
            entryDate, font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.DISPLAY_SMALL
        )

        dateLabel = ft.Text(
            "Data: ", font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.HEADLINE_SMALL
        )

        dateTextfield = ft.TextField(
            value= entryDate,
            width= 390, 
            height= 40,
            border= ft.InputBorder.OUTLINE, border_color= self.WHITE,
            border_radius= ft.border_radius.all(10),
            filled= True, fill_color= self.WHITE
        )

        descriptionLabel = ft.Text(
            "Descrição: ", font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.HEADLINE_SMALL
        )

        descriptionTextfield = ft.TextField(
            value= description,
            multiline= True,
            min_lines= 10,
            width= 390,
            border= ft.InputBorder.OUTLINE, border_color= self.WHITE,
            border_radius= ft.border_radius.all(15),
            filled= True, fill_color= self.WHITE
        )

        imageUploadButton = ft.FilledButton(
            text= "Upload de foto",
            width=  240,
            height= 33,
            style= ft.ButtonStyle(
                bgcolor= self.DARKGRAY,
                shape= ft.RoundedRectangleBorder(radius= 12),
                text_style= ft.TextStyle(
                    size= 20, weight= ft.FontWeight.W_400
                )
            )
        )

        imageDeleteButton = ft.FilledButton(
            text= "Deletar foto",
            width= 190,
            height= 33,
            style= ft.ButtonStyle(
                bgcolor= self.LIGHTGRAY,
                shape= ft.RoundedRectangleBorder(radius= 12),
                text_style= ft.TextStyle(
                    size= 20, weight= ft.FontWeight.W_400
                )
            )
        )

        imageContainer = ft.Container(
            content= image,
            width= 450,
            height= 375,
            bgcolor= self.WHITE, 
            border_radius= 10
        )

        updateEntryButton = ft.FilledButton(
            text= "Atualizar",
            style= ft.ButtonStyle(
                padding= ft.Padding(40, 10, 40, 10),
                bgcolor= {"": self.ROSEQUARTZ, "hovered": self.PALESALMON},
                text_style = ft.TextStyle(size= 22)
            )
        )

        leftColumn = ft.Column(
            controls= [
                title, dateLabel, dateTextfield, 
                descriptionLabel, descriptionTextfield
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.START,
            spacing= 15
        )

        imageButtonRow = ft.Row(
            controls = [imageUploadButton, imageDeleteButton],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER
        )

        rightColumn = ft.Column(
            controls= [ft.Container(height= 30), imageButtonRow, imageContainer],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 15
        )

        buttonRow =  ft.Row(
            controls= [self.return_button(), updateEntryButton],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 60
        )

        mainRow = ft.Row(
            controls= [leftColumn, rightColumn],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 40
        )

        updateEntryScreenFrame = ft.View(
            route = "/",
            controls= [mainRow, buttonRow],
            horizontal_alignment= ft.MainAxisAlignment.CENTER,
            padding= ft.padding.all(40),
            spacing= 40
        )
        updateEntryScreenFrame.bgcolor = self.BEIGE
        return updateEntryScreenFrame

    def entry_screen(self):

        entryDate = "Data da entrada"
        description = "Pele com manchinhas de acne, cravos profundos e acne cística no queixo e parte inferior do rosto. Ressecamento na testa e bochechas."
        image = ft.Image(
            src= f"assets/images/produtos.jpg",
            width= 535,
            height= 660,
            fit= ft.ImageFit.CONTAIN
        )
 
        title = ft.Row( 
            controls = [
                ft.Text(
                    entryDate, font_family= "AlbertSans",
                    theme_style= ft.TextThemeStyle.DISPLAY_SMALL
                ),
                ft.Container(width= 520)
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER
        )

        descriptionLabel = ft.Text(
            "Descrição: ", font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.TITLE_LARGE,
        )

        descriptionText = ft.Column(
            [
                ft.Text(
                    description, theme_style= ft.TextThemeStyle.TITLE_LARGE,
                    size= 20,
                    no_wrap= False,
                   width= 300   
                ),
            ],
            height= 200,
            scroll= ft.ScrollMode.ALWAYS
        )

        imageContainer = ft.Container(
            content= image,
            width= 450,
            height= 375,
            bgcolor= self.WHITE, 
            border_radius= 10
        )

        next_button = ft.FilledButton(
            text= "Próximo",
            style= ft.ButtonStyle(
                padding= ft.Padding(40, 10, 40, 10),
                bgcolor= {"": self.ROSEQUARTZ, "hovered": self.PALESALMON},
                text_style = ft.TextStyle(size= 22)
            )
        )

        descriptionColumn = ft.Column(
            [descriptionLabel, descriptionText],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.START,
            spacing= 20
        )

        mainRow = ft.Row(
            [descriptionColumn, imageContainer],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 40
        )

        buttonRow = ft.Row(
            [self.return_button(), next_button],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 60
        )

        mainColumn = ft.Column(
            [title, mainRow, buttonRow],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 40
        )

        entryScreenFrame = ft.View(route= "/", controls= [mainColumn],
            horizontal_alignment= ft.MainAxisAlignment.CENTER,
            padding= ft.padding.all(60),
            spacing= 40
        )
        entryScreenFrame.bgcolor = self.BEIGE
        return entryScreenFrame 

    def add_button_to_diary_screen(self, entries_list):
        for entry in entries_list:
            button = ft.Container( 
                    content= ft.ListTile(    
                        title= ft.FilledButton(
                            text= entry["date"],
                            #on_click= self.go_to_entry_screen(entry["_id"]),
                            style= ft.ButtonStyle(
                                color= ft.colors.BLACK,
                                bgcolor= ft.colors.TRANSPARENT,
                                overlay_color= ft.colors.TRANSPARENT,
                                text_style= ft.TextStyle(
                                    size= 24, 
                                    decoration= ft.TextDecoration.UNDERLINE,
                                    font_family= "Albert Sans",
                                    weight= ft.FontWeight.W_300
                                )
                            )
                        ),
            
                        trailing= ft.PopupMenuButton(
                        icon= ft.icons.MORE_VERT,
                        items= [
                            ft.PopupMenuItem(text="Editar", 
                                #on_click= self.go_to_update_entry_screen(entry["_id"])
                            ),
                            ft.PopupMenuItem(text="Excluir"
                            )
                        ]
                        ),
                    bgcolor= self.PALESALMON 
                    ),
                    padding= 10,
                    border_radius= ft.border_radius.all(15),
                    alignment= ft.alignment.center,
                    width= 300
                )
            self.entries.controls.append(button)

        self.page.update()

    def return_button(self, action):
        returnButton = ft.FilledButton(
            text= "Voltar",
            on_click= action,
            style= ft.ButtonStyle(
                bgcolor= {"": ft.colors.TRANSPARENT, "hovered": self.BEIGE}, 
                color= ft.colors.BLACK,
                side= ft.BorderSide(
                color= ft.colors.BLACK, width= 0.5),
                padding= ft.Padding(60, 10, 60, 10),
                text_style= ft.TextStyle(size= 22)
            )
        )                      
        return returnButton
    
    def return_to_login(self, e):
        self.page.clean()
        self.page.add(self.login_screen())

    def return_to_main(self, e):
        self.page.clean()
        self.page.add(self.mainScreenContainer)

    def success_alert_modal(self, message, description):
        ok_button = ft.FilledButton(
            text= "Ok",
            on_click= self.close_success_modal,
            style= ft.ButtonStyle(
                bgcolor= self.LIGHTGRAY,
                color= self.WHITE,
                padding= ft.Padding(40, 10, 40, 10),
                text_style= ft.TextStyle(size=22)
            )
        )

        self.success_modal = ft.AlertDialog(
            modal= True, 
            bgcolor= self.ROSEQUARTZ,
            title= ft.Text(message + " com sucesso!"),
            content= ft.Text(description),
            actions= [ok_button],
            actions_alignment= ft.MainAxisAlignment.CENTER,
            on_dismiss= self.return_to_login
        )

        self.page.open(self.success_modal)
        self.page.update()

    def close_success_modal(self, e):
        self.page.close(self.success_modal)

    def fail_alert_modal(self, message, errorDescription):
        ok_button = ft.FilledButton(
            text= "Ok",
            on_click= self.close_fail_modal,
            style= ft.ButtonStyle(
                bgcolor= self.LIGHTGRAY,
                color= self.WHITE,
                padding= ft.Padding(40, 10, 40, 10),
                text_style= ft.TextStyle(size=22)
            )
        )

        self.fail_modal = ft.AlertDialog(
            modal= True,
            bgcolor= self.ROSEQUARTZ,
            title= ft.Text("Erro ao " + message),
            content= ft.Column(controls= [ft.Text(errorDescription)], tight= True),
            actions= [ok_button],
            actions_alignment= ft.MainAxisAlignment.CENTER,
        )
        self.page.open(self.fail_modal)
        self.page.update()

    def close_fail_modal(self, e):
        self.page.close(self.fail_modal)

    def init(self):
        ft.app(target= self.screen_manager)

    def screen_manager(self, page: ft.Page):
        self.page = page
        self.page.fonts = {"AlbertSans": "assets/fonts/AlbertSans-Light.ttf"}
        self.page.bgcolor = self.BEIGE
        
        self.page.add(self.login_screen())
        self.page.update()

