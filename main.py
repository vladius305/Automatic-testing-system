from flask import Flask, jsonify, request
import pymysql.cursors

app = Flask(__name__)

# Подключение к базе данных
connection = pymysql.connect(host="127.0.0.1",
                             user="root",
                             password="111999qqq",
                             db="mydb",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Метод GET для получения всех записей из таблицы users
@app.route('/users', methods=['GET'])
def get_users():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
    return jsonify(users)

# Метод GET для получения записи из таблицы users по id
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM users WHERE id=%s', (user_id,))
        user = cursor.fetchone()
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

# Метод POST для создания новой записи в таблице users
@app.route('/users', methods=['POST'])
def create_user():
    user = request.get_json()
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
                       (user['name'], user['email'], user['password']))
        connection.commit()
        user_id = cursor.lastrowid
    user['id'] = user_id
    return jsonify(user), 201

# Метод PUT для обновления записи в таблице users по id
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = request.get_json()
    with connection.cursor() as cursor:
        cursor.execute('UPDATE users SET name=%s, email=%s, password=%s WHERE id=%s',
                       (user['name'], user['email'], user['password'], user_id))
        connection.commit()
    return jsonify(user)

# Метод DELETE для удаления записи из таблицы users по id
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM users WHERE id=%s', (user_id,))
        connection.commit()
    return '', 204

# Метод GET для получения всех записей из таблицы orders
@app.route('/test', methods=['GET'])
def get_test():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM test')
        tests = cursor.fetchall()
    return jsonify(tests)

# и т.д. для остальных таблиц...

if __name__ == '__main__':
    app.run(debug=True)
