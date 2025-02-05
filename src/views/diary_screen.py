import flet as ft

class DiaryScreen(ft.Container):


    def __init__(self, view):
        super().__init__()
        self.view = view

        self.view.page.update()

    def diary_screen(self, entries_list):
        
        title = ft.Text(
            "Diário de progresso", font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.DISPLAY_SMALL
        )

        self.entries = ft.GridView(
            auto_scroll= True, 
            runs_count= 4,
            max_extent= 250,
            spacing= 10,
            run_spacing= 20,
            child_aspect_ratio= 2.5
        )

        titleEntriesColumn = ft.Column(
            [title, self.entries],
            alignment= ft.MainAxisAlignment.START, 
            horizontal_alignment= ft.CrossAxisAlignment.START,
        )

        mainContainer = ft.Container(
            content = titleEntriesColumn,
            margin = ft.margin.only(top=80, left= 100, right= 100)
        )

        returnButtonContainer = ft.Container(
            content= self.view.return_button(self.view.return_to_main),
            alignment= ft.alignment.center
        )

        self.diaryScreenColumn = ft.Column(
            [mainContainer, returnButtonContainer],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.START,
            spacing= 30
        )

        self.add_button_to_diary_screen(entries_list)

        self.content = self.diaryScreenColumn

    def add_button_to_diary_screen(self, entries_list):
        for index, (entry) in enumerate(entries_list):
            button = ft.Container( 
                    content= ft.ListTile(    
                        title= ft.FilledButton(
                            text= entry["date"],
                            on_click= lambda e, entry=entry, index=index: 
                                self.view.go_to_entry_screen(entry["_id"], index),
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
                                on_click= lambda e, entry=entry:
                                self.view.go_to_update_entry_screen(entry["_id"])
                            ),
                            ft.PopupMenuItem(text="Excluir",
                                on_click= lambda e, entry=entry: 
                                self.view.delete_entry(entry["_id"])
                            )
                        ]
                        ),
                    bgcolor= self.view.PALESALMON 
                    ),
                    padding= 10,
                    border_radius= ft.border_radius.all(15),
                    alignment= ft.alignment.center,
                    width= 300
                )
            self.entries.controls.append(button)

        self.view.page.update()