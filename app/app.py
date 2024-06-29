
from flask import Flask, render_template
import redis

app = Flask(__name__)


@app.route('/')
def index():
    # Получение значения ключа 'name' из Redis
    r = redis.Redis(host='d_redis', port=6379, db=0)
    name = r.get('name')
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
