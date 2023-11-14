from flask import Flask
from flask import request
from flask import render_template
import re
from flask import redirect
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route("/")
def hello_world():
    return render_template('main.html')

@app.route('/search', methods=['POST'])
def search():
    search_result = request.form['searchResult']
    if sanitized(search_result):
        return render_template('search.html', searchResult=search_result)
    else:
        return redirect("/")
    
def sanitized(search_result):
    pattern = re.compile(r"^[a-zA-Z0-9 ]+$")
    if pattern.match(search_result):
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
