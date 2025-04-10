def calculate_kpis(shift_data):
    kpis = {
        'separation_accuracy': (shift_data['correct_separations'] / shift_data['total_processed']) * 100,
        'productivity': shift_data['total_processed'] / shift_data['operating_hours'],
        'mixed_materials': (shift_data['mixed_materials'] / shift_data['total_processed']) * 100
    }
    return {k: round(v, 2) for k, v in kpis.items()}

def get_shift_data(data, date, shift):
    for day in data:
        if day['date'] == date:
            for s in day['shifts']:
                if s['shift'] == shift:
                    return s
    return None