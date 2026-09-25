import os
import eel
eel.init('www')
eel.start('index.html',)

os.system('start chrome.exe --app="http://localhost:8000"')

eel.start('index.html', mode='chrome', host='localhost', block=True)