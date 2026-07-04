from datetime import datetime


ESPECIALIDADES = [
    "Clinica medica",
    "Pediatria",
    "Cardiologia",
    "Traumatologia",
    "Guardia",
]

PRIORIDADES = {
    1: "Alta",
    2: "Media",
    3: "Baja",
}


def mostrar_titulo(texto):
    print("\n" + "=" * 60)
    print(texto.upper())
    print("=" * 60)


def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: el dato no puede quedar vacio.")


def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Error: el valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Error: el valor debe ser menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Error: ingrese un numero entero valido.")


def pedir_dni():
    while True:
        dni = pedir_texto("DNI del paciente: ")
        if dni.isdigit() and len(dni) == 8:
            return dni
        print("Error: el DNI debe tener exactamente 8 digitos numericos.")


def pedir_fecha():
    while True:
        fecha = pedir_texto("Fecha del turno (dd/mm/aaaa): ")
        try:
            fecha_turno = datetime.strptime(fecha, "%d/%m/%Y").date()
            return fecha_turno.strftime("%d/%m/%Y")
        except ValueError:
            print("Error: ingrese una fecha valida con formato dd/mm/aaaa.")


def pedir_hora():
    while True:
        hora = pedir_texto("Hora del turno (hh:mm): ")
        try:
            hora_turno = datetime.strptime(hora, "%H:%M").time()
            return hora_turno.strftime("%H:%M")
        except ValueError:
            print("Error: ingrese una hora valida con formato hh:mm.")


def elegir_especialidad():
    print("\nEspecialidades disponibles:")
    for indice, especialidad in enumerate(ESPECIALIDADES, start=1):
        print(f"{indice}. {especialidad}")
    opcion = pedir_entero("Seleccione una especialidad: ", 1, len(ESPECIALIDADES))
    return ESPECIALIDADES[opcion - 1]


def elegir_prioridad():
    print("\nPrioridad segun urgencia:")
    for numero, nombre in PRIORIDADES.items():
        print(f"{numero}. {nombre}")
    opcion = pedir_entero("Seleccione la prioridad: ", 1, len(PRIORIDADES))
    return opcion


def buscar_paciente(pacientes, dni):
    for paciente in pacientes:
        if paciente["dni"] == dni:
            return paciente
    return None


def registrar_paciente(pacientes):
    mostrar_titulo("Registro de paciente")
    dni = pedir_dni()

    if buscar_paciente(pacientes, dni):
        print("Ya existe un paciente registrado con ese DNI.")
        return

    nombre = pedir_texto("Nombre y apellido: ")
    edad = pedir_entero("Edad: ", 0, 120)
    telefono = pedir_texto("Telefono de contacto: ")

    paciente = {
        "dni": dni,
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono,
    }
    pacientes.append(paciente)
    print("Paciente registrado correctamente.")


def listar_pacientes(pacientes):
    mostrar_titulo("Pacientes registrados")
    if not pacientes:
        print("No hay pacientes registrados.")
        return

    for paciente in pacientes:
        print(
            f"DNI: {paciente['dni']} | "
            f"Nombre: {paciente['nombre']} | "
            f"Edad: {paciente['edad']} | "
            f"Telefono: {paciente['telefono']}"
        )


def turno_disponible(turnos, especialidad, fecha, hora):
    for turno in turnos:
        mismo_horario = (
            turno["especialidad"] == especialidad
            and turno["fecha"] == fecha
            and turno["hora"] == hora
        )
        if mismo_horario and turno["estado"] != "Cancelado":
            return False
    return True


def paciente_disponible(turnos, dni, fecha, hora):
    for turno in turnos:
        mismo_paciente = turno["dni"] == dni
        mismo_horario = turno["fecha"] == fecha and turno["hora"] == hora
        if mismo_paciente and mismo_horario and turno["estado"] != "Cancelado":
            return False
    return True


def asignar_turno(pacientes, turnos, contador_turnos):
    mostrar_titulo("Asignacion de turno")
    dni = pedir_dni()
    paciente = buscar_paciente(pacientes, dni)

    if paciente is None:
        print("No existe un paciente con ese DNI. Primero debe registrarlo.")
        return contador_turnos

    especialidad = elegir_especialidad()

    while True:
        fecha = pedir_fecha()
        hora = pedir_hora()

        if not turno_disponible(turnos, especialidad, fecha, hora):
            print("Ese horario ya esta ocupado para la especialidad seleccionada.")
            print("Ingrese otra fecha u otro horario.")
            continue

        if not paciente_disponible(turnos, paciente["dni"], fecha, hora):
            print("Ese paciente ya tiene un turno asignado en esa fecha y hora.")
            print("Ingrese otra fecha u otro horario.")
            continue

        break

    prioridad = elegir_prioridad()
    contador_turnos += 1
    turno = {
        "id": contador_turnos,
        "dni": paciente["dni"],
        "paciente": paciente["nombre"],
        "especialidad": especialidad,
        "fecha": fecha,
        "hora": hora,
        "prioridad": prioridad,
        "estado": "Pendiente",
    }
    turnos.append(turno)
    print(f"Turno asignado correctamente. Numero de turno: {turno['id']}")
    return contador_turnos


def listar_turnos(turnos):
    mostrar_titulo("Listado de turnos")
    if not turnos:
        print("No hay turnos cargados.")
        return

    for turno in turnos:
        print(
            f"Turno {turno['id']} | "
            f"{turno['fecha']} {turno['hora']} | "
            f"{turno['especialidad']} | "
            f"Paciente: {turno['paciente']} | "
            f"Prioridad: {PRIORIDADES[turno['prioridad']]} | "
            f"Estado: {turno['estado']}"
        )


def obtener_siguiente_turno(turnos):
    pendientes = [turno for turno in turnos if turno["estado"] == "Pendiente"]
    if not pendientes:
        return None
    return sorted(pendientes, key=lambda turno: (turno["prioridad"], turno["id"]))[0]


def atender_paciente(turnos):
    mostrar_titulo("Atencion de paciente")
    turno = obtener_siguiente_turno(turnos)

    if turno is None:
        print("No hay pacientes pendientes de atencion.")
        return

    turno["estado"] = "Atendido"
    print(
        f"Se atendio a {turno['paciente']} "
        f"({turno['especialidad']}, prioridad {PRIORIDADES[turno['prioridad']]})."
    )


def cancelar_turno(turnos):
    mostrar_titulo("Cancelacion de turno")
    if not turnos:
        print("No hay turnos para cancelar.")
        return

    numero_turno = pedir_entero("Ingrese el numero de turno a cancelar: ", 1)
    for turno in turnos:
        if turno["id"] == numero_turno:
            if turno["estado"] == "Atendido":
                print("No se puede cancelar un turno que ya fue atendido.")
                return
            if turno["estado"] == "Cancelado":
                print("Ese turno ya se encontraba cancelado.")
                return
            turno["estado"] = "Cancelado"
            print("Turno cancelado correctamente.")
            return

    print("No se encontro un turno con ese numero.")


def mostrar_estadisticas(pacientes, turnos):
    mostrar_titulo("Estadisticas de atencion")
    total_turnos = len(turnos)
    pendientes = 0
    atendidos = 0
    cancelados = 0
    suma_edades = 0

    for paciente in pacientes:
        suma_edades += paciente["edad"]

    for turno in turnos:
        if turno["estado"] == "Pendiente":
            pendientes += 1
        elif turno["estado"] == "Atendido":
            atendidos += 1
        elif turno["estado"] == "Cancelado":
            cancelados += 1

    promedio_edad = suma_edades / len(pacientes) if pacientes else 0

    print(f"Pacientes registrados: {len(pacientes)}")
    print(f"Turnos cargados: {total_turnos}")
    print(f"Turnos pendientes: {pendientes}")
    print(f"Pacientes atendidos: {atendidos}")
    print(f"Turnos cancelados: {cancelados}")
    print(f"Promedio de edad de pacientes: {promedio_edad:.1f}")

    print("\n" + "-" * 60)
    print("\nTurnos por especialidad:")
    for especialidad in ESPECIALIDADES:
        contador = 0
        for turno in turnos:
            if turno["especialidad"] == especialidad:
                contador += 1
        print(f"- {especialidad}: {contador}")
    print("-" * 60)
    input("\nPresione ENTER para volver al menu principal...")


def mostrar_menu():
    print("\nSistema de turnos hospitalarios")
    print("1. Registrar paciente")
    print("2. Listar pacientes")
    print("3. Asignar turno")
    print("4. Listar turnos")
    print("5. Atender siguiente paciente")
    print("6. Cancelar turno")
    print("7. Ver estadisticas")
    print("8. Salir")


def ejecutar_sistema():
    pacientes = []
    turnos = []
    contador_turnos = 0

    while True:
        mostrar_menu()
        opcion = pedir_entero("Seleccione una opcion: ", 1, 8)

        if opcion == 1:
            registrar_paciente(pacientes)
        elif opcion == 2:
            listar_pacientes(pacientes)
        elif opcion == 3:
            contador_turnos = asignar_turno(pacientes, turnos, contador_turnos)
        elif opcion == 4:
            listar_turnos(turnos)
        elif opcion == 5:
            atender_paciente(turnos)
        elif opcion == 6:
            cancelar_turno(turnos)
        elif opcion == 7:
            mostrar_estadisticas(pacientes, turnos)
        elif opcion == 8:
            print("Gracias por utilizar el sistema.")
            break


if __name__ == "__main__":
    try:
        ejecutar_sistema()
    except KeyboardInterrupt:
        print("\nPrograma finalizado por el usuario.")
