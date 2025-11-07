"""
Módulo: notificacion.py
Descripción: Define la clase Notificación para gestionar recordatorios y avisos del sistema.
"""

from datetime import datetime
from typing import Optional


class Notificacion:
    """
    Clase que representa una notificación en el sistema.
    
    Atributos:
        id (str): Identificador único de la notificación
        destinatario: Usuario que recibe la notificación
        mensaje (str): Contenido del mensaje
        fecha_envio (str): Fecha y hora de envío
        tipo (str): Tipo de notificación (confirmacion, recordatorio, cancelacion)
        leida (bool): Si la notificación ha sido leída
    """
    
    contador_id = 5000
    
    def __init__(self, destinatario, mensaje: str, tipo: str = "general"):
        """
        Inicializa una notificación.
        
        Args:
            destinatario: Usuario destinatario
            mensaje (str): Contenido del mensaje
            tipo (str): Tipo de notificación
        """
        self.id = f"NOT{Notificacion.contador_id}"
        Notificacion.contador_id += 1
        self.destinatario = destinatario
        self.mensaje = mensaje
        self.fecha_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tipo = tipo
        self.leida = False
    
    def enviar(self) -> str:
        """
        Envía la notificación.
        
        Returns:
            str: Mensaje de confirmación de envío
        """
        mensaje_confirmacion = f"""
        ========== NOTIFICACIÓN ENVIADA ==========
        ID: {self.id}
        Para: {self.destinatario.nombre} ({self.destinatario.email})
        Tipo: {self.tipo}
        Fecha: {self.fecha_envio}
        Mensaje: {self.mensaje}
        ==========================================
        """
        return mensaje_confirmacion
    
    def marcar_como_leida(self) -> str:
        """
        Marca la notificación como leída.
        
        Returns:
            str: Mensaje de confirmación
        """
        self.leida = True
        return f"Notificación {self.id} marcada como leída"
    
    def obtener_estado(self) -> str:
        """
        Obtiene el estado actual de la notificación.
        
        Returns:
            str: Estado de la notificación
        """
        estado = "leída" if self.leida else "no leída"
        return f"Notificación {self.id} ({estado})"
    
    def __str__(self) -> str:
        """Representación en texto de la notificación."""
        estado = "✓ Leída" if self.leida else "✗ No leída"
        return (f"Notificación(ID: {self.id}, Para: {self.destinatario.nombre}, "
                f"Tipo: {self.tipo}, Estado: {estado})")
