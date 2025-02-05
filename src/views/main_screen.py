import flet as ft
 

class MainScreen(ft.Container):


    def __init__(self, view):
        super().__init__()
        self.view = view

        title = ft.Text(
            "Bem-vindo!", font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.DISPLAY_SMALL)
        
        createRoutineButton = ft.FilledButton(
            text= "Montar rotina",
            on_click= view.go_to_routine_form,
            width= 390,
            height= 50,
            style= ft.ButtonStyle(
                bgcolor= {"": view.ROSEQUARTZ, "hovered": view.PALESALMON},
                padding= ft.padding.all(10),
                shape= ft.RoundedRectangleBorder(radius= 15),
                text_style= ft.TextStyle(
                    size= 24, weight= ft.FontWeight.W_400
                )
            )
        )
    
        showRoutineButton = ft.FilledButton(
            text= "Ver rotina",
            on_click= view.go_to_recommended_routine_screen,
            width= 390,
            height= 50,
            style= ft.ButtonStyle(
                bgcolor= {"": view.PALESALMON, "hovered": view.ROSEQUARTZ},
                padding= ft.padding.all(10),
                shape= ft.RoundedRectangleBorder(radius= 15),
                text_style= ft.TextStyle(
                    size= 24, weight= ft.FontWeight.W_400
                )
            )
        )

        addNewEntryButton = ft.FilledButton(
            text= "Adicionar nova entrada",
            on_click= view.go_to_add_entry_screen,
            width= 390,
            height= 50,
            style= ft.ButtonStyle(
                bgcolor= {"": view.ROSEQUARTZ, "hovered": view.PALESALMON},
                padding= ft.padding.all(10),
                shape= ft.RoundedRectangleBorder(radius= 15),
                text_style= ft.TextStyle(
                    size= 24, weight= ft.FontWeight.W_400
                )
            )
        )
        showDiaryButton = ft.FilledButton(
            text= "Diário de progresso",
            on_click= view.go_to_diary_screen,
            width= 390,
            height= 50,
            style= ft.ButtonStyle(
                bgcolor= {"": view.PALESALMON, "hovered": view.ROSEQUARTZ},
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
        
        self.content = self.mainScreenContainer

