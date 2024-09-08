# app/main.py

from datetime import datetime
from paciente import Paciente, pacientes  # Importar Paciente y la tabla de datos de pacientes
from medico import Medico, medicos  # Importar Medico y la tabla de datos de médicos
from cita import Cita  # Importar Cita
from agenda import Agenda  # Importar Agenda
from reporte import Reporte  # Importar Reporte
from notificacion import Notificacion  # Importar Notificacion

def mostrar_menu():
    print("\n=== Sistema de Gestión de Citas Médicas ===")
    print("1. Agregar Paciente")
    print("2. Registrar Médico")
    print("3. Actualizar Horario de Médico")
    print("4. Salir")
    return input("Seleccione una opción: ")

def agregar_paciente():
    print("\n--- Agregar Paciente ---")
    id_paciente = int(input("Ingrese ID del paciente: "))
    nombre_paciente = input("Ingrese nombre del paciente: ")
    correo_paciente = input("Ingrese correo del paciente: ")
    telefono_paciente = input("Ingrese teléfono del paciente: ")
    paciente = Paciente(id_paciente, nombre_paciente, correo_paciente, telefono_paciente)
    paciente.agregar_paciente()

def registrar_medico():
    print("\n--- Registrar Médico ---")
    id_medico = int(input("Ingrese ID del médico: "))
    nombre_medico = input("Ingrese nombre del médico: ")
    especialidad = input("Ingrese especialidad del médico: ")
    horario = {}  # Diccionario vacío para el horario
    medico = Medico(id_medico, nombre_medico, especialidad, horario)
    medico.agregar_medico()

def actualizar_horario_medico():
    print("\n--- Actualizar Horario de Médico ---")
    id_medico = int(input("Ingrese ID del médico para actualizar horario: "))
    nuevo_horario = {}
    while True:
        dia = input("Ingrese día de la semana (o 'fin' para terminar): ")
        if dia.lower() == 'fin':
            break
        horas = input(f"Ingrese horas disponibles para {dia} (separadas por coma): ").split(',')
        nuevo_horario[dia] = [hora.strip() for hora in horas]
    for medico in medicos:
        if medico[0] == id_medico:
            m = Medico(medico[0], medico[1], medico[2], medico[3])
            m.actualizar_horario(nuevo_horario)
            break
    else:
        print("Médico no encontrado.")

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            agregar_paciente()
        elif opcion == '2':
            registrar_medico()
        elif opcion == '3':
            actualizar_horario_medico()
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def prueba_metodos_adicionales():
    # Crear instancias de Paciente y Médico
    paciente1 = Paciente(1, "Juan Pérez", "juan.perez@gmail.com", "123456789")
    medico1 = Medico(1, "Dra. Martínez", "Cardiología", {"Lunes": ["09:00", "10:00"], "Martes": ["11:00", "12:00"]})

    # Agregar el paciente y el médico a sus respectivas tablas de datos
    paciente1.agregar_paciente()
    medico1.agregar_medico()

    # Crear instancia de Agenda
    agenda = Agenda()

    # Prueba de agendar cita
    cita = Cita(1, datetime(2024, 9, 7, 10, 0), datetime(2024, 9, 7, 10, 0), paciente1, medico1)
    agenda.agendar_cita(cita)

    # Prueba de generar reportes
    reporte = Reporte("Medicos demandados")
    print(reporte.generar_reporte_medicos_mas_demandados(agenda))
if __name__ == "__main__":
    main()
    prueba_metodos_adicionales()

