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
