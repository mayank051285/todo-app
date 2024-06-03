import FreeSimpleGUI

label1 = FreeSimpleGUI.Text("Select files to compress")
test1 = FreeSimpleGUI.Input()
button1 = FreeSimpleGUI.FileBrowse("Choose")

label2 = FreeSimpleGUI.Text("Select destination")
test2 = FreeSimpleGUI.Input()
button2 = FreeSimpleGUI.FolderBrowse("Choose")

button3 = FreeSimpleGUI.Button("Compress")

window = FreeSimpleGUI.Window("Compress", layout=[[label1, test1, button1],
                                                  [label2, test2, button2],
                                                  [button3]])

window.read()
window.close()

