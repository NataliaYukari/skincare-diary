import flet as ft
from models.entry import Entry


class UpdateEntryScreen(ft.Container):


    def __init__(self, view, filePicker):
        super().__init__()
        self.view = view
        self.imagePath = None
        self.filePicker = filePicker
        self.filePicker.on_result= self.entry_image_update

    def update_entry_screen(self, entryData, imagePath):
        entryDate = entryData["date"]
        description = entryData["description"]

        image = ft.Image(
            src_base64= imagePath,
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

        self.updateDateTextfield = ft.TextField(
            value= entryDate,
            width= 390, 
            height= 40,
            border= ft.InputBorder.OUTLINE, border_color= self.view.WHITE,
            border_radius= ft.border_radius.all(10),
            filled= True, fill_color= self.view.WHITE
        )

        descriptionLabel = ft.Text(
            "Descrição: ", font_family= "AlbertSans",
            theme_style= ft.TextThemeStyle.HEADLINE_SMALL
        )

        self.updateDescriptionTextfield = ft.TextField(
            value= description,
            multiline= True,
            min_lines= 10,
            width= 390,
            border= ft.InputBorder.OUTLINE, border_color= self.view.WHITE,
            border_radius= ft.border_radius.all(15),
            filled= True, fill_color= self.view.WHITE
        )

        imageUpdateButton = ft.FilledButton(
            text= "Upload de foto",
            on_click= lambda _: self.filePicker.pick_files(),
            width=  240,
            height= 33,
            style= ft.ButtonStyle(
                bgcolor= self.view.DARKGRAY,
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
                bgcolor= self.view.LIGHTGRAY,
                shape= ft.RoundedRectangleBorder(radius= 12),
                text_style= ft.TextStyle(
                    size= 20, weight= ft.FontWeight.W_400
                )
            )
        )

        self.updateImageContainer = ft.Container(
            content= image,
            width= 450,
            height= 375,
            bgcolor= self.view.WHITE, 
            border_radius= 10
        )

        updateEntryButton = ft.FilledButton(
            text= "Atualizar",
            on_click= lambda e: self.update_entry(entryData["_id"]),
            style= ft.ButtonStyle(
                padding= ft.Padding(40, 10, 40, 10),
                bgcolor= {"": self.view.ROSEQUARTZ, "hovered": self.view.PALESALMON},
                text_style = ft.TextStyle(size= 22)
            )
        )

        leftColumn = ft.Column(
            controls= [
                title, dateLabel, self.updateDateTextfield, 
                descriptionLabel, self.updateDescriptionTextfield
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.START,
            spacing= 15
        )

        imageButtonRow = ft.Row(
            controls = [imageUpdateButton, imageDeleteButton],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER
        )

        rightColumn = ft.Column(
            controls= [ft.Container(height= 30), imageButtonRow, self.updateImageContainer],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            spacing= 15
        )

        buttonRow =  ft.Row(
            controls= [self.view.return_button(self.view.return_to_diary), updateEntryButton],
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

        self.content = mainContainer
        self.view.page.add(self.filePicker)

    def entry_image_update(self, e):
        if e.files:
            self.imagePath = e.files[0].path

        image = ft.Image(
            src= self.imagePath, 
            width= 535,
            height= 660,
            fit= ft.ImageFit.CONTAIN
        )

        self.updateImageContainer.content = image
        self.view.page.update()

    def entry_image_delete(self, e):
        self.updateImageContainer.content = None
        self.view.page.update()

    def update_entry(self, entryId):
        newDate = self.updateDateTextfield.value
        newDescription = self.updateDescriptionTextfield.value
        newImage = self.imagePath

        newEntryData = Entry(newDate, newDescription, newImage)
        self.view.controller.update_entry(entryId, newEntryData)