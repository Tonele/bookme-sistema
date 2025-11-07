"""
Módulo: cita.py
Descripción: Define la clase Cita que representa una reserva de un cliente en el sistema.
"""

from datetime import datetime, timedelta
from typing import Optional


class Cita:
    """
    Clase que representa una cita o reserva en el sistema.
    
    Atributos:
        id (str): Identificador único de la cita
        cliente: Objeto Cliente que realizó la reserva
        empleado: Objeto Empleado asignado a la cita
        servicio: Objeto Servicio contratado
        fecha_hora_inicio (str): Fecha y hora de inicio "YYYY-MM-DD HH:MM"
        fecha_hora_fin (str): Fecha y hora de fin "YYYY-MM-DD HH:MM"
        estado (str): Estado de la cita (pendiente, confirmada, cancelada, completada)
    """
    
    contador_id = 4000
    
    def __init__(self, cliente, empleado, servicio, fecha_hora_inicio: str):
        """
        Inicializa una cita.
        
        Args:
            cliente: Objeto Cliente
            empleado: Objeto Empleado
            servicio: Objeto Servicio
            fecha_hora_inicio (str): Fecha y hora de inicio "YYYY-MM-DD HH:MM"
        """
        self.id = f"CIT{Cita.contador_id}"
        Cita.contador_id += 1
        self.cliente = cliente
        self.empleado = empleado
        self.servicio = servicio
        self.fecha_hora_inicio = fecha_hora_inicio
        self.fecha_hora_fin = self._calcular_hora_fin()
        self.estado = "pendiente"
    
    def _calcular_hora_fin(self) -> str:
        """
        Calcula la hora de fin basándose en la duración del servicio.
        
        Returns:
            str: Fecha y hora de fin
        """
        try:
            fecha_inicio = datetime.strptime(self.fecha_hora_inicio, "%Y-%m-%d %H:%M")
            duracion = timedelta(minutes=self.servicio.duracion)
            fecha_fin = fecha_inicio + duracion
            return fecha_fin.strftime("%Y-%m-%d %H:%M")
        except ValueError:
            return "Fecha inválida"
    
    def confirmar(self) -> str:
        """
        Confirma la cita.
        
        Returns:
            str: Mensaje de confirmación
        """
        if self.estado == "pendiente":
            self.estado = "confirmada"
            return f"Cita {self.id} confirmada exitosamente"
        return f"No se puede confirmar una cita con estado {self.estado}"
    
    def cancelar(self, razon: str = "") -> str:
        """
        Cancela la cita.
        
        Args:
            razon (str): Razón de la cancelación
        
        Returns:
            str: Mensaje de cancelación
        """
        if self.estado != "cancelada" and self.estado != "completada":
            self.estado = "cancelada"
            msg = f"Cita {self.id} cancelada"
            if razon:
                msg += f" Razón: {razon}"
            return msg
        return f"No se puede cancelar una cita con estado {self.estado}"
    
    def marcar_completada(self) -> str:
        """
        Marca la cita como completada.
        
        Returns:
            str: Mensaje de confirmación
        """
        if self.estado == "confirmada":
            self.estado = "completada"
            return f"Cita {self.id} marcada como completada"
        return f"Solo se pueden completar citas confirmadas"
    
    def mostrar_info(self) -> str:
        """
        Muestra la información completa de la cita.
        
        Returns:
            str: Información formateada de la cita
        """
        info = f"""
        ========== INFORMACIÓN DE LA CITA ==========
        ID: {self.id}
        Cliente: {self.cliente.nombre}
        Empleado: {self.empleado.nombre}
        Servicio: {self.servicio.nombre}
        Inicio: {self.fecha_hora_inicio}
        Fin: {self.fecha_hora_fin}
        Duración: {self.servicio.duracion} minutos
        Precio: {self.servicio.precio}€
        Estado: {self.estado}
        ============================================
        """
        return info
    
    def __str__(self) -> str:
        """Representación en texto de la cita."""
        return (f"Cita(ID: {self.id}, Cliente: {self.cliente.nombre}, "
                f"Empleado: {self.empleado.nombre}, Servicio: {self.servicio.nombre}, "
                f"Estado: {self.estado})")
