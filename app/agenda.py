# app/agenda.py

from typing import List
from datetime import datetime
from cita import Cita, citas
from medico import Medico, medicos

class Agenda:
    """Clase que representa la agenda del sistema de gestión de citas médicas."""

    def __init__(self):
        self.citas: List[Cita] = []

    def agendar_cita(self, cita: Cita) -> bool:
        """Agenda una nueva cita médica."""
        if self._verificar_disponibilidad(cita.medico, cita.fecha_cita, cita.hora_cita):
            cita.confirmar_cita()
            self.citas.append(cita)
            return True
        else:
            print("El médico no está disponible en la fecha y hora solicitadas.")
            return False

    def cancelar_cita(self, id_cita: int) -> bool:
        """Cancela una cita existente."""
        Cita.cancelar_cita(id_cita)

    def reprogramar_cita(self, id_cita: int, nueva_fecha: datetime, nueva_hora: datetime) -> bool:
        """Reprograma una cita existente."""
        for cita in self.citas:
            if cita.id_cita == id_cita:
                if self._verificar_disponibilidad(cita.medico, nueva_fecha, nueva_hora):
                    cita.fecha_cita = nueva_fecha
                    cita.hora_cita = nueva_hora
                    print(f"Cita {id_cita} reprogramada exitosamente.")
                    return True
        print(f"No se pudo reprogramar la cita {id_cita}. Verifique los datos e intente nuevamente.")
        return False

    def reporte_citas(self) -> List[Cita]:
        """Genera un reporte básico de todas las citas."""
        return self.citas

    def _verificar_disponibilidad(self, medico: Medico, fecha: datetime, hora: datetime) -> bool:
        """Verifica la disponibilidad del médico para una fecha y hora dadas."""
        for cita in self.citas:
            if cita.medico.id_medico == medico.id_medico and cita.fecha_cita == fecha and cita.hora_cita == hora:
                return False
        return True
