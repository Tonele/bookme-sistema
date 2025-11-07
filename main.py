"""
Módulo: main.py
Descripción: Archivo principal que prueba todas las funcionalidades del sistema BookMe.
             Demuestra la creación de usuarios, servicios, citas y notificaciones.
"""

from bookme_service import BookMeService
from horario import Horario


def linea_separadora():
    """Imprime una línea separadora."""
    print("\n" + "="*60 + "\n")


def main():
    """Función principal que ejecuta las pruebas del sistema."""
    
    print("╔══════════════════════════════════════════════════╗")
    print("║          BIENVENIDO AL SISTEMA BOOKME            ║")
    print("║     Sistema de Gestión de Reservas y Citas       ║")
    print("╚══════════════════════════════════════════════════╝")
    
    # INICIALIZAR EL SERVICIO
    print("\n[1] INICIALIZANDO EL NEGOCIO...")
    service = BookMeService(
        nombre_negocio="BookMe Peluquería Plus",
        direccion="Calle Principal 123, Madrid",
        telefono="91-123-4567"
    )
    print("✓ Negocio inicializado correctamente")
    
    linea_separadora()
    
    #  REGISTRAR USUARIOS 
    print("[2] REGISTRANDO USUARIOS DEL SISTEMA...")
    
    # Registrar clientes
    cliente1 = service.registrar_usuario(
        tipo_usuario="cliente",
        nombre="Juan García",
        email="juan.garcia@gmail.com",
        datos_adicionales={"telefono": "600-111-111"}
    )
    
    cliente2 = service.registrar_usuario(
        tipo_usuario="cliente",
        nombre="María López",
        email="maria.lopez@gmail.com",
        datos_adicionales={"telefono": "600-222-222"}
    )
    
    cliente3 = service.registrar_usuario(
        tipo_usuario="cliente",
        nombre="Carlos Rodríguez",
        email="carlos.rodriguez@gmail.com",
        datos_adicionales={"telefono": "600-333-333"}
    )
    
    # Registrar empleados
    empleado1 = service.registrar_usuario(
        tipo_usuario="empleado",
        nombre="Antonio Recio",
        email="antonio@bookme.com",
        datos_adicionales={"especialidad": "Corte y Barba"}
    )
    
    empleado2 = service.registrar_usuario(
        tipo_usuario="empleado",
        nombre="Sandra Fernández",
        email="sandra@bookme.com",
        datos_adicionales={"especialidad": "Coloración y Tratamientos"}
    )
    
    # Registrar administrador
    admin = service.registrar_usuario(
        tipo_usuario="administrador",
        nombre="Roberto Administrador",
        email="admin@bookme.com"
    )
    
    linea_separadora()
    
    # Mostrar usuarios registrados
    print("[3] LISTADO DE USUARIOS REGISTRADOS:")
    print(service.listar_usuarios())
    
    linea_separadora()
    
    #  CREAR SERVICIOS 
    print("[4] CREANDO SERVICIOS DEL NEGOCIO...")
    
    servicio1 = service.crear_servicio(
        nombre="Corte de pelo",
        descripcion="Corte básico con máquina y tijeras",
        duracion=30,
        precio=15.00
    )
    
    servicio2 = service.crear_servicio(
        nombre="Barba Completa",
        descripcion="Afeitado y diseño de barba con navaja",
        duracion=20,
        precio=12.00
    )
    
    servicio3 = service.crear_servicio(
        nombre="Tratamiento Capilar",
        descripcion="Tratamiento profundo para el cabello",
        duracion=45,
        precio=25.00
    )
    
    servicio4 = service.crear_servicio(
        nombre="Coloración",
        descripcion="Teñido completo de cabello",
        duracion=60,
        precio=35.00
    )
    
    servicio5 = service.crear_servicio(
        nombre="Corte + Barba",
        descripcion="Corte y diseño de barba combo",
        duracion=50,
        precio=25.00
    )
    
    linea_separadora()
    
    # Mostrar servicios disponibles
    print("[5] SERVICIOS DISPONIBLES EN EL NEGOCIO:")
    print(service.listar_servicios())
    
    linea_separadora()
    
    #  CREAR HORARIOS 
    print("[6] CONFIGURANDO HORARIOS DE EMPLEADOS...")
    
    horario_empleado1 = Horario(
        dia="Lunes",
        hora_inicio="09:00",
        hora_fin="18:00",
        pausas=["13:00-14:00"]
    )
    empleado1.horario = horario_empleado1
    print(f"✓ Horario asignado a {empleado1.nombre}: {horario_empleado1}")
    
    horario_empleado2 = Horario(
        dia="Martes",
        hora_inicio="10:00",
        hora_fin="19:00",
        pausas=["13:30-14:30"]
    )
    empleado2.horario = horario_empleado2
    print(f"✓ Horario asignado a {empleado2.nombre}: {horario_empleado2}")
    
    linea_separadora()
    
    #  CREAR CITAS 
    print("[7] CREANDO CITAS EN EL SISTEMA...")
    
    # Cita 1: Cliente 1 reserva corte de cabello con empleado 1
    cita1 = service.crear_cita(
        cliente_id=cliente1.id,
        empleado_id=empleado1.id,
        servicio_id=servicio1.id,
        fecha_hora="2025-11-10 09:30"
    )
    
    # Cita 2: Cliente 2 reserva coloración con empleado 2
    cita2 = service.crear_cita(
        cliente_id=cliente2.id,
        empleado_id=empleado2.id,
        servicio_id=servicio4.id,
        fecha_hora="2025-11-11 10:00"
    )
    
    # Cita 3: Cliente 3 reserva corte + barba con empleado 1
    cita3 = service.crear_cita(
        cliente_id=cliente3.id,
        empleado_id=empleado1.id,
        servicio_id=servicio5.id,
        fecha_hora="2025-11-10 14:00"
    )
    
    # Cita 4: Cliente 1 reserva tratamiento capilar con empleado 2
    cita4 = service.crear_cita(
        cliente_id=cliente1.id,
        empleado_id=empleado2.id,
        servicio_id=servicio3.id,
        fecha_hora="2025-11-12 15:00"
    )
    
    linea_separadora()
    
    #  MOSTRAR INFORMACIÓN DE CITAS 
    print("[8] INFORMACIÓN DETALLADA DE CITAS CREADAS:")
    
    if cita1:
        print(cita1.mostrar_info())
    
    if cita2:
        print(cita2.mostrar_info())
    
    linea_separadora()
    
    #  LISTAR TODAS LAS CITAS 
    print("[9] TODAS LAS CITAS DEL SISTEMA:")
    print(service.listar_todas_citas())
    
    linea_separadora()
    
    #  HISTORIAL DE CITAS POR CLIENTE 
    print("[10] HISTORIAL DE CITAS POR CLIENTE:")
    print(service.listar_citas_cliente(cliente1.id))
    print(service.listar_citas_cliente(cliente2.id))
    
    linea_separadora()
    
    #  MODIFICAR CITA 
    print("[11] MODIFICANDO UNA CITA...")
    if cita1:
        resultado = service.modificar_cita(cita1.id, "2025-11-10 11:00")
        if resultado:
            print(f"✓ Cita modificada correctamente")
            print(resultado.mostrar_info())
    
    linea_separadora()
    
    #  ENVIAR RECORDATORIOS 
    print("[12] ENVIANDO RECORDATORIOS AUTOMÁTICOS...")
    if cita2:
        print(service.enviar_recordatorio(cita2.id))
    
    if cita3:
        print(service.enviar_recordatorio(cita3.id))
    
    linea_separadora()
    
    #  LISTAR NOTIFICACIONES 
    print("[13] NOTIFICACIONES DE CLIENTES:")
    print(service.listar_notificaciones(cliente1.id))
    print(service.listar_notificaciones(cliente2.id))
    
    linea_separadora()
    
    #  CANCELAR CITA 
    print("[14] CANCELANDO UNA CITA...")
    if cita4:
        resultado = service.cancelar_cita(
            cita4.id,
            razon="Cliente solicitó cancelación"
        )
        print(f"Resultado: {resultado}")
    
    linea_separadora()
    
    #  ESTADÍSTICAS 
    print("[15] ESTADÍSTICAS DEL NEGOCIO:")
    print(service.obtener_estadisticas())
    
    linea_separadora()
    
    #  INFORMACIÓN DEL NEGOCIO 
    print("[16] INFORMACIÓN DEL NEGOCIO:")
    print(service.obtener_informacion_negocio())
    
    linea_separadora()
    
    #  PRUEBAS ADICIONALES 
    print("[17] PRUEBAS ADICIONALES Y FUNCIONALIDADES:")
    
    # Verificar disponibilidad de horario
    print("\nVerificando disponibilidad de horarios:")
    print(f"¿Disponible a las 09:30? {horario_empleado1.disponible('09:30')}")
    print(f"¿Disponible a las 13:15 (pausa)? {horario_empleado1.disponible('13:15')}")
    print(f"¿Disponible a las 20:00 (fuera de horario)? {horario_empleado1.disponible('20:00')}")
    
    # Obtener horas disponibles
    print(f"\nHoras disponibles para {empleado1.nombre}:")
    horas_disponibles = horario_empleado1.obtener_horas_disponibles()
    print(", ".join(horas_disponibles))
    
    # Información de servicios
    print(f"\nInformación detallada del servicio:")
    print(servicio1.mostrar_info())
    
    # Calcular costo de servicios
    print(f"Costo de {servicio1.nombre}: {servicio1.calcular_costo_total(1)}€")
    print(f"Costo de 2 sesiones de {servicio3.nombre}: {servicio3.calcular_costo_total(2)}€")
    
    linea_separadora()
    
    #  RESUMEN FINAL 
    print("\n╔════════════════════════════════════════════════════════════╗")
    print("  ║              FIN DE LAS PRUEBAS DEL SISTEMA                ║")
    print("  ╚════════════════════════════════════════════════════════════╝\n")


if __name__ == "__main__":
    main()
