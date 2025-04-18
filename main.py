from flask import Flask, session, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/folder', methods=['GET', 'POST'])
def folder():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''

    <form action = "" method = "post">
        <p><input type = text name = username></p>
        <p><input type = submit value = Login></p>
    </form>

    '''

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)