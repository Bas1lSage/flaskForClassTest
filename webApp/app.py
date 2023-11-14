from flask import Flask
from flask import request
from flask import render_template
import re
from flask import redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('main.html')

@app.route('/search', methods=['POST'])
def search():
    searchResult = request.form['searchResult']
    if sanitized(searchResult):
        return render_template('search.html', searchResult=searchResult)
    else:
        return redirect("/")
    
def sanitized(searchResult):
    pattern = re.compile(r"^[a-zA-Z0-9 ]+$")
    if pattern.match(searchResult):
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
