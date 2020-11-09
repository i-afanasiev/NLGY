from bottle import get, post, request, run 

"""
<script>alert(123);</script>
"""


def check_login(username,password):
	return True if username else False



@get('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct, {}</p>".format(username)
    else:
        return "<p>Login failed.</p>"

run(host='localhost', port=8080)