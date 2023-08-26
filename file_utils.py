import PySimpleGUI as sg

from layout import layout
from consts import FILES_KEY, MERGE_KEY
from mergePDF import MergePDF


window = sg.Window('File Utils', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == MERGE_KEY:
        files = values[FILES_KEY] .split(";")

        try:
            mergePDF = MergePDF()
            mergePDF.merge_files(files)
            sg.Popup("Done", keep_on_top=True)
            break
        except Exception as e:
            print("Error ooccured: {}".format(e))

window.close()
