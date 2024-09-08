# app/cita.py

from datetime import datetime

# Tabla de datos para almacenar las citas
citas = []

class Cita:
    """Clase que representa una cita médica."""

    def __init__(self, id_cita: int, fecha_cita: datetime, hora_cita: datetime, paciente, medico):
        self.id_cita = id_cita
        self.fecha_cita = fecha_cita
        self.hora_cita = hora_cita
        self.paciente = paciente
        self.medico = medico

    def confirmar_cita(self):
        """Confirmar una cita médica."""
        nueva_cita = [self.id_cita, self.fecha_cita, self.hora_cita, self.paciente.id_paciente, self.medico.id_medico]
        citas.append(nueva_cita)
        print(f"Cita confirmada para el paciente {self.paciente.nombre_paciente} con el médico {self.medico.nombre_medico} en {self.fecha_cita} a las {self.hora_cita}.")

    @staticmethod
    def cancelar_cita(id_cita: int):
        """Cancelar una cita médica."""
        for cita in citas:
            if cita[0] == id_cita:
                citas.remove(cita)
                print(f"Cita con ID {id_cita} cancelada exitosamente.")
                return
        print(f"No se encontró ninguna cita con el ID {id_cita}.")
