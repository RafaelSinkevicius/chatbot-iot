import pytest
from app.chatbot import RecyclingChatbot
from app.processor import calculate_kpis

@pytest.fixture
def chatbot():
    return RecyclingChatbot()

def test_volume_query(chatbot):
    response = chatbot.handle_query("Volume de hoje")
    assert "kg" in response

def test_kpi_calculation():
    test_data = {
        'correct_separations': 950,
        'total_processed': 1000,
        'operating_hours': 8,
        'mixed_materials': 50
    }
    kpis = calculate_kpis(test_data)
    assert kpis['separation_accuracy'] == 95.0