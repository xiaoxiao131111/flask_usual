from flask import Flask, make_response, Response, request
app = Flask(__name__)


# 状态保持
# · cookie
# · session

'''
. Cookie
特点:

将数据保存在 客户端 (用户的电脑上), 可以减轻服务器压力
访问网站时, 浏览器会 自动 将该网站的cookie数据发送给服务器
使用场景:

保存一些 不太重要的数据
'''
@app.route('/')
def index():
    # 后端设置cookie： 通过响应体的set_cookie字段

    # 创建响应对象
    response = make_response('index') # type: Response

    # 设置响应头的set_cookie字段， value必须是str/bytes类型
    response.set_cookie('per_page', '10', max_age=86400)

    # 删除cookie 本质： 设置max_age = 0
    # response.delete_cookie('per_page')

    # 返回响应对象
    return response

@app.route('/demo1')
def demo1():
    # 获取cookie： 浏览器会自动通过请求头的cookie字段来传递cookie数据

    # request.cookies 直接获取到字典形式的cookie数据
    print(request.cookies.get('per_page'))

    return 'demo1'

if __name__ == '__main__':
    app.run(debug=True)