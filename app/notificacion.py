# app/notificacion.py

class Notificacion:
    """Clase que gestiona el envío de notificaciones."""

    def __init__(self, destinatario: str, mensaje: str):
        self.destinatario = destinatario
        self.mensaje = mensaje

    def enviar_email(self) -> bool:
        """Envía una notificación por correo electrónico."""
        # Implementación para enviar notificación por correo.
        print(f"Enviando correo a {self.destinatario}: {self.mensaje}")
        return True

    def enviar_sms(self) -> bool:
        """Envía una notificación por SMS."""
        # Implementación para enviar notificación por SMS.
        print(f"Enviando SMS a {self.destinatario}: {self.mensaje}")
        return True

    def enviar_notificacion_movil(self) -> bool:
        """Envía una notificación a través de la aplicación móvil."""
        # Implementación para enviar notificación móvil.
        print(f"Enviando notificación móvil a {self.destinatario}: {self.mensaje}")
        return True
