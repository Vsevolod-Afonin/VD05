from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    context = {
        'blog': 'Блог про футболистов'
    }
    return render_template('hw_index.html', **context)

@app.route('/blog/')
def blog():
    context = {
        'blog': 'Блог про футболистов'
    }
    return render_template('hw_blog.html', **context)

if __name__ == '__main__':
    app.run()