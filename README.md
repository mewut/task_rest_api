# REST API Json Планировщик задач.

## Установка
1. Клонируйте репозиторий на свой компьютер:
   
```
git clone (https://github.com/mewut/task_rest_api.git)
```

2. Перейдите в директорию проекта:

```
cd task_auto
```

3. Установите необходимые зависимости:
   
```
pip install -r requirements.txt
```

## Запуск

1. Запустите контейнер с помощью Docker:

```
sudo docker-compose up -d
```

2. Перейдите в браузере по адресу:
 
Обновить задачу

```
http://localhost:8000/task/update 
```

   Создать задачу
   
```
http://localhost:8000/task/create 
```

   Удалить задачу
   
```
http://localhost:8000/task/destroy 
```

