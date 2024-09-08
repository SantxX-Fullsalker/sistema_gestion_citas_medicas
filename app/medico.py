# app/medico.py

# Tabla de datos para almacenar los médicos
medicos = []

class Medico:
    """Clase que representa a un médico."""

    def __init__(self, id_medico: int, nombre_medico: str, especialidad: str, horario: dict):
        self.id_medico = id_medico
        self.nombre_medico = nombre_medico
        self.especialidad = especialidad
        self.horario = horario

    def agregar_medico(self):
        """Agregar un médico al sistema."""
        nuevo_medico = [self.id_medico, self.nombre_medico, self.especialidad, self.horario]
        medicos.append(nuevo_medico)
        print(f"Médico {self.nombre_medico} agregado exitosamente.")

    def actualizar_horario(self, nuevo_horario: dict):
        """Actualizar el horario de un médico."""
        for medico in medicos:
            if medico[0] == self.id_medico:
                medico[3] = nuevo_horario
                print(f"Horario del médico {self.nombre_medico} actualizado exitosamente.")
                break

