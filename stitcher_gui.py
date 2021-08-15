from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.filechooser import FileChooserListView

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '450')
Config.write()

#main window
class Stitcher(App):
    def build(self):
        layout = GridLayout(
                cols = 1,
                rows = 2,
                rows_minimum = {1:200,2:50},
                spacing = 10,
                #padding = 10,
                pos_hint = {"center_x":0.5,
                            "center_y":0.5
                            }
                )
        layout.add_widget(Label(text='Stitcher',  font_size='50sp'))

        self.filechooser = FileChooserListView(
                                              rootpath=".\\",
                                              path=".\\input",
                                              multiselect=True
                                              )
        layout.add_widget(self.filechooser)

        #layout.add_widget(Label(text='Body',  font_size='50sp'))
        return(layout)

Stitcher().run()