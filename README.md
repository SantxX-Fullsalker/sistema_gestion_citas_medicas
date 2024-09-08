# Sistema de Gestión de Citas Médicas

Este proyecto es un sistema de gestión de citas médicas desarrollado en Python. Permite a los pacientes agendar, cancelar y reprogramar citas médicas; a los médicos administrar sus horarios; y a los administradores generar reportes sobre la disponibilidad de médicos, tendencias de citas, y la eficiencia del servicio.

## Características

- **Gestión de Pacientes:** Agregar nuevos pacientes al sistema.
- **Gestión de Médicos:** Registrar nuevos médicos y actualizar sus horarios.
- **Gestión de Citas:**
  - Agendar nuevas citas.
  - Cancelar citas existentes.
  - Reprogramar citas.
  - Ver todas las citas existentes.
- **Generación de Reportes:**
  - Disponibilidad de médicos según especialidad y horarios.
  - Médicos más demandados.
  - Tendencias de citas a lo largo del tiempo.
  - Porcentaje de ausentismo y eficiencia de consultas.
- **Notificaciones a Pacientes:** Enviar notificaciones a pacientes por correo electrónico, SMS o notificación móvil.
- **Exportación a Excel:** Exportar los reportes generados a archivos de Excel.

## Requisitos

Asegúrate de tener instalado Python 3.7 o superior. También necesitas instalar las dependencias listadas en el archivo `requirements.txt`.

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/SantxX-Fullstalker/sistema-gestion-citas-medicas.git
    cd sistema-gestion-citas-medicas
    ```

2. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar el sistema, simplemente ejecuta el archivo `main.py`:

```bash
python app/main.py



### Lista de Verificación para el Proyecto de Sistema de Gestión de Citas Médicas

#### **1. Verificación de Funcionalidad**

- [R] **Agregar Paciente:**
  - [R] Permite agregar un nuevo paciente con todos los atributos requeridos (ID, nombre, correo, teléfono).
  - [R] El paciente se almacena correctamente en la tabla de datos `pacientes`.

- [R] **Registrar Médico:**
  - [R] Permite registrar un nuevo médico con todos los atributos requeridos (ID, nombre, especialidad, horario).
  - [R] El médico se almacena correctamente en la tabla de datos `medicos`.

- [R] **Actualizar Horario de Médico:**
  - [R] Permite actualizar el horario de un médico existente.
  - [R] Los cambios en el horario se reflejan correctamente en la tabla de datos `medicos`.

- [R] **Citas:**
  - [R] **Agendar Cita:**
    - [R] Verifica la disponibilidad del médico antes de agendar la cita.
    - [R] Crea una nueva cita si el médico está disponible y la almacena correctamente.
  - [R] **Cancelar Cita:**
    - [R] Permite cancelar una cita existente y elimina la entrada de la tabla de datos `citas`.
  - [R] **Reprogramar Cita:**
    - [R] Permite reprogramar una cita existente y actualiza la información correctamente.
  - [R] **Ver Todas las Citas Existentes:**
    - [R] Muestra todas las citas registradas en el sistema.

- [R/N] **Reportes:**
  - [R] **Disponibilidad de Médicos según Especialidad y Horarios:**
    - [N] Genera el reporte de disponibilidad correctamente y lo exporta a Excel.
  - [R] **Reporte de Médicos más Demandados:**
    - [N] Genera el reporte de médicos más demandados y lo exporta a Excel.
  - [N] **Reporte de Tendencias de Citas:**
    - [N] Genera el reporte de tendencias de citas a lo largo del tiempo y lo exporta a Excel.
  - [N] **Porcentaje de Ausentismo y Eficiencia de Consultas:**
    - [N] Calcula correctamente el porcentaje de ausentismo y eficiencia.

- [R] **Notificaciones:**
  - [R] Permite enviar notificaciones por correo, SMS o móvil.
  - [R] Las notificaciones se envían correctamente con los detalles especificados.

#### **2. Verificación de Calidad del Código**

- [R] **Código Limpio y Bien Organizado:**
  - [R] Sigue las buenas prácticas de programación (PEP-8 para Python).
  - [R] Código modular y fácil de leer.
  - [R] Uso adecuado de nombres de variables y métodos descriptivos.

- [R] **Patrones de Diseño:**
  - [R] Aplicación de patrones de diseño relevantes donde se considere necesario.
  - [R] Documentación sobre las decisiones de diseño y la justificación de los patrones utilizados.

- [R] **Comentarios y Documentación:**
  - [R] Comentarios claros y útiles en partes complejas del código.
  - [R] Documentación adecuada para cada clase y método.
  - [R] Archivo `README.md` incluye descripción del proyecto, instrucciones de instalación, y uso.

#### **3. Verificación de Documentación y Entregables**

- [R] **Estructura del Proyecto:**
  - [R] Proyecto organizado según la estructura de directorios definida.
  - [R] Archivos principales (`main.py`, `paciente.py`, `medico.py`, `cita.py`, `agenda.py`, `notificacion.py`, `reporte.py`) presentes y correctamente ubicados.

- [R] **Archivos de Documentación:**
  - [R] `README.md` contiene información estándar del proyecto.
  - [R] `.gitignore` configurado correctamente para excluir archivos innecesarios del repositorio.
  - [R] `requirements.txt` contiene todas las dependencias necesarias para ejecutar el proyecto.

- [R] **Directorios de Documentación:**
  - [R] `docs` contiene un documento `.md` con el listado de requerimientos.
  - [R] `docs` contiene un archivo `.pdf` con el diagrama de clases (UML).

- [N] **Exportación de Reportes:**
  - [N] Exportación a Excel funciona correctamente para todos los reportes.
  - [N] Nombres de archivos de Excel coinciden con el tipo de reporte exportado.

#### **4. Verificación Final de Integración**

- [N] **Pruebas de Integración:**
  - [N] Todas las funcionalidades han sido probadas y verificadas.
  - [R] No hay errores de ejecución o lógica en la interfaz principal (`main.py`).
  - [N] Pruebas adicionales de casos de borde y manejo de excepciones.

