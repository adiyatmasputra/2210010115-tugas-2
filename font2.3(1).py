import PySimpleGUI as sg
sg.theme("LightBlue2")
sg.theme_text_color("#F5F5DC")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("FTI UNISKA",font=("Helvetiva",24))],
[sg.Text("FAKULTAS TEKNOLOGI INFORMASI",font=("Courier",18,"italic","bold","underline"))],
 [sg.Text("UNISKA MAB BANJARMASIN")]],
 size=(439,200),
 font=("Times", 18))
 
window()
window.close()