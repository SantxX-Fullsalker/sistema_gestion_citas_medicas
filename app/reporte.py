# app/reporte.py

from agenda import Agenda
from medico import Medico

class Reporte:
    """Clase que gestiona la generación de reportes del sistema."""

    def __init__(self, tipo_reporte: str):
        self.tipo_reporte = tipo_reporte

    def disponibilidad_medicos_segun_especialidad_y_horarios(self, agenda: Agenda) -> dict:
        """Genera un reporte de disponibilidad de médicos según especialidad y horarios."""
        disponibilidad = {}
        for medico in agenda.medicos:
            disponibilidad[medico.nombre_medico] = medico.horario
        return disponibilidad

    def generar_reporte_medicos_mas_demandados(self, agenda: Agenda) -> dict:
        """Genera un reporte de los médicos más demandados."""
        demanda = {}
        for cita in agenda.citas:
            medico = cita.medico.nombre_medico
            demanda[medico] = demanda.get(medico, 0) + 1
        return demanda

    def generar_reporte_tendencias(self, agenda: Agenda) -> dict:
        """Genera un reporte de tendencias de citas a lo largo del tiempo."""
        tendencias = {}
        for cita in agenda.citas:
            fecha = cita.fecha_cita.date()
            tendencias[fecha] = tendencias.get(fecha, 0) + 1
        return tendencias

    def porcentaje_ausentismo_y_eficiencia_consultas(self, agenda: Agenda) -> float:
        """Calcula el porcentaje de ausentismo y eficiencia de las consultas."""
        total_citas = len(agenda.citas)
        citas_canceladas = len([c for c in agenda.citas if not c.confirmar_cita()])
        return (citas_canceladas / total_citas) * 100 if total_citas > 0 else 0

    def exportar_excel(self, datos: dict) -> None:
        """Exporta el reporte a un archivo Excel."""
        # Aquí dejamos la implementación en blanco.
        print("Exportando datos a Excel...")
