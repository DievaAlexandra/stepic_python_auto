#КЛЮЧЕВОЕ СЛОВО IN для поиска подстроки в каком-то тексте
#Здесь например мы задааем новую переменную туда вписываем значение строки
# и далее пишем условие, если что-то В переменной есть, то принт бла-бла если нет то вот. Сама конструкция возвращает true
# или false и от этого уже работает условие

s = 'My Name is Julia'
if 'Names' in s:
    print('Substring found')
else:
    print("no")


#ЛИБО ЧЕРЕЗ ФУНКЦИЮ FIND()
s = 'My Name is Julia'
index = s.find('Name') #инициализируем новую переменную, присваиваем ей значение функции поиска,
# функция принимает на вход как раз значение которое мы ищем
if index != -1:
    print(f'Substring found at index {index}')

#в выводе будет "Substring found at index 3" потому что он прям по символам считает, а N это как раз 3 символ (с 0 начиная)
#Пример ассерта:
#assert "login" in browser.current_url  #сообщение об ошибке


#ЗАДАНИЕ
substring = "some_value"
full_string = "fulltext"
def test_substring(full_string, substring):
    assert (substring in  full_string), f"expected '{substring}' to be substring of '{full_string}'"


