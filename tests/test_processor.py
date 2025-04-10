from app.processor import calculate_kpis, get_shift_data

def test_mixed_materials_percentage():
    test_shift = {
        'total_processed': 2000,
        'mixed_materials': 150
    }
    kpis = calculate_kpis(test_shift)
    assert kpis['mixed_materials'] == 7.5

def test_productivity_calculation():
    test_data = {
        'total_processed': 1600,
        'operating_hours': 8
    }
    kpis = calculate_kpis(test_data)
    assert kpis['productivity'] == 200