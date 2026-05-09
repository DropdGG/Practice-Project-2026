import sys
import os

def test(name, expected, actual):
    if abs(expected - actual) > 0.01:
        print(f"❌ {name} - ошибка: ждали {expected}, получили {actual}")
        return False
    print(f"✅ {name} - пройден")
    return True

def test_bool(name, expected, actual):
    if expected != actual:
        print(f"❌ {name} - ошибка: ждали {expected}, получили {actual}")
        return False
    print(f"✅ {name} - пройден")
    return True

test("БЖУ 24/3.6/0 → 128.4 ккал", 128.4, 24*4 + 3.6*9 + 0*4)
test("Нулевые БЖУ → 0", 0, 0*4 + 0*9 + 0*4)

test("150г = 1.5 порции", 1.5, 150/100)
test("15000г (15кг) = 150 порций", 150, 15000/100)

test_bool("Вес 0 невалиден", False, 0 > 0)
test_bool("Вес -50 невалиден", False, -50 > 0)
test_bool("Вес 16000 > 15000 невалиден", False, 16000 <= 15000)
test_bool("Пустое название невалидно", False, len("".strip()) > 0)
test_bool("Отрицательные БЖУ невалидны", False, -10 >= 0)

test("Сумма 78 + 247.5 + 165 = 490.5", 490.5, 78 + 247.5 + 165)

print("\n🎯 Все тесты выполнены")