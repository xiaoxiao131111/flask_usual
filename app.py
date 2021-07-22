from flask import Flask, Blueprint, url_for, make_response, request, jsonify, redirect
"""
Blueprint概念
    简单来说，Blueprint是一个存储操作方法的容器
    这些操作在这个blueprint被注册到一个应用之后就可以被调用
    Flask 可以通过blueprint来组织URL以及处理请求

flask 使用blueprint让应用实现模块化， 在flask中，blueprint具有如下属性：
    一个应用可以具有多个blueprint
    在一个应用中，一个模块可以注册多次
    blueprint 可以单独具有自己的模块、静态文件或者其它的通用操作方法
    在一个应用初始化时，就应该要注册需要使用的 blueprint
    一个 blueprint 并不是一个完整的一个应用， 他不能独立于应用运行，而必须要注册到某一个应用中
"""
# Flask对象的初始化参数 也可以 修改静态资源的存储和访问路径
app = Flask(__name__,  # 导入名称，flask 会根据该参数查询静态文件的存储路径
            # 官方建议直接使用__name__, 表示从当前目录中查询静态文件存储路径
            static_folder='static1', # 设置静态文件的存储目录
            static_url_path='/res/img'  # 设置静态文件的URL访问路径，如127.0.0.1:5000/res/img/123.jpg
            )

# Flask中 视图函数的返回值可以设置三个, 分别对应 响应体, 响应状态码, 响应头
@app.route('/demo1')
def demo1():
    # 返回值:  响应体, 响应状态码, 响应头
    return 'demo1', 400, {'A': 40}

# 视图函数返回的 str / bytes 类型数据会被包装为 Response 响应对象, 也可以 创建响应对象来 自定义响应头 等信息
# 自定义响应对象
@app.route('/demo2')
def demo2():
    # 视图函数的返回值可以为str/bytes类型, 并且flask内部会将其包装为Response响应对象
    # return 'hello flask'

    # 创建响应对象     设置响应头时,需要手动创建响应对象
    response = make_response('hello flask')  # type: Response
    # 设置响应头
    response.headers['B'] = 10
    return response

# 如果接口需要返回json数据格式， 在flask 中可以直接使用jsonify（）生成一个json的响应
# 不推荐使用 json.dumps() 直接返回， 因为返回的数据要符合HTTP 协议规范，如果是JSON需要指定 content-type：application/json
@app.route('/demo3')
def demo3():

    dict1 = {'name': 'zs', 'age': 20}
    # 字典转json字符串
    # return json.dumps(dict1)

    # 可以将字典转json字符串, 并且设置响应头的content-type为application/json
    # return jsonify(dict1)
    return jsonify(name='zs', age=20)  # 也支持关键字实参的形式

# flask中通过 redirect() 实现重定向功能
@app.route('/demo4')
def demo4():
    # 重定向到指定网站
    # return redirect('http://www.baidu.com')
    # 重定向到自己的路由   只需要URL资源段
    return redirect('/demo3')



# flask常用方法、blueprint 对象用起来和一个应用、flask对象差不多， 最大的区别就是在于一个蓝图没有办法独立运行，必须将它注册到一个应用对象上才能生效


# 1.创建一个蓝图对象
admin = Blueprint('admin', __name__)

# 2. 在这个蓝图对象上进行操作，注册路由， 指定静态文件夹， 注册模板过滤器
@admin.route('/')
def admin_home():
    return 'admin_home'

# 3. 在应用对象上注册这个蓝图对象
app.register_blueprint(admin, url_prefix='/admin')

# 蓝图对象中的参数
# 1.蓝图的url前缀：
# 当我们在应用对象上注册一个蓝图时， 可以指定一个url_prefix 关键字参数（这个参数默认是/)
# 在应用最终的路由表 url_map 中， 在蓝图上注册的路由URL 自动被加上了这个前缀，这个可以保证在多个蓝图中使动相同的URL规则
# 而不会最终引起冲突， 只要在注册蓝图时将不同的蓝图挂接到不同的子路径即可
url_for('admin.index')

# 2.注册静态路由





@app.route('/')
def index():
    return 'index'

@app.route('/list')
def list():
    return 'list'

@app.route('/detail')
def detail():
    return 'detail'

@app.route('/')
def admin_home():
    return 'admin_home'

@app.route('/new')
def new():
    return 'new'

@app.route('/edit')
def edit():
    return 'edit'

@app.route('/publish')
def publish():
    return 'publish'

if __name__=='__main__':
    app.run()