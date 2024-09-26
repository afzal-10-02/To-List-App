from flask import Flask, render_template, request

app = Flask(__name__)

completed_task = ['this', 'that', 'what']

incompleted_task = ['wash the car', 'what to do', 'add new task']

@app.route('/')
def home():
    return render_template('home.html', completed_task= completed_task, incompleted_task= incompleted_task)


if __name__ == '__main__':
    app.run(debug=True)