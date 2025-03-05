from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
from flask_login import login_user, current_user, logout_user
from blog_control.user_mgnt import User

blog_abtest = Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        #print(request.args.get('user_email'))
        return redirect('/blog/test_blog')
    else:
        #print(request.form)
        user = User.create(request.form['user_email'], 'A')
        login_user(user) # 
        return redirect('/blog/test_blog')


@blog_abtest.route('/test_blog')
def test_blog():
    if current_user.is_authenticated:
        # mysql에 ID가 존재하는 경우
        return render_template('blog_A.html', user_email=current_user.user_email)
    else:
        # 세션이 없거나 세션을 갖고올 ID가 mysql에 저장이 안되어 있는 경우
        return render_template('blog_A.html')
    
@blog_abtest.route('/logout')
def logout():
    # DB에서 해당 user id 삭제
    User.delete(current_user.id)
    # 현재 세션 정보를 지움
    logout_user() 
    return redirect('/blog/test_blog')
