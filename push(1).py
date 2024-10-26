import PySimpleGUI as sg
susunan=[[sg.Push(),
          sg.Text("UNISKA MAB", font=("Times New Roman",24)),
          sg.Push()],
          [sg.Text("BANJARMASIN", font=("Helvtica",18)),
          sg.Push()]
          ]
window = sg.Window(title="Elemen Text",
                    layout=susunan,
                    size=(430,200))
window()
window.close()      