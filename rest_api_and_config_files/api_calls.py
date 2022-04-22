import requests


headers = {
    'Content-type': 'text/json',
    'Accept': '*/*'
}

new_book_data = {
  "id": 1331,
  "title": "Hi",
  "description": "My name is",
  "pageCount": 13,
  "excerpt": "Test",
  "publishDate": "2022-04-20T20:08:26.362Z"
}

new_user_data = {
  "id": 28,
  "userName": "Hannah",
  "password": "123"
}

updated_book_data = {
  "id": 10,
  "title": "Updated book",
  "description": "string",
  "pageCount": 0,
  "excerpt": "string",
  "publishDate": "2022-04-20T20:46:39.926Z"
}


get_authors_list = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors')
print(f'Список всех авторов \n{get_authors_list.text}\n')

get_author_by_id = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors/4')
print(f'Автор с id = 4 \n{get_author_by_id.text}\n')

create_new_book = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Books',
                                json=new_book_data, headers=headers)
print(f'Создание книги \n{create_new_book.text}\nкод ответа {create_new_book.status_code}\n')

create_new_user = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Users',
                                json=new_user_data, headers=headers)
print(f'Создание нового юзера \n{create_new_user.text}\nкод ответа {create_new_user.status_code}\n')

update_book = requests.put('https://fakerestapi.azurewebsites.net/api/v1/Books/10',
                           json=updated_book_data, headers=headers)
print(f'Обновление книги с id = 10 \n{update_book.text}\nкод ответа {update_book.status_code}\n')

delete_user = requests.delete('https://fakerestapi.azurewebsites.net/api/v1/Users/4')
print(f'Удаление юзера с id = 4\nкод ответа {delete_user.status_code}')
