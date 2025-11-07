"""
Módulo: servicio.py
Descripción: Define la clase Servicio que representa los servicios ofrecidos por el negocio.
             Cada servicio tiene características como duración, precio y descripción.
"""

from typing import List


class Servicio:
    """
    Clase que representa un servicio ofrecido por el negocio.
    
    Atributos:
        id (str): Identificador único del servicio
        nombre (str): Nombre del servicio
        descripcion (str): Descripción del servicio
        duracion (int): Duración del servicio en minutos
        precio (float): Precio del servicio en euros
    """
    
    contador_id = 2000
    
    def __init__(self, nombre: str, descripcion: str, duracion: int, precio: float):
        """
        Inicializa un servicio.
        
        Args:
            nombre (str): Nombre del servicio
            descripcion (str): Descripción del servicio
            duracion (int): Duración en minutos
            precio (float): Precio del servicio
        """
        self.id = f"SRV{Servicio.contador_id}"
        Servicio.contador_id += 1
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.precio = precio
    
    def mostrar_info(self) -> str:
        """
        Muestra la información del servicio.
        
        Returns:
            str: Información formateada del servicio
        """
        info = f"""
        ========== INFORMACIÓN DEL SERVICIO ==========
        ID: {self.id}
        Nombre: {self.nombre}
        Descripción: {self.descripcion}
        Duración: {self.duracion} minutos
        Precio: {self.precio}€
        ============================================
        """
        return info
    
    def calcular_costo_total(self, cantidad: int = 1) -> float:
        """
        Calcula el costo total de contrataciones múltiples del servicio.
        
        Args:
            cantidad (int): Número de contrataciones
        
        Returns:
            float: Costo total
        """
        return self.precio * cantidad
    
    def __str__(self) -> str:
        """Representación en texto del servicio."""
        return f"Servicio(ID: {self.id}, Nombre: {self.nombre}, Duración: {self.duracion}min, Precio: {self.precio}€)"
