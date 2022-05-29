from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, this your intro page to projeto_flask!</h1>'

@app.route('/hello/<name>')
def hello_name(name):
  return 'Hello World %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
  return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
  return 'Revision Number %f' % revNo

if __name__ == '__main__':
  app.run()