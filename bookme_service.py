## Utilizaremos "" para las anotaciones por comodidad a la hora de redactar y usar párrafos.

"""
Módulo: bookme_service.py
Descripción: Clase principal que coordina la lógica general del sistema BookMe.
Gestiona usuarios, servicios, citas y notificaciones.
"""

from typing import List, Optional, Dict
from usuario import Usuario, Cliente, Empleado, Administrador
from servicio import Servicio
from cita import Cita
from notificacion import Notificacion
from negocio import Negocio


class BookMeService:
    """
    Clase principal que coordina todas las operaciones del sistema BookMe.
    
    Atributos:
        lista_usuarios (List): Lista de todos los usuarios registrados
        lista_servicios (List): Lista de todos los servicios
        lista_citas (List): Lista de todas las citas
        lista_notificaciones (List): Lista de notificaciones
        negocio (Negocio): Objeto Negocio asociado
    """
    
    def __init__(self, nombre_negocio: str, direccion: str, telefono: str):
        """
        Inicializa el servicio de BookMe.
        
        Args:
            nombre_negocio (str): Nombre del negocio
            direccion (str): Dirección del negocio
            telefono (str): Teléfono del negocio
        """
        self.lista_usuarios = []
        self.lista_servicios = []
        self.lista_citas = []
        self.lista_notificaciones = []
        self.negocio = Negocio(nombre_negocio, direccion, telefono)
    
    #  MÉTODOS DE USUARIOS
    def registrar_usuario(self, tipo_usuario: str, nombre: str, email: str, 
                         datos_adicionales: Dict = None) -> Optional[Usuario]:
        """
        Registra un nuevo usuario en el sistema.
        
        Args:
            tipo_usuario (str): Tipo de usuario ("cliente", "empleado", "administrador")
            nombre (str): Nombre del usuario
            email (str): Email del usuario
            datos_adicionales (Dict): Datos adicionales según el tipo de usuario
        
        Returns:
            Usuario: Usuario registrado o None si hay error
        """
        datos_adicionales = datos_adicionales or {}
        
        try:
            if tipo_usuario.lower() == "cliente":
                telefono = datos_adicionales.get("telefono", "")
                usuario = Cliente(nombre, email, telefono)
            elif tipo_usuario.lower() == "empleado":
                especialidad = datos_adicionales.get("especialidad", "General")
                usuario = Empleado(nombre, email, especialidad)
            elif tipo_usuario.lower() == "administrador":
                usuario = Administrador(nombre, email)
            else:
                print(f"Tipo de usuario '{tipo_usuario}' no reconocido")
                return None
            
            self.lista_usuarios.append(usuario)
            print(f"✓ Usuario '{nombre}' registrado como {tipo_usuario.lower()}")
            return usuario
        except Exception as e:
            print(f"✗ Error al registrar usuario: {e}")
            return None
    
    def obtener_usuario(self, usuario_id: str) -> Optional[Usuario]:
        """
        Obtiene un usuario por su ID.
        
        Args:
            usuario_id (str): ID del usuario
        
        Returns:
            Usuario: Usuario encontrado o None
        """
        for usuario in self.lista_usuarios:
            if usuario.id == usuario_id:
                return usuario
        return None
    
    def listar_usuarios(self) -> str:
        """
        Lista todos los usuarios registrados.
        
        Returns:
            str: Lista formateada de usuarios
        """
        if not self.lista_usuarios:
            return "No hay usuarios registrados"
        
        lista = "\n========== USUARIOS REGISTRADOS ==========\n"
        for i, usuario in enumerate(self.lista_usuarios, 1):
            lista += f"{i}. {usuario}\n"
        lista += "========================================="
        return lista
    
    # MÉTODOS DE SERVICIOS
    
    def crear_servicio(self, nombre: str, descripcion: str, 
                      duracion: int, precio: float) -> Optional[Servicio]:
        """
        Crea un nuevo servicio.
        
        Args:
            nombre (str): Nombre del servicio
            descripcion (str): Descripción del servicio
            duracion (int): Duración en minutos
            precio (float): Precio del servicio
        
        Returns:
            Servicio: Servicio creado o None si hay error
        """
        try:
            servicio = Servicio(nombre, descripcion, duracion, precio)
            self.lista_servicios.append(servicio)
            self.negocio.agregar_servicio(servicio)
            print(f"✓ Servicio '{nombre}' creado exitosamente")
            return servicio
        except Exception as e:
            print(f"✗ Error al crear servicio: {e}")
            return None
    
    def obtener_servicio(self, servicio_id: str) -> Optional[Servicio]:
        """
        Obtiene un servicio por su ID.
        
        Args:
            servicio_id (str): ID del servicio
        
        Returns:
            Servicio: Servicio encontrado o None
        """
        for servicio in self.lista_servicios:
            if servicio.id == servicio_id:
                return servicio
        return None
    
    def listar_servicios(self) -> str:
        """
        Lista todos los servicios disponibles.
        
        Returns:
            str: Lista formateada de servicios
        """
        return self.negocio.listar_servicios()
    
    def eliminar_servicio(self, servicio_id: str) -> str:
        """
        Elimina un servicio del sistema.
        
        Args:
            servicio_id (str): ID del servicio a eliminar
        
        Returns:
            str: Mensaje de confirmación o error
        """
        for servicio in self.lista_servicios:
            if servicio.id == servicio_id:
                self.lista_servicios.remove(servicio)
                self.negocio.eliminar_servicio(servicio_id)
                return f"✓ Servicio {servicio_id} eliminado"
        return f"✗ Servicio {servicio_id} no encontrado"
    
    # MÉTODOS DE CITAS
    
    def crear_cita(self, cliente_id: str, empleado_id: str, 
                   servicio_id: str, fecha_hora: str) -> Optional[Cita]:
        """
        Crea una nueva cita en el sistema.
        
        Args:
            cliente_id (str): ID del cliente
            empleado_id (str): ID del empleado
            servicio_id (str): ID del servicio
            fecha_hora (str): Fecha y hora en formato "YYYY-MM-DD HH:MM"
        
        Returns:
            Cita: Cita creada o None si hay error
        """
        try:
            cliente = self.obtener_usuario(cliente_id)
            empleado = self.obtener_usuario(empleado_id)
            servicio = self.obtener_servicio(servicio_id)
            
            if not cliente:
                print(f"✗ Cliente {cliente_id} no encontrado")
                return None
            if not empleado:
                print(f"✗ Empleado {empleado_id} no encontrado")
                return None
            if not servicio:
                print(f"✗ Servicio {servicio_id} no encontrado")
                return None
            
            cita = Cita(cliente, empleado, servicio, fecha_hora)
            cita.confirmar()
            self.lista_citas.append(cita)
            
            # Agregar a historial del cliente
            if isinstance(cliente, Cliente):
                cliente.reservar(cita)
            
            # Crear notificación
            mensaje = f"Tu cita con {empleado.nombre} para {servicio.nombre} " \
                     f"ha sido confirmada el {fecha_hora}"
            self._crear_notificacion(cliente, mensaje, "confirmacion")
            
            print(f"✓ Cita {cita.id} creada y confirmada")
            return cita
        except Exception as e:
            print(f"✗ Error al crear cita: {e}")
            return None
    
    def obtener_cita(self, cita_id: str) -> Optional[Cita]:
        """
        Obtiene una cita por su ID.
        
        Args:
            cita_id (str): ID de la cita
        
        Returns:
            Cita: Cita encontrada o None
        """
        for cita in self.lista_citas:
            if cita.id == cita_id:
                return cita
        return None
    
    def modificar_cita(self, cita_id: str, nueva_fecha_hora: str) -> Optional[Cita]:
        """
        Modifica la fecha y hora de una cita.
        
        Args:
            cita_id (str): ID de la cita
            nueva_fecha_hora (str): Nueva fecha y hora
        
        Returns:
            Cita: Cita modificada o None si hay error
        """
        cita = self.obtener_cita(cita_id)
        if cita and cita.estado == "confirmada":
            cita.fecha_hora_inicio = nueva_fecha_hora
            cita.fecha_hora_fin = cita._calcular_hora_fin()
            
            mensaje = f"Tu cita ha sido modificada a {nueva_fecha_hora}"
            self._crear_notificacion(cita.cliente, mensaje, "modificacion")
            
            print(f"✓ Cita {cita_id} modificada a {nueva_fecha_hora}")
            return cita
        
        print(f"✗ No se puede modificar la cita {cita_id}")
        return None
    
    def cancelar_cita(self, cita_id: str, razon: str = "") -> str:
        """
        Cancela una cita del sistema.
        
        Args:
            cita_id (str): ID de la cita a cancelar
            razon (str): Razón de la cancelación
        
        Returns:
            str: Mensaje de confirmación o error
        """
        cita = self.obtener_cita(cita_id)
        if cita:
            resultado = cita.cancelar(razon)
            
            mensaje = f"Tu cita ha sido cancelada. Razón: {razon}"
            self._crear_notificacion(cita.cliente, mensaje, "cancelacion")
            
            print(f"✓ {resultado}")
            return resultado
        
        print(f"✗ Cita {cita_id} no encontrada")
        return f"Cita {cita_id} no encontrada"
    
    def listar_citas_cliente(self, cliente_id: str) -> str:
        """
        Lista todas las citas de un cliente.
        
        Args:
            cliente_id (str): ID del cliente
        
        Returns:
            str: Lista formateada de citas
        """
        cliente = self.obtener_usuario(cliente_id)
        if not cliente or not isinstance(cliente, Cliente):
            return f"Cliente {cliente_id} no encontrado"
        
        citas = cliente.consultar_historial()
        if not citas:
            return f"El cliente no tiene citas reservadas"
        
        lista = f"\n========== CITAS DE {cliente.nombre.upper()} ==========\n"
        for i, cita in enumerate(citas, 1):
            lista += f"{i}. {cita}\n"
        lista += "=========================================="
        return lista
    
    def listar_todas_citas(self) -> str:
        """
        Lista todas las citas del sistema.
        
        Returns:
            str: Lista formateada de citas
        """
        if not self.lista_citas:
            return "No hay citas registradas"
        
        lista = "\n========== TODAS LAS CITAS ==========\n"
        for i, cita in enumerate(self.lista_citas, 1):
            lista += f"{i}. {cita}\n"
        lista += "===================================="
        return lista
    
    # MÉTODOS DE NOTIFICACIONES
    
    def _crear_notificacion(self, destinatario: Usuario, mensaje: str, tipo: str) -> Notificacion:
        """
        Crea una notificación en el sistema (método privado).
        
        Args:
            destinatario: Usuario destinatario
            mensaje (str): Contenido del mensaje
            tipo (str): Tipo de notificación
        
        Returns:
            Notificacion: Notificación creada
        """
        notificacion = Notificacion(destinatario, mensaje, tipo)
        self.lista_notificaciones.append(notificacion)
        return notificacion
    
    def enviar_recordatorio(self, cita_id: str) -> str:
        """
        Envía un recordatorio automático para una cita.
        
        Args:
            cita_id (str): ID de la cita
        
        Returns:
            str: Mensaje de confirmación o error
        """
        cita = self.obtener_cita(cita_id)
        if not cita:
            return f"Cita {cita_id} no encontrada"
        
        mensaje = (f"Recordatorio: Tienes una cita mañana con {cita.empleado.nombre} "
                  f"para {cita.servicio.nombre} a las {cita.fecha_hora_inicio}")
        notificacion = self._crear_notificacion(cita.cliente, mensaje, "recordatorio")
        
        return notificacion.enviar()
    
    def listar_notificaciones(self, usuario_id: str) -> str:
        """
        Lista las notificaciones de un usuario.
        
        Args:
            usuario_id (str): ID del usuario
        
        Returns:
            str: Lista formateada de notificaciones
        """
        usuario = self.obtener_usuario(usuario_id)
        if not usuario:
            return f"Usuario {usuario_id} no encontrado"
        
        notificaciones_usuario = [n for n in self.lista_notificaciones 
                                  if n.destinatario.id == usuario_id]
        
        if not notificaciones_usuario:
            return f"{usuario.nombre} no tiene notificaciones"
        
        lista = f"\n========== NOTIFICACIONES DE {usuario.nombre.upper()} ==========\n"
        for i, notif in enumerate(notificaciones_usuario, 1):
            lista += f"{i}. {notif}\n"
        lista += "=================================================="
        return lista
    
    # MÉTODOS DE ESTADÍSTICAS
    def obtener_estadisticas(self) -> str:
        """
        Obtiene un resumen de estadísticas del negocio.
        
        Returns:
            str: Estadísticas formateadas
        """
        total_clientes = len([u for u in self.lista_usuarios if isinstance(u, Cliente)])
        total_empleados = len([u for u in self.lista_usuarios if isinstance(u, Empleado)])
        total_citas = len(self.lista_citas)
        citas_confirmadas = len([c for c in self.lista_citas if c.estado == "confirmada"])
        ingresos_totales = sum([c.servicio.precio for c in self.lista_citas 
                               if c.estado == "confirmada"])
        
        stats = f"""
        ========== ESTADÍSTICAS DEL NEGOCIO ==========
        Negocio: {self.negocio.nombre}
        Total de usuarios: {len(self.lista_usuarios)}
        - Clientes: {total_clientes}
        - Empleados: {total_empleados}
        - Administradores: {len([u for u in self.lista_usuarios if isinstance(u, Administrador)])}
        
        Total de servicios: {len(self.lista_servicios)}
        Total de citas: {total_citas}
        - Confirmadas: {citas_confirmadas}
        - Canceladas: {len([c for c in self.lista_citas if c.estado == 'cancelada'])}
        - Completadas: {len([c for c in self.lista_citas if c.estado == 'completada'])}
        
        Ingresos totales: {ingresos_totales}€
        =============================================
        """
        return stats
    
    def obtener_informacion_negocio(self) -> str:
        """
        Obtiene la información del negocio.
        
        Returns:
            str: Información formateada
        """
        return self.negocio.obtener_informacion()
