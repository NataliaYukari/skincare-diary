import flet as ft

class RecommendedRoutineScreen(ft.Container):


    def __init__(self, view):
        super().__init__()
        self.view = view

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
            [self.view.return_button(self.view.return_to_main)],
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

        self.content = mainContainer