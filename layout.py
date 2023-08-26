import PySimpleGUI as sg
from consts import FILES_KEY, MERGE_KEY

layout = [
    [
        sg.Text('Select files'),
        sg.Input(key=FILES_KEY),
        sg.FilesBrowse()
    ],
    [
        sg.Button("Merge", key=MERGE_KEY),
    ]
]
