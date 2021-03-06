## Яндекс-Афиша для Артема

### Описание
Данный репозиторий содержит код написанный на python3 по заданию Артема.
Задание заключалось в создании backend-кода (fronend предоставлен [Devman](https://github.com/devmanorg/where-to-go-frontend/)),
по реализации подобия Яндекс-Афиши.

Заказчик человек творческий и любознательный, побывал везде где только можно в своем родном городе (кстати, не факт...) и хочет поделиться со всеми своим опытом, а если повезёт - монетизировать проект.

Сайт представляет собой карту с указанием различных **локаций**, после выбора которой появляется подробное описание указанного места и различные рекомендации, почему это конкретное место может заинтересовать посетителя.

Для решения задачи создан Django-проект,
подготовлено API для работы с данными, оптимизированна работа панели администратора.

#### 1. Запуск локального сервера:
Скачайте [код](https://github.com/Sam1808/where-to-go/archive/master.zip),
распакуйте его в [виртуальном окружении](https://pythoner.name/documentation/tutorial/venv).
Установите пакет зависимостей:

```
pip install -r requirements.txt
```

Создайте файл переменных `.env` для `settings.py` в каталоге `where_to_go`, пример:

``` python
# where_to_go/.env

SECRET_KEY="your_key"
STATIC_URL="/static_url/"
MEDIA_ROOT="media_folder/"
MEDIA_URL="/media_url/"
DEBUG= True or False
```
*ВАЖНО: проверьте `settings.py`, данные переменные указаны со значением по умолчанию.* 

Для работы сайта нужна наполненная база данных. В текущем случае по умолчанию используется стандартная SQLite база данных (БД) `db.sqlite3`.

Примените миграции для БД:  
```
python manage.py migrate
```  
Запустите локальный сервер:  
```
python manage.py runserver
```

Сайт будет доступен по локальному адресу:  
[127.0.0.1:8000](http://127.0.0.1:8000/)

#### 2. Работа с API сайта:

По просьбе Артема реализовано API, которое представляет собой ответ на http запрос
`http://127.0.0.1:8000/places/[id локации]/`

Ответ представлен в JSON формате:

```
title:	заголовок локации
imgs:
0:	относительный пусть к файлу изображения_0
1:	относительный пусть к файлу изображения_1
...
description_short:	краткое описание
description_long:     полное описание
coordinates:
lat:	широта
lng:	долгота
```
#### 3. Работа с панелью администратора:

Для работы с администраторской панелью не забудьте создать соответвующего пользователя:  
```
python manage.py createsuperuser
```  
После создания администратора перейдите по ссылке [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) и введите пару логин/пароль.  
В администраторской панели представлено приложение `PLACES` (да, да, те самые **локации**), в котором две модели
`Image` и собственноо `Place`.

Модель `Image` довольно скушная.., позволяет добавить картинку, привязать ее к определенной локации. Дополнительные поля `Позиция` и `Описание` вряд ли будут использоваться, потому как `Позиция` доступна через основную модель `Place` (и лучше именно там ее пользовать) , а
`Описание` нигде не применяется, необязательно и вообще служит простым информационным полем для увлекательной работы контент-менеджера. Зато, мы обеспечили
контент-менеджеру личное пространство, здорово же...

Модель `Place` гораздо интереснее - это сердце сайта. Модель содержит детализированную информацию об определенной локации (локации, где *советует* побывать автор).

В первую очередь модель позволяет создать новую локацию и с помощью следующих полей дать ей подробное описание:  
 - `Название` - краткое название локации;  
 - `Короткое описание` - это первое описание локации, которое увидит посетитель сайта;
 - `Полное описание` - несложно догадаться о назначении; в поле реализован редактор текста;   
 - `Долгота` - это долгота;  
 - `Широта` - это недолгота.  
 
Дальше, тоже интересно... располагаются картинки привязанные к конкретной локации, картинку можно двигать (изменять порядок отображения), не говоря уже о добавлении и удалении. Так что,
 `CRUD` для нас не пустой звук. Все тоже самое можно делать с локацией целиком.
 Пожалуйста, не забывайте нажимать `Save` после всех изменений.

#### 4. Примеры...

На хостинге `pythonanywhere.com` развернут пример работы сайта Афиши.
Сайт доступен по адресу:
[http://sam1808.pythonanywhere.com/](http://sam1808.pythonanywhere.com/)  
Панель администратора:  
[https://sam1808.pythonanywhere.com/admin/](https://sam1808.pythonanywhere.com/admin/)  
Связка логин/пароль:  
 - `user`  
 - `super`  

Сайт абсолютно не соответвует критериям безопасности, запущен с ключами по умолчанию, служит исключительно для демонстрации возможностей и тестов.
В базу данных вручную добавлены несколько локаций, вы можете проверить работу API, например для первой локации (id=1), по ссылке:  
[https://sam1808.pythonanywhere.com/places/1/](https://sam1808.pythonanywhere.com/places/1/)

Сайт размещен под *бесплатным* аккаунтом, если сайт не доступен, то:   
- сработало ограничение бесплатного аккаунта по нагрузке (попробуйте завтра);
- хостер проводит работы (попробуйте сегодня);
- проводятся работы по обновлению сайта (попробуйте прям сейчас);
- все удалено в связи с неактуальностью (такое тоже бывает);
- поломались ресурсы, на которые ссылается сайт (будем лечить).


#### 5. Дополнительный функционал.

```
Контент-менеджеры - пчелы,  
Никогда и нипочем бы,  
Ни за что бы не подумали,  
Как же важен бедных... труд...
```
По просьбе Артема облегчаем труд контент-менеджеров, а именно - подготовлена специальная managment команда `load_place`.

Синтаксис простой:  
```
python manage.py load_place [URL на JSON-файл локации]
```  

Запускаем с консоли сервера, при этом `URL` - опция обязательная, без нее система сообщит об ошибке.

С данными [любезно делятся](https://github.com/devmanorg/where-to-go-places/tree/master/places), обратите внимание, что вам нужен чистый JSON файл, например `Антикафе Bizone.json` будет доступно по кнопке `RAW` и выглядит [вот так](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json), а команда загрузки на сервер, вот так: 
```
python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json
```

Сообщение о создание локации в консоли сервера, например,
`Created location: Смотровая площадка PANORAMA360 в ММДЦ «Москва-Сити»`
говорит о том, что локация успешно создана. В случае если такая локация уже есть, консоль и об этом скажет.

Скрипт проверяет http(s) запросы на предмет доступности. В случае недоступности данных/ошибки в запросе, скрипт сообщит причину и детали ошибки.
