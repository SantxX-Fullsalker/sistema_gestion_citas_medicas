# app/paciente.py

from cita import Cita

# Tabla de datos para almacenar los pacientes
pacientes = []

class Paciente:
    """Clase que representa a un paciente."""

    def __init__(self, id_paciente: int, nombre_paciente: str, correo_paciente: str, telefono_paciente: str):
        self.id_paciente = id_paciente
        self.nombre_paciente = nombre_paciente
        self.correo_paciente = correo_paciente
        self.telefono_paciente = telefono_paciente

    def agregar_paciente(self):
        """Agregar un paciente al sistema."""
        nuevo_paciente = [self.id_paciente, self.nombre_paciente, self.correo_paciente, self.telefono_paciente]
        pacientes.append(nuevo_paciente)
        print(f"Paciente {self.nombre_paciente} agregado exitosamente.")

    def solicitar_cita(self, cita: Cita):
        """Solicitar una cita médica."""
        cita.confirmar_cita()

    def cancelar_cita(self, id_cita: int):
        """Cancelar una cita médica."""
        Cita.cancelar_cita(id_cita)

