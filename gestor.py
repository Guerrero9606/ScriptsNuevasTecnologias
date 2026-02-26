def menu():
    print("---MENU---")
    print("Bienvenido por favor ingrese una opcion: ")
    opciones = """  1) Agregar productos
                    2) Ver inventario
                    3) Consultar
                    4) Salir
    """
    print(opciones)

def main():
    inventario = [] #Guardar los productos
    while(True):
        menu()
        opcion = int(input("Seleccione una opcion:\n"))

        if opcion == 1:
            print("NUEVO PRODUCTO")
            nombre = input("Ingrese el nombre: ")
            precio = float(input("Ingrese el precio: "))
            cantidad = int(input("Ingrese la cantidad: "))
            producto = {"Nombre": nombre,
                        "Precio": precio}
            producto["Cantidad"] = cantidad

            inventario.append(producto)
            print("Producto guardado con exito")

        elif opcion == 2:
            print("Inventario actual")
            if len(inventario) == 0:
                print("Inventario vacio.")
            else:
                for item in inventario:
                    print(f"Nombre del producto {item["Nombre"]}\
                          y el precio es {item["Precio"]} y su \
                            cantidad es {item["Cantidad"]}")

        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()