import toga

def build(app):
    box = toga.Box()
    return box

#crear ventana
def main():
    app = toga.App("Hola mundo", "com.codigofacilito.toga", startup=build)#(titulo, identifacador unico, startup = crear una funcion a llamar o callback )
    return app

if __name__ == "__main__":
    app = main()
    app.main_loop()