### Requerimientos del Sistema de Gestión de Citas Médicas

**1. Funcionalidades Principales:**
   - **Agendamiento de citas:**
     R - Los pacientes registrados deben poder agendar sus citas por sí mismos.
     R - Verificar disponibilidad de médicos según la especialidad y los horarios asignados.
     R - Mostrar en tiempo real los horarios ocupados y disponibles, incluyendo las citas agendadas y canceladas.
     R - Confirmación automática de citas a través de correo electrónico, SMS, o notificaciones de la aplicación móvil.
     R - Envío de recordatorio automático al paciente dos días antes de la cita.

   - **Cancelación de citas:**
     R - Permitir a los pacientes cancelar sus citas.
     R - Liberación inmediata de los horarios cuando una cita es cancelada.

   - **Gestión de datos:**
     R - Almacenamiento de los datos de los pacientes, incluyendo su información de contacto y citas previas.
     R - Registro de los médicos, con detalles de sus especialidades y horarios de atención.

   - **Generación de reportes:**
     R - Reporte sobre los médicos con mayor demanda y las especialidades más solicitadas.
     R - Reporte de tendencias de citas a lo largo del tiempo, identificando patrones y posibles causas de cancelaciones.
     R - Reporte de porcentaje de ausentismo y eficiencia de las consultas.
     R - Posibilidad de exportar los reportes a Excel para análisis más detallados.

**2. Requisitos No Funcionales:**
   - **Interfaz de usuario:**
     - La interfaz será de texto, suficiente para probar que los requerimientos se cumplen.
   
   - **Documentación:**
     - Crear un archivo `README.md` con el contenido estándar.
     - Crear un archivo `.gitignore` para gestionar archivos innecesarios en el repositorio de Git.
     - Crear un archivo `requirements.txt` con las dependencias necesarias para instalar con `pip`.
     - En el directorio `docs`:
       - Documento `.md` con el listado de requerimientos.
       - Archivo `.pdf` con el diagrama de clases (UML).
     - En el directorio `app`:
       - Archivo `main.py` como el punto de entrada del programa.
       - Archivos de clases y otros componentes necesarios para la solución.

**3. Reglas de Negocio:**
   - Duración estándar de una cita: **20 minutos**.
   - Confirmación de la cita al paciente **dos días antes**.
   - Si una cita es cancelada, se debe notificar a los pacientes que podrían ocupar ese horario.
   - Los datos de médicos y pacientes actualmente se almacenan en fichas físicas, lo cual deberá ser digitalizado.

**4. Restricciones:**
   - No se integrará con servicios de terceros para el envío de notificaciones (dejado "en blanco" para futura implementación).
   - Desarrollado usando **Python** en **Visual Studio Code**.
   - Código siguiendo las buenas prácticas de programación: PEP-8, documentación, y comentarios mínimos necesarios.


