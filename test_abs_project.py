


import unittest #импортируем юниттест
class TestAbs(unittest.TestCase): #создаем класс, который наследуется от от класса testCase
    def test_abs1(self): #Превратить тестовые функции в методы,
        # добавив ссылку на экземпляр класса self в качестве аргумента функции
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
 #меняем ассерты на self.assertEqual()
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

#менаяем строку запуска программы на unittest.main()
if __name__ == "__main__":
    unittest.main()

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

if __name__ == "__main__": #служит для подтверждения того,
                            # что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля
    test_abs1()
    print("All tests passed!") #В этой конструкции мы вызвали функцию test_abs1(),
                            # которая выполняет тестовый сценарий. принтом вывели что все тесты успешны


#МЫ МОЖЕМ ДОБАВИТЬ ЕЩЕ ОДИН ТЕСТ, ДОБАВИВ ЕГО КАК ФУНКЦИЮ В ЭТОМ ЖЕ ФАЙЛЕ
def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")
