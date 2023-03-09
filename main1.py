
from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Конфигурация базы данных
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="111999qqq",
    database="mydb"
)

# Обработчик маршрута /users, который возвращает всех пользователей из базы данных
@app.route('/user', methods=['GET'])
def get_user():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    return jsonify(users)


# Обработчик маршрута /users/:id, который возвращает пользователя с указанным идентификатором
@app.route('/user/<int:iduser>', methods=['GET'])
def get_users(iduser):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM user WHERE id = %s", (iduser,))
    user = cursor.fetchone()
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'})

# Обработчик маршрута /users, который добавляет нового пользователя в базу данных
@app.route('/user', methods=['POST'])
def add_user():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO user (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    mydb.commit()
    return jsonify({'message': 'User added successfully'})

# Обработчик маршрута /users/:id, который удаляет пользователя с указанным идентификатором
@app.route('/user/<int:iduser>', methods=['DELETE'])
def delete_user(iduser):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM user WHERE id = %s", (iduser,))
    mydb.commit()
    return jsonify({'message': 'User deleted successfully'})

# Обработчик маршрута /user test, который возвращает все посты из базы данных
@app.route('/user_test', methods=['GET'])
def get_posts():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM user_test")
    user_tests = cursor.fetchall()
    return jsonify(user_tests)

@app.route('/test', methods=['GET'])
def get_posts():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM test")
    tests = cursor.fetchall()
    return jsonify(tests)

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True)