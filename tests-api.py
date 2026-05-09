from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.main import app

client = TestClient(app)

def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    print("GET / - главная страница")

def test_products_api():
    response = client.get("/api/products")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    print(f"GET /api/products - {len(data)} продуктов")

def test_stats_api():
    response = client.get("/api/stats")
    assert response.status_code == 200
    print("GET /api/stats - статистика")

if __name__ == "__main__":
    test_home_page()
    test_products_api()
    test_stats_api()
    print("\nВсе API-тесты пройдены")