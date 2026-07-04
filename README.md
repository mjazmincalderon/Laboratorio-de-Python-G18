Laboratorio de Python

Grupo: 18

Integrantes: Bentolilla Elías Ezequiel, Calderón  Macarena Jazmín, Alcorta Tomás, Binaghi Lucio Tomás, Mac Lachlan Guadalupe

Comisión: 3

Descripción General: Este proyecto consiste en un sistema de gestión de turnos hospitalarios desarrollado en Python. La aplicación permite registrar pacientes, almacenar su información personal y administrar la asignación de turnos para distintas especialidades médicas.
El sistema verifica que los datos ingresados sean válidos, evita registrar pacientes duplicados y controla que no existan conflictos de horarios al momento de asignar un turno. Además, cada turno puede clasificarse según un nivel de prioridad (alta, media o baja), lo que permite que la atención de los pacientes se realice respetando el orden de urgencia y, en caso de empate, el orden de asignación.
También es posible listar los pacientes y turnos registrados, cancelar turnos pendientes, registrar la atención de pacientes y consultar estadísticas generales, como la cantidad de turnos por especialidad, el promedio de edad de los pacientes y el estado de los turnos. Todo el sistema fue implementado mediante una estructura modular basada en funciones y utilizando listas y diccionarios para el almacenamiento de la información en memoria.

Instrucciones de uso: Al iniciar el programa se mostrará un menú con las diferentes opciones disponibles. Para utilizar correctamente el sistema se recomienda seguir el siguiente orden:
1. Registrar paciente: ingresar los datos personales del paciente. El sistema validará que el DNI no se encuentre registrado previamente.
2. Asignar turno: seleccionar un paciente registrado, elegir la especialidad médica, la fecha, el horario y el nivel de prioridad. El sistema verificará la disponibilidad del turno antes de asignarlo.
3. Listar pacientes: visualizar todos los pacientes registrados en el sistema.
4. Listar turnos: consultar los turnos asignados junto con su especialidad, prioridad y estado.
5. Atender siguiente paciente: registrar la atención del próximo paciente pendiente, respetando el orden de prioridad y de asignación.
6. Cancelar turno: cancelar un turno pendiente ingresando su número de identificación.
7. Ver estadísticas: consultar un resumen con la cantidad de pacientes registrados, turnos pendientes, atendidos, cancelados, promedio de edad y cantidad de turnos por especialidad.
8. Salir: finalizar la ejecución del programa.
