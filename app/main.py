# app/main.py

from datetime import datetime
from paciente import Paciente, pacientes  # Importar Paciente y la tabla de datos de pacientes
from medico import Medico, medicos  # Importar Medico y la tabla de datos de médicos
from cita import Cita  # Importar Cita
from agenda import Agenda  # Importar Agenda
from reporte import Reporte  # Importar Reporte
from notificacion import Notificacion  # Importar Notificacion

# Instanciar las clases necesarias
agenda = Agenda()

def mostrar_menu():
    print("\n=== Sistema de Gestión de Citas Médicas ===")
    print("1. Agregar Paciente")
    print("2. Registrar Médico")
    print("3. Actualizar Horario de Médico")
    print("4. Citas")
    print("5. Reportes")
    print("6. Notificaciones a Pacientes")
    print("7. Salir")
    return input("Seleccione una opción: ")

def menu_citas():
    print("\n=== Gestión de Citas ===")
    print("1. Agendar una nueva cita médica")
    print("2. Cancelar una cita existente")
    print("3. Reprogramar una cita existente")
    print("4. Ver todas las citas existentes")
    print("5. Volver al menú principal")
    return input("Seleccione una opción: ")

def menu_reportes():
    print("\n=== Generación de Reportes ===")
    print("1. Ver la disponibilidad de médicos según especialidad y horarios")
    print("2. Ver el reporte de los médicos más demandados")
    print("3. Ver el reporte de tendencias de citas a lo largo del tiempo")
    print("4. Calcular el porcentaje de ausentismo y eficiencia de las consultas")
    print("5. Volver al menú principal")
    return input("Seleccione una opción: ")

def menu_notificaciones():
    print("\n=== Notificaciones a Pacientes ===")
    print("1. Enviar Notificación a Paciente")
    print("2. Volver al menú principal")
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

def gestionar_citas():
    while True:
        opcion = menu_citas()
        if opcion == '1':
            # Agendar una nueva cita médica
            id_cita = int(input("Ingrese el ID de la cita: "))
            fecha_cita = datetime.strptime(input("Ingrese la fecha de la cita (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            paciente_id = int(input("Ingrese el ID del paciente: "))
            medico_id = int(input("Ingrese el ID del médico: "))
            paciente = next((p for p in pacientes if p[0] == paciente_id), None)
            medico = next((m for m in medicos if m[0] == medico_id), None)
            if paciente and medico:
                cita = Cita(id_cita, fecha_cita, fecha_cita, paciente, medico)
                agenda.agendar_cita(cita)
            else:
                print("Paciente o médico no encontrado.")
        elif opcion == '2':
            # Cancelar una cita existente
            id_cita = int(input("Ingrese el ID de la cita a cancelar: "))
            agenda.cancelar_cita(id_cita)
        elif opcion == '3':
            # Reprogramar una cita existente
            id_cita = int(input("Ingrese el ID de la cita a reprogramar: "))
            nueva_fecha = datetime.strptime(input("Ingrese la nueva fecha de la cita (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            agenda.reprogramar_cita(id_cita, nueva_fecha, nueva_fecha)
        elif opcion == '4':
            # Ver todas las citas existentes
            citas = agenda.reporte_citas()
            print("Citas existentes:")
            for cita in citas:
                print(cita)
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def generar_reportes():
    while True:
        opcion = menu_reportes()
        reporte = Reporte("Reporte")
        if opcion == '1':
            print(reporte.disponibilidad_medicos_segun_especialidad_y_horarios(agenda))
            reporte.exportar_excel(reporte.disponibilidad_medicos_segun_especialidad_y_horarios(agenda), "disponibilidad_medicos")
        elif opcion == '2':
            print(reporte.generar_reporte_medicos_mas_demandados(agenda))
            reporte.exportar_excel(reporte.generar_reporte_medicos_mas_demandados(agenda), "medicos_mas_demandados")
        elif opcion == '3':
            print(reporte.generar_reporte_tendencias(agenda))
            reporte.exportar_excel(reporte.generar_reporte_tendencias(agenda), "tendencias_citas")
        elif opcion == '4':
            print(reporte.porcentaje_ausentismo_y_eficiencia_consultas(agenda))
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def enviar_notificacion():
    destinatario = input("Ingrese el destinatario (correo o teléfono): ")
    mensaje = input("Ingrese el mensaje: ")
    notificacion = Notificacion(destinatario, mensaje)
    print("\nSeleccione el método de envío:")
    print("1. Enviar por correo")
    print("2. Enviar por SMS")
    print("3. Enviar por notificación móvil")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        notificacion.enviar_email()
    elif opcion == '2':
        notificacion.enviar_sms()
    elif opcion == '3':
        notificacion.enviar_notificacion_movil()
    else:
        print("Opción inválida.")

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
            gestionar_citas()
        elif opcion == '5':
            generar_reportes()
        elif opcion == '6':
            enviar_notificacion()
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()