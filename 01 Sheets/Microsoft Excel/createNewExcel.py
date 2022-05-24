import xlsxwriter


# esta librería sirve solo para crear documentos
# en el siguiente link se puede ver la documentación de la librería que usaremos
# https://github.com/jmcnamara/XlsxWriter

def main():
    # Indicamos en donde queremos crear un archivo excel, tener en cuenta que la carpeta debe existir previamente.
    workbook = xlsxwriter.Workbook('out/mi curso favorito3.xlsx')

    # Agregamos una nueva hoja al excel
    worksheet = workbook.add_worksheet()

    # Escribimos en una celda
    worksheet.set_column('A:A', 20)

    # volvemos a escribir en una celda
    worksheet.write('A1', 'Hello')

    # creamos un estilo
    bold = workbook.add_format({'bold': True})

    # Usamos el estilo en otra celda
    worksheet.write('A2', 'World', bold)

    # escribimos en celdas usando otra notacion
    worksheet.write(2, 0, 123)
    worksheet.write(3, 0, 123.456)

    # agregamos una imagen en el excel
    worksheet.insert_image('B10', '../Media/gato.png')

    # cerramos el archivo
    workbook.close()


if __name__ == '__main__':
    main()
