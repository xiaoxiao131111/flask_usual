from datetime import timedelta
from flask import Flask, session

app = Flask(__name__)
# 设置应用密钥，  会被用于session签名
app.secret_key = 'test'
# 设置session 过期时间， 默认31天
app.permanent_session_lifetime = timedelta(days=7)


'''
Session
特点:

将数据保存在 服务端 (服务器的数据库中), 安全性更高
使用场景:

保存一些 重要/敏感的数据
'''

@app.route('/')
def index():
    # session 是一个类字典对象， 对其取值、赋值， 就可以实现session数据的读写

    # 记录 session数据
    session['username'] = 'zs'

    # 设置session支持过期时间
    session.permanent = True

    # 删除session数据
    # session.pop('username')

    return 'index'

@app.route('/demo1')
def demo1():
    # 获取session数据
    name = session.get('username')
    print(name)

    return 'demo1'

if __name__ == '__main__':
    app.run(debug=True)


"""
flask的默认session机制 没有将session数据保存到服务器的数据库中, 而是将session数据编码后保存到了cookie中 (签名cookie机制)

可以使用 flask-session组件 来实现传统的session存储
"""
