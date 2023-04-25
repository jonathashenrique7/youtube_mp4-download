import webbrowser as web
import PySimpleGUI as gui 
import time 
from pytube import YouTube 

def executar_download( link, path ) -> any:
    video = YouTube(link)
    video.streams.get_highest_resolution().download(output_path=path)
    
gui.theme('Reddit')

layout = [
    [ gui.Text('Link do vídeo: '), gui.InputText(size=(40, 1)) ],
    [ gui.Text('Onde encaminhar: '), gui.InputText(size=(40, 1)), gui.FolderBrowse('Encontrar') ],
    [ gui.Button('Baixar')],
]

janela = gui.Window('Baixador de vídeos Youtube', layout)

while True: 
    event, values = janela.read()

    if event == gui.WINDOW_CLOSED:
        break
    elif event == 'Baixar':
        executar_download( values[0], values[1] )
        gui.popup_ok('Download realizado!')

janela.close()

