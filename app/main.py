import toga
from consts import *
class PokeDex(toga.App):
    def __init__(self, title, id):
        toga.App.__init__(self, title, id)

        self.title = title
        self.size = (WIDTH, HEIGHT)

        self.heading = ["Nombre"]
        self.data = ["Pyhton", "Rubi", "sql"]

        self.create_elements()

    def startup(self):
        self.main_window = toga.MainWindow("main", title=self.title,
                                            size=self.size)#ancho y alto en px

        box = toga.Box()

        split = toga.SplitContainer()
        split.content = [self.table, box]

        self.main_window.content = split
        self.main_window.show()

    def create_elements(self):
        self.create_table()
    
    def create_table(self):
        self.table = toga.Table(self.heading, data=self.data)

    #CALLBACKS
if __name__ == "__main__":
    Pokedex = PokeDex("Pokedex", "com.codigofacilito.Pokedex")
    Pokedex.main_loop()