import PySimpleGUI as sg
susunan = [[sg.VPush()],
           [sg.Text("UNISKA MAB", font=("Times New Roman",24))],
           [sg.Text("Banjarmasin", font=("Helvtica",18))],
           [sg.VPush()]]
Window = sg.Window(title="Elemen Text",
                   layout=susunan,
                   element_justification = "center",
                   size=(430,200))
Window.read()
Window.close()