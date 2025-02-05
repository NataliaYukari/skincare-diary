import flet as ft

class EntryScreen(ft.Container):


    def __init__(self, view):
        super().__init__()
        self.view = view

    def entry_screen(self, entryData, imagePath):
        entryDate = entryData["date"]
        description = entryData["description"]

        image = ft.Image(
            src_base64= imagePath,
            width= 535,
            height= 660,
            fit= ft.ImageFit.CONTAIN
        )
 
        title = ft.Row( 
            controls = [
                ft.Text(
                    entryDate, font_family= "AlbertSans",
                    theme_style= ft.TextThemeStyle.DISPLAY_MEDIUM
                ),
                ft.Container(width= 520)
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.START
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
            bgcolor= self.view.WHITE, 
            border_radius= 10
        )

        next_button = ft.FilledButton(
            text= "Próximo",
            on_click= self.go_to_next_entry,
            style= ft.ButtonStyle(
                padding= ft.Padding(40, 10, 40, 10),
                bgcolor= {"": self.view.ROSEQUARTZ, "hovered": self.view.PALESALMON},
                text_style = ft.TextStyle(size= 22)
            )
        )

        previous_button = ft.FilledButton(
            text= "Anterior",
            on_click= self.go_to_previous_entry,
            style= ft.ButtonStyle(
                padding= ft.Padding(40, 10, 40, 10),
                bgcolor= {"": self.view.ROSEQUARTZ, "hovered": self.view.PALESALMON},
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
            [previous_button, self.view.return_button(self.view.return_to_diary), next_button],
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

        mainContainer = ft.Container(
            content= mainColumn,
            margin= ft.margin.only(top= 60)
        )

        self.content = mainContainer

    def go_to_next_entry(self, e):
        self.view.controller.go_to_next_entry()

    def go_to_previous_entry(self, e):
        self.view.controller.go_to_previous_entry()