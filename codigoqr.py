import qrcode

def QR_color(name, url, back, fill):
    '''Función que se hará cargo de generar el Código QR con color.Parámetros:
    -name: nombre el cuál se llamará la imagen .png.
    -url: contenido del Código QR, ya sea URL o un texto en general.
    -back: color de fondo.
    -fill: color del contenido del código.
    '''

    qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
)

    url = qrcode.make(url)
    type(url)
    url = qr.make_image(back_color=back, fill_color=fill) #Color de fondo, Color de relleno
    url.save(name + '.png') 



def QR(name, url):
    '''Función que se hará cargo de generar el Código QR sin color.Parámetros:
    -name: nombre el cuál se llamará la imagen .png.
    -url: contenido del Código QR, ya sea URL o un texto en general.
    '''

    url = qrcode.make(url)
    type(url)
    url.save(name + '.png') 


#El usuario escogerá como generar su código:
while True:
    option = int(input('''
Menú:
1 - Código QR Normal.
2 - Código QR Personalizable.
3 - Salir.

>>> '''))

    if option == 1:
        name = input("¿Como quiere llamar su código QR?: ")
        url = input("URL o Contenido para el código: ")
        
        #Llamada a la función
        QR(name,url)
        break #Fin

    elif option == 2:
        name = input("¿Como quiere llamar su código QR?: ")
        url = input("URL o Contenido para el código: ")
        #Para los colores se deberá llamarse con su nombre en inglés.
        back = input("Ingrese el color de fondo (en inglés): ")
        fill = input("Ingrese el color de su código (en inglés): ")
        
        #Llamada a la función
        QR_color(name, url, back, fill)
        break #Fin

    elif option == 3:
        break #Fin

    else:
        print("ERROR!")



