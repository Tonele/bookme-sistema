"""
Módulo: negocio.py
Descripción: Define la clase Negocio que representa el establecimiento que utiliza la aplicación.
"""

from typing import List, Optional


class Negocio:
    """
    Clase que representa un negocio/establecimiento en el sistema.
    
    Atributos:
        id (str): Identificador único del negocio
        nombre (str): Nombre del negocio
        direccion (str): Dirección del negocio
        telefono (str): Teléfono de contacto
        servicios (List): Lista de servicios disponibles
        empleados (List): Lista de empleados del negocio
        horario_general: Horario de funcionamiento general del negocio
    """
    
    contador_id = 6000
    
    def __init__(self, nombre: str, direccion: str, telefono: str):
        """
        Inicializa un negocio.
        
        Args:
            nombre (str): Nombre del negocio
            direccion (str): Dirección del negocio
            telefono (str): Teléfono de contacto
        """
        self.id = f"NEG{Negocio.contador_id}"
        Negocio.contador_id += 1
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.servicios = []
        self.empleados = []
        self.horario_general = None
    
    def agregar_servicio(self, servicio) -> str:
        """
        Agrega un nuevo servicio al negocio.
        
        Args:
            servicio: Objeto Servicio a agregar
        
        Returns:
            str: Mensaje de confirmación
        """
        self.servicios.append(servicio)
        return f"Servicio '{servicio.nombre}' agregado exitosamente"
    
    def eliminar_servicio(self, servicio_id: str) -> str:
        """
        Elimina un servicio del negocio.
        
        Args:
            servicio_id (str): ID del servicio a eliminar
        
        Returns:
            str: Mensaje de confirmación o error
        """
        for servicio in self.servicios:
            if servicio.id == servicio_id:
                self.servicios.remove(servicio)
                return f"Servicio {servicio_id} eliminado"
        return f"Servicio {servicio_id} no encontrado"
    
    def agregar_empleado(self, empleado) -> str:
        """
        Agrega un empleado al negocio.
        
        Args:
            empleado: Objeto Empleado a agregar
        
        Returns:
            str: Mensaje de confirmación
        """
        self.empleados.append(empleado)
        return f"Empleado '{empleado.nombre}' agregado exitosamente"
    
    def eliminar_empleado(self, empleado_id: str) -> str:
        """
        Elimina un empleado del negocio.
        
        Args:
            empleado_id (str): ID del empleado a eliminar
        
        Returns:
            str: Mensaje de confirmación o error
        """
        for empleado in self.empleados:
            if empleado.id == empleado_id:
                self.empleados.remove(empleado)
                return f"Empleado {empleado_id} eliminado"
        return f"Empleado {empleado_id} no encontrado"
    
    def obtener_servicios(self) -> List:
        """
        Obtiene la lista de servicios disponibles.
        
        Returns:
            List: Lista de servicios
        """
        return self.servicios
    
    def obtener_empleados(self) -> List:
        """
        Obtiene la lista de empleados.
        
        Returns:
            List: Lista de empleados
        """
        return self.empleados
    
    def obtener_informacion(self) -> str:
        """
        Obtiene la información completa del negocio.
        
        Returns:
            str: Información formateada del negocio
        """
        info = f"""
        ========== INFORMACIÓN DEL NEGOCIO ==========
        ID: {self.id}
        Nombre: {self.nombre}
        Dirección: {self.direccion}
        Teléfono: {self.telefono}
        Servicios disponibles: {len(self.servicios)}
        Empleados: {len(self.empleados)}
        ============================================
        """
        return info
    
    def listar_servicios(self) -> str:
        """
        Lista todos los servicios disponibles.
        
        Returns:
            str: Lista formateada de servicios
        """
        if not self.servicios:
            return "No hay servicios disponibles"
        
        lista = "\n========== SERVICIOS DISPONIBLES ==========\n"
        for i, servicio in enumerate(self.servicios, 1):
            lista += f"{i}. {servicio.nombre} - {servicio.precio}€ ({servicio.duracion}min)\n"
        lista += "==========================================="
        return lista
    
    def listar_empleados(self) -> str:
        """
        Lista todos los empleados del negocio.
        
        Returns:
            str: Lista formateada de empleados
        """
        if not self.empleados:
            return "No hay empleados registrados"
        
        lista = "\n========== EMPLEADOS ==========\n"
        for i, empleado in enumerate(self.empleados, 1):
            lista += f"{i}. {empleado.nombre} ({empleado.especialidad}) - {empleado.email}\n"
        lista += "=============================="
        return lista
    
    def __str__(self) -> str:
        """Representación en texto del negocio."""
        return (f"Negocio(ID: {self.id}, Nombre: {self.nombre}, "
                f"Dirección: {self.direccion}, Servicios: {len(self.servicios)}, "
                f"Empleados: {len(self.empleados)})")
