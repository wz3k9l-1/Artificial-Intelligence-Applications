# Artificial-Intelligence-Applications
Файлы main.py, model_module.py, requirements.txt и training.py должны находиться в папке, допустим "C:\Users\[имя пользователя]\Desktop\laba6\", а файл index.html отдельно, но по той же директории, т.е "C:\Users\[имя пользователя]\Desktop\laba6\templates\"
После чего, первым делом, нужно запустить training.py (желательно через PyCharm, но для начала установить все requirements), после обучения модели появится датасет iris_model.h5 в корне проекта, также в консоли будет точность на тесте (должна быть высокой, ~0.95+). 
Далее нужно запустить приложение с помощью терминала в корне проекта (также через PyCharm), используя команду "uvicorn main:app --reload". 
После всех этих действий в терминале выведется сообщение вроде: "Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)", открываем браузер и переходим по адресу: http://127.0.0.1:8000, увидете форму для ввода параметров цветка (Sepal Length, Sepal Width, Petal Length, Petal Width), введите примерные значения, например:

Sepal Length: 5.1
Sepal Width: 3.5
Petal Length: 1.4
Petal Width: 0.2

Нажмите "Submit" — на странице появится предсказание, например: "Predicted Flower: Setosa". 
На сайте не всегда будет выводиться Setosa, для этого нужно будет вводить другие значения, примеры из датасета:
Setosa: Sepal Length: 5.1, Sepal Width: 3.5, Petal Length: 1.4, Petal Width: 0.2 → Должен быть Setosa.
Versicolor: Sepal Length: 7.0, Sepal Width: 3.2, Petal Length: 4.7, Petal Width: 1.4 → Должен быть Versicolor.
Virginica: Sepal Length: 6.3, Sepal Width: 3.3, Petal Length: 6.0, Petal Width: 2.5 → Должен быть Virginica.
