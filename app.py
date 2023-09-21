import threading 
from flask import Flask, render_template, send_file, Response, request, jsonify
import mysql.connector
from db_init import database
from bot_init import run_bot
import random
import string
import os
import time 
import string
import glob

app = Flask(__name__)

class Server(): 
    
    def __init__(self,host,port):
        self.host = host 
        self.port = port
    
    def run_server(self):
        database.db_start()
        self.bot = threading.Thread(target=run_bot)
        self.server = threading.Thread(target=app.run, kwargs={'host': self.host, 'port': self.port})
        self.server.start()
        self.bot.start()
        return self.server
    
    def check_promo_code(self, promo_code):
        self.conn = mysql.connector.connect(
            host='db',
            port=3306,
            user='root',
            password='root',
            database='promocode'
        ) 
        self.cursor = self.conn.cursor()
        promo_code = promo_code.replace(";", "")
        promo_code = promo_code.replace("sleep", "")
        query = "SELECT * FROM promocodes WHERE promocode = '" + promo_code + "'"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            if result != []:
                self.cursor.close()
                self.conn.close()
                if result:
                    discount = result[0]
                    if discount[2] != 100:
                        return f"Недостаточно средств! {result}"
                    else:
                        return 'anytime-override-object-capricorn'
            else:
                return "Некорректный промокод!"
        except:
            return 'Недостаточно средств!'
        
@app.route('/')
def get_home():
    response = Response(render_template('main.html'))
    return response
@app.route('/js/main.js')
def main_js():
    response = send_file('./js/main.js')
    return response

@app.route('/main')
def get_main():
    response = Response(render_template('main.html'))
    return response

@app.route('/1.jpg')
def get_image():
    response = send_file('images/1.jpg', mimetype='image/jpeg')
    return response

@app.route('/2.jpg')
def get_image_2():
    response = send_file('images/2.jpg', mimetype='image/jpeg')
    return response

@app.route('/3.jpg')
def get_image_3():
    response = send_file('images/3.jpg', mimetype='image/jpeg')
    return response

@app.route('/4.jpg')
def get_image_4():
    response = send_file('images/4.jpg', mimetype='image/jpeg')
    return response

@app.route('/favicon.png')
def get_favicon():
    response = send_file('images/favicon.png', mimetype='image/x-icon')
    return response

@app.route('/buy-ticket', methods=['POST'])
def buy_ticket():
    promo_code = request.json.get('promoCode')
    if promo_code:
        return server.check_promo_code(promo_code)
    return 'Промокод не указан.'

@app.route('/support')
def get_support():
    if 'cookie' not in request.cookies:
        cookie_value = generate_random_string(16)
        file_name = f"chats/{cookie_value}.txt"
        open(file_name, 'w').close() 
        response = Response(render_template('support.html'))
        response.set_cookie('cookie', cookie_value)
        return response
    elif 'cookie' in request.cookies:
        cookie_value = request.cookies.get('cookie')
        file_name = f"chats/{cookie_value}.txt"
        if not os.path.isfile(file_name):
            cookie_value = generate_random_string(16)
            file_name = f"chats/{cookie_value}.txt"
            open(file_name, 'w').close()
            response = Response(render_template('support.html'))
            response.set_cookie('cookie', cookie_value)
            return response
        else:
            response = Response(render_template('support.html'))
            return response

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return random_string

@app.route('/support-chat', methods=['POST'])
def get_support_chat():
    message_from_admin = "Мы постараемся вам ответить в ближайшее время !"
    message_from_user = str(request.json.get('text'))
    cookie = request.cookies.get('cookie')
    file_path = 'chats/'+ cookie + '.txt'
    if os.path.isfile(file_path):
        with open(file_path, 'r') as chat_file:
            lines = chat_file.readlines()
            line_count = len(lines)
            if line_count >= 20:
                lines = lines[line_count - 19:]
        
            with open(file_path, 'w') as chat_file:
                chat_file.writelines(lines)
                chat_file.write(message_from_user + '\n')
                chat_file.write(message_from_admin + '\n')
        return message_from_admin
    else:
        cookie_value = generate_random_string(16)
        file_path = f"chats/{cookie_value}.txt"
        with open(file_path, 'w') as chat_file:
            chat_file.write(message_from_user + '\n')
            chat_file.write(message_from_admin + '\n')
        response = Response()
        response.set_cookie('cookie', cookie_value)
        response.data = message_from_admin
        return response

@app.route('/chat-history')
def get_chat_history():
    history = []
    time.sleep(0.2)
    cookie = request.cookies.get('cookie')

    with open(f'chats/{cookie}.txt', 'r') as file:
        lines = file.readlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        if i % 2 == 0:
            message = {
                'sender': 'user',
                'text': line
            }
        else:
            message = {
                'sender': 'admin',
                'text': line
            }
        history.append(message)
    
    return jsonify(history)
   
@app.route('/champion_emote_unpleased_leverage')
def create_html_page():
    cookie = request.cookies.get('cookie')
    if cookie == 'bobbed-scorebook-tricycle-thickness':
        number = generate_random_string(20)
        folder_path = "templates/"

        file_list = os.listdir(folder_path)

        for file_name in file_list:
            if file_name.startswith("bot"):
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)
        directory = 'chats/'
        txt_files = glob.glob(os.path.join(directory, '*.txt'))
        
        html_content = '<html>\n\t<head>\n\t<meta charset="UTF-8" />\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n\t<title>Билеты на Маяк</title>\n\t<link rel="icon" href="favicon.png" type="image/x-icon">\n\t</head>\n\t<body>\n'
        
        for txt_file in txt_files:
            with open(txt_file, 'r') as file:
                file_content = file.read()
                html_content += f'\t<p>{file_content}</p>\n'
        
        html_content += '\t</body>\n</html>'
        
        with open(f'templates/bot{number}.html', 'w') as html_file:
            html_file.write(html_content)
        
        response = Response(render_template(f'bot{number}.html'))
        return response
    else:
        return get_home()

if __name__ == '__main__':

    server_host = '0.0.0.0'
    server_port = 5005
    
    server = Server(host=server_host, port=server_port)
    server.run_server()