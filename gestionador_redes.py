# Programa simple de gestion de dispositivos de red

dispositivos = []

# Leer archivo
def cargar_desde_archivo():
    try:
        with open("dispositivos.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                
                dispositivo = {
                    "nombre": datos[0],
                    "ip": datos[1],
                    "vlans": datos[2],
                    "servicios": datos[3],
                    "capa": datos[4]
                }
                
                dispositivos.append(dispositivo)
        print("Datos cargados correctamente.\n")
    except:
        print("No se pudo leer el archivo.\n")

# Agregar dispositivo
def agregar_dispositivo():
    nombre = input("Nombre: ")
    ip = input("IP: ")
    vlans = input("VLANs: ")
    servicios = input("Servicios: ")
    capa = input("Capa (Acceso/Distribucion/Core): ")
    
    dispositivo = {
        "nombre": nombre,
        "ip": ip,
        "vlans": vlans,
        "servicios": servicios,
        "capa": capa
    }
    
    dispositivos.append(dispositivo)
    print("Dispositivo agregado.\n")

# Mostrar dispositivos
def mostrar_dispositivos():
    if len(dispositivos) == 0:
        print("No hay dispositivos.\n")
    else:
        for d in dispositivos:
            print("----------------------")
            print("Nombre:", d["nombre"])
            print("IP:", d["ip"])
            print("VLANs:", d["vlans"])
            print("Servicios:", d["servicios"])
            print("Capa:", d["capa"])
        print("----------------------\n")

# Menu principal
def menu():
    while True:
        print("1. Cargar archivo")
        print("2. Agregar dispositivo")
        print("3. Mostrar dispositivos")
        print("4. Salir")
        
        opcion = input("Seleccione: ")
        
        if opcion == "1":
            cargar_desde_archivo()
        elif opcion == "2":
            agregar_dispositivo()
        elif opcion == "3":
            mostrar_dispositivos()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida\n")

menu()