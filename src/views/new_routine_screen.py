import flet as ft
from models.skin_concerns import SkinConcerns

class NewRoutineScreen(ft.Container):


    def __init__(self, view):
        super().__init__()
        self.view = view

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
            fill_color= view.WHITE,
            check_color= view.ROSEQUARTZ, active_color= view.ROSEQUARTZ,
            border_side= ft.BorderSide(color= view.WHITE, width= 1),
            scale= 1.5
        )

        self.acneCheckbox = ft.Checkbox(
            value= False,
            fill_color= view.WHITE,
            check_color= view.ROSEQUARTZ, active_color= view.ROSEQUARTZ,
            border_side= ft.BorderSide(color= view.WHITE, width= 1),
            scale= 1.5
        )

        self.poresCheckbox = ft.Checkbox(
        value= False,
        fill_color= view.WHITE,
        check_color= view.ROSEQUARTZ, active_color= view.ROSEQUARTZ,
        border_side= ft.BorderSide(color= view.WHITE, width= 1),
        scale= 1.5
        )

        self.pigmentationCheckbox = ft.Checkbox(
        value= False,
        fill_color= view.WHITE,
        check_color= view.ROSEQUARTZ, active_color= view.ROSEQUARTZ,
        border_side= ft.BorderSide(color= view.WHITE, width= 1),
        scale= 1.5
        )

        self.textureCheckbox = ft.Checkbox(
        value= False,
        fill_color= view.WHITE,
        check_color= view.ROSEQUARTZ, active_color= view.ROSEQUARTZ,
        border_side= ft.BorderSide(color= view.WHITE, width= 1),
        scale= 1.5
        )

        self.irritationCheckbox = ft.Checkbox(
        value= False,
        fill_color= view.WHITE,
        check_color= view.ROSEQUARTZ, active_color= view.ROSEQUARTZ,
        border_side= ft.BorderSide(color= view.WHITE, width= 1),
        scale= 1.5
        )

        self.dehydrationCheckbox = ft.Checkbox(
        value= False,
        fill_color= view.WHITE,
        check_color= view.ROSEQUARTZ, active_color= view.ROSEQUARTZ,
        border_side= ft.BorderSide(color= view.WHITE, width= 1),
        scale= 1.5
        )

        self.excessOilCheckbox = ft.Checkbox(
        value= False,
        fill_color= view.WHITE,
        check_color= view.ROSEQUARTZ, active_color= view.ROSEQUARTZ,
        border_side= ft.BorderSide(color= view.WHITE, width= 1),
        scale= 1.5
        )

        generateRoutineButton = ft.FilledButton(
            text= "Gerar rotina",
            on_click= self.generate_routine,
            style= ft.ButtonStyle(
                padding= ft.Padding(40, 10, 40, 10),
                bgcolor= {"": view.ROSEQUARTZ, "hovered": view.PALESALMON},
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
            controls= [view.return_button(view.return_to_main), generateRoutineButton],
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

        self.content = mainContainer

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
        
        self.view.controller.generate_routine(skinWorries)