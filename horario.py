"""
Módulo: horario.py
Descripción: Define la clase Horario que gestiona la disponibilidad del negocio y empleados.
"""

from typing import List, Dict


class Horario:
    """
    Clase que representa el horario de disponibilidad de un empleado o negocio.
    
    Atributos:
        dia (str): Día de la semana
        hora_inicio (str): Hora de inicio en formato "HH:MM"
        hora_fin (str): Hora de fin en formato "HH:MM"
        pausas (List): Lista de pausas/descansos
    """
    
    contador_id = 3000
    
    def __init__(self, dia: str, hora_inicio: str, hora_fin: str, pausas: List[str] = None):
        """
        Inicializa un horario.
        
        Args:
            dia (str): Día de la semana (Lunes, Martes, etc.)
            hora_inicio (str): Hora de inicio "HH:MM"
            hora_fin (str): Hora de fin "HH:MM"
            pausas (List): Lista de pausas, ejemplo: ["12:00-13:00"]
        """
        self.id = f"HOR{Horario.contador_id}"
        Horario.contador_id += 1
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.pausas = pausas if pausas else []
    
    def disponible(self, hora_consultada: str) -> bool:
        """
        Verifica si el horario está disponible a una hora determinada.
        
        Args:
            hora_consultada (str): Hora a consultar en formato "HH:MM"
        
        Returns:
            bool: True si está disponible, False en caso contrario
        """
        # Convertir horas a minutos para facilitar la comparación
        def hora_a_minutos(hora: str) -> int:
            h, m = map(int, hora.split(':'))
            return h * 60 + m
        
        hora_consulta_min = hora_a_minutos(hora_consultada)
        inicio_min = hora_a_minutos(self.hora_inicio)
        fin_min = hora_a_minutos(self.hora_fin)
        
        # Verificar si está dentro del horario general
        if not (inicio_min <= hora_consulta_min < fin_min):
            return False
        
        # Verificar si coincide con alguna pausa
        for pausa in self.pausas:
            pausa_inicio, pausa_fin = pausa.split('-')
            pausa_inicio_min = hora_a_minutos(pausa_inicio)
            pausa_fin_min = hora_a_minutos(pausa_fin)
            if pausa_inicio_min <= hora_consulta_min < pausa_fin_min:
                return False
        
        return True
    
    def agregar_pausa(self, pausa: str) -> str:
        """
        Agrega una pausa al horario.
        
        Args:
            pausa (str): Pausa en formato "HH:MM-HH:MM"
        
        Returns:
            str: Mensaje de confirmación
        """
        self.pausas.append(pausa)
        return f"Pausa {pausa} agregada al horario"
    
    def obtener_horas_disponibles(self) -> List[str]:
        """
        Obtiene todas las horas disponibles durante el horario.
        
        Returns:
            List[str]: Lista de horas disponibles
        """
        horas_disponibles = []
        
        def hora_a_minutos(hora: str) -> int:
            h, m = map(int, hora.split(':'))
            return h * 60 + m
        
        def minutos_a_hora(minutos: int) -> str:
            h = minutos // 60
            m = minutos % 60
            return f"{h:02d}:{m:02d}"
        
        inicio_min = hora_a_minutos(self.hora_inicio)
        fin_min = hora_a_minutos(self.hora_fin)
        
        # Generar horas cada 30 minutos
        for minuto in range(inicio_min, fin_min, 30):
            hora = minutos_a_hora(minuto)
            if self.disponible(hora):
                horas_disponibles.append(hora)
        
        return horas_disponibles
    
    def __str__(self) -> str:
        """Representación en texto del horario."""
        return f"Horario(Día: {self.dia}, Inicio: {self.hora_inicio}, Fin: {self.hora_fin})"
