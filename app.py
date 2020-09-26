from flask import Flask, request, redirect, url_for, render_template,flash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from login_models import User, query_user
import pandas as pd

app = Flask(__name__)
app.secret_key = '1234567'

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = '请登录'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    if query_user(user_id) is not None:
        curr_user = User()
        curr_user.id = user_id
        return curr_user

@app.route('/')
@login_required
def index():
    dataciyuntudefault = pd.read_excel("./source/datadefault/词云图数据.xlsx")
    dataciyuntudefault.columns=['label','value']
    dataciyuntudefault_json = dataciyuntudefault.to_dict(orient='records')
    return render_template('tool_ciyuntu.html',wordclouddata = dataciyuntudefault_json)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('username')
        user = query_user(user_id)
        if user is not None and request.form['password'] == user['password']:

            curr_user = User()
            curr_user.id = user_id

            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user)

            return redirect(url_for('index'))

        flash('用户名或密码错误!')

    # GET 请求
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html')

@app.route('/data_get', methods=['POST'])
def data_get():
    if request.method == 'POST':
        file = request.files.get('file')
        filename = file.filename
        file.save("./source/datasave/ciyuntudata."+filename.split('.')[1])
    data_ciyuntu = pd.read_excel("./source/datasave/ciyuntudata."+filename.split('.')[1])
    data_ciyuntu.columns = ['label', 'value']
    data_ciyuntu_json = data_ciyuntu.to_dict(orient='records')
    return render_template('tool_ciyuntu.html', wordclouddata=data_ciyuntu_json)

if __name__ == '__main__':
    app.run()
