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
