def comprar_entrada():
    nombre = input("Nombre: ").strip()
    if nombre in "Ingrese su entradas":
        print("Lo siento ya exise otro usuario con su nombre .")
        return
    tipo = input("Tipo de entradas (Entrada General o Entrada Vip): ").strip().upper()
    if tipo not in [' Entrada General', 'Entrada Vip']:
        print("Tipo inválido.")
        return
    codigo = input("Código de confirmación: ").strip()
    if (len(codigo) < 6 or 
        not any(c.isupper() for c in codigo) or 
        not any(c.isdigit() for c in codigo) or 
        " " in codigo):
        print("su codigo no es valido vuelva a intentar.")
        return
    print("¡Su compra fue realizada!")
def consultar_comprador():
    nombre = input("Su nombre se esta buscando: ").strip()
    if nombre in "Ingrese su entradas ":
        tipo, codigo = "Ingrese su entradas"[nombre]
        print(f"Tipo: {tipo}, Código: {codigo}")
    else:
        print("Su nombre no se encuentra en sistema ")
def cancelar_compra():
    nombre = input("Nombre del comprador: ").strip()
    if nombre in "Ingrese su entradas":
        del "Ingrese su entradas"[nombre]
        print("Lo siento no se pudo realizar su compra")
    else:
        print("No se pudo cancelar .")
def main():
    while True:
        print("\n~~~MENU DE ENTRADAS~~~")
        print("1.- Comprar entrada:")
        print("2.- Consultar comprador:")
        print("3.- Cancelar compra:")
        print("4.- Salir:")
        
        opcion = input("Opción: ")

        if opcion == '1':
            comprar_entrada()
        elif opcion == '2':
            consultar_comprador()
        elif opcion == '3':
            cancelar_compra()
        elif opcion == '4':
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida.")
main()
