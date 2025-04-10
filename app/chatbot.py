import json
from datetime import datetime
from .processor import calculate_kpis, get_shift_data
from .utils import load_data, parse_date

class RecyclingChatbot:
    def __init__(self):
        self.data = load_data()
        
    def handle_query(self, message):
        message = message.lower()
        
        if 'volume' in message:
            return self._handle_volume_query(message)
        elif 'tempo' in message or 'horas' in message:
            return self._handle_time_query(message)
        elif 'eficiência' in message or 'produtividade' in message or 'misturados' in message:
            return self._handle_kpi_query(message)
        else:
            return "Por favor, reformule sua pergunta. Posso ajudar com:\n- Volumes processados\n- Tempos de operação\n- Indicadores de eficiência"

    def _handle_volume_query(self, message):
        date = parse_date(message)
        shift = '1' if 'turno 1' in message else '2' if 'turno 2' in message else None
        
        if date:
            daily_data = [d for d in self.data if d['date'] == date]
            if not daily_data:
                return f"Nenhum dado encontrado para {date}"
                
            if shift:
                total = sum(s['total_processed'] for s in daily_data[0]['shifts'] if s['shift'] == shift)
                return f"Volume do turno {shift} em {date}: {total} kg"
            else:
                total = sum(s['total_processed'] for s in daily_data[0]['shifts'])
                return f"Volume total em {date}: {total} kg"
        else:
            return "Por favor, especifique uma data (ex: 'volume de hoje' ou 'volume do turno 2 em 2023-10-05')"

    # Continuação com _handle_time_query e _handle_kpi_query (similar)