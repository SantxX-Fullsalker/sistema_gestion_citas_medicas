# app/reporte.py

import pandas as pd

from agenda import Agenda
from medico import Medico, medicos

class Reporte:
    """Clase que gestiona la generación de reportes del sistema."""

    def __init__(self, tipo_reporte: str):
        self.tipo_reporte = tipo_reporte

    def disponibilidad_medicos_segun_especialidad_y_horarios(self, agenda: Agenda) -> dict:
        """Genera un reporte de disponibilidad de médicos según especialidad y horarios."""
        disponibilidad = {}
        for medico in medicos:
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

    def exportar_excel(self, reporte: dict, nombre_archivo: str) -> None:
        """Exporta el reporte seleccionado a un archivo Excel."""
        df = pd.DataFrame(list(reporte.items()), columns=['Descripción', 'Valor'])
        df.to_excel(f'{nombre_archivo}.xlsx', index=False)
        print(f"Reporte exportado exitosamente a {nombre_archivo}.xlsx")
