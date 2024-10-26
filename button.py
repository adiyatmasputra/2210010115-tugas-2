import PySimpleGUI as sg
sg.theme("LightBlue2")
sg.theme_text_color("#F5F5DC")
window = sg.Window(title="Contoh Button",
                   layout=[[sg.Text("Contoh Button")],
                           [sg.Button("Button Simpan")],
                           [sg.Button("Button Keluar")]
                           ],
                           size=(400,200),
                           font=("Times", 18))
kejadian,nilai = window.read()
print(kejadian,"=>",nilai)
window.close()