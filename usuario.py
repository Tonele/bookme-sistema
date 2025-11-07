"""
Módulo: usuario.py
Descripción: Define las clases para gestionar los diferentes tipos de usuarios del sistema.
             Incluye Usuario base, Cliente, Empleado y Administrador.
"""

from datetime import datetime
from typing import List


class Usuario:
    """
    Clase base que representa un usuario en el sistema.
    
    Atributos:
        id (str): Identificador único del usuario
        nombre (str): Nombre completo del usuario
        email (str): Correo electrónico del usuario
    """
    
    contador_id = 1000
    
    def __init__(self, nombre: str, email: str):
        """
        Inicializa un usuario.
        
        Args:
            nombre (str): Nombre del usuario
            email (str): Email del usuario
        """
        self.id = f"USR{Usuario.contador_id}"
        Usuario.contador_id += 1
        self.nombre = nombre
        self.email = email
    
    def iniciar_sesion(self) -> str:
        """Simula el inicio de sesión del usuario."""
        return f"{self.nombre} ha iniciado sesión"
    
    def cerrar_sesion(self) -> str:
        """Simula el cierre de sesión del usuario."""
        return f"{self.nombre} ha cerrado sesión"
    
    def is_admin(self) -> bool:
        """Verifica si el usuario es administrador."""
        return False
    
    def __str__(self) -> str:
        """Representación en texto del usuario."""
        return f"Usuario(ID: {self.id}, Nombre: {self.nombre}, Email: {self.email})"


class Cliente(Usuario):
    """
    Clase que representa un cliente en el sistema.
    Hereda de Usuario y añade información específica del cliente.
    
    Atributos:
        teléfono (str): Número de teléfono del cliente
        historial (List): Lista de citas realizadas por el cliente
    """
    
    def __init__(self, nombre: str, email: str, teléfono: str):
        """
        Inicializa un cliente.
        
        Args:
            nombre (str): Nombre del cliente
            email (str): Email del cliente
            teléfono (str): Número de teléfono del cliente
        """
        super().__init__(nombre, email)
        self.teléfono = teléfono
        self.historial = []
    
    def reservar(self, cita) -> str:
        """
        Realiza una reserva de cita.
        
        Args:
            cita: Objeto Cita a reservar
        
        Returns:
            str: Mensaje de confirmación
        """
        self.historial.append(cita)
        return f"Cita reservada para {self.nombre}"
    
    def consultar_historial(self) -> List:
        """
        Consulta el historial de citas del cliente.
        
        Returns:
            List: Lista de citas del cliente
        """
        return self.historial
    
    def __str__(self) -> str:
        """Representación en texto del cliente."""
        return f"Cliente(ID: {self.id}, Nombre: {self.nombre}, Email: {self.email}, Teléfono: {self.teléfono})"


class Empleado(Usuario):
    """
    Clase que representa un empleado en el sistema.
    Hereda de Usuario y añade información específica del empleado.
    
    Atributos:
        especialidad (str): Especialidad o servicio que ofrece el empleado
        horario: Objeto Horario del empleado
    """
    
    def __init__(self, nombre: str, email: str, especialidad: str):
        """
        Inicializa un empleado.
        
        Args:
            nombre (str): Nombre del empleado
            email (str): Email del empleado
            especialidad (str): Especialidad del empleado
        """
        super().__init__(nombre, email)
        self.especialidad = especialidad
        self.horario = None
    
    def ver_agenda(self, fecha: str) -> str:
        """
        Visualiza la agenda del empleado para una fecha determinada.
        
        Args:
            fecha (str): Fecha en formato "YYYY-MM-DD"
        
        Returns:
            str: Mensaje con la agenda del empleado
        """
        return f"Agenda del empleado {self.nombre} para la fecha {fecha}"
    
    def actualizar_estado_cita(self, cita, nuevo_estado: str) -> str:
        """
        Actualiza el estado de una cita.
        
        Args:
            cita: Objeto Cita
            nuevo_estado (str): Nuevo estado de la cita
        
        Returns:
            str: Mensaje de confirmación
        """
        cita.estado = nuevo_estado
        return f"Cita actualizada a estado: {nuevo_estado}"
    
    def __str__(self) -> str:
        """Representación en texto del empleado."""
        return f"Empleado(ID: {self.id}, Nombre: {self.nombre}, Email: {self.email}, Especialidad: {self.especialidad})"


class Administrador(Usuario):
    """
    Clase que representa un administrador del sistema.
    Hereda de Usuario y tiene permisos especiales.
    
    Atributos:
        permisos (List): Lista de permisos del administrador
    """
    
    def __init__(self, nombre: str, email: str):
        """
        Inicializa un administrador.
        
        Args:
            nombre (str): Nombre del administrador
            email (str): Email del administrador
        """
        super().__init__(nombre, email)
        self.permisos = ["gestionar_empleados", "gestionar_servicios", 
                        "gestionar_horarios", "consultar_estadisticas"]
    
    def is_admin(self) -> bool:
        """Verifica que el usuario es administrador."""
        return True
    
    def gestionar_empleados(self) -> str:
        """Gestiona los empleados del negocio."""
        return "Gestionando empleados del negocio"
    
    def gestionar_servicios(self) -> str:
        """Gestiona los servicios ofrecidos."""
        return "Gestionando servicios del negocio"
    
    def gestionar_horarios(self) -> str:
        """Gestiona los horarios del negocio."""
        return "Gestionando horarios del negocio"
    
    def consultar_estadisticas(self) -> str:
        """Consulta estadísticas del negocio."""
        return "Consultando estadísticas del negocio"
    
    def __str__(self) -> str:
        """Representación en texto del administrador."""
        return f"Administrador(ID: {self.id}, Nombre: {self.nombre}, Email: {self.email}, Permisos: {len(self.permisos)})"
