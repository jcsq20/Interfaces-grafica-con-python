import toga

#funcionalidad al precionar widget es un disparador para que funcione un evento
def on_press(widget):
    print("Hola mundo utilizando toga")

def new_button():
    button = toga.Button("Hola mundo", on_press=on_press)#(lo que dira el boton, on_press=)
    button.style.padding = 20
    button.style.font_size = 14
    button.style.width = 200
    
    return button

def build(app):
    #creamos nuestra caja
    box = toga.Box()
    #instaciamos el boton
    boton1 = new_button()
    #agregamos el boton a la caja
    box.add(boton1)
    return box

#crear ventana
def main():
    app = toga.App("Hola mundo", "com.codigofacilito.toga", startup=build)#(titulo, identifacador unico, startup = crear una funcion a llamar o callback )
    return app

if __name__ == "__main__":
    app = main()
    app.main_loop()