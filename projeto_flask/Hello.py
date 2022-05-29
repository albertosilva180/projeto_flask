from flask import Flask, redirect, url_for

app = Flask(__name__)

# pagina inicial
@app.route('/')
def hello():
    return '<h1>Hello, this your intro page to projeto_flask!</h1>'

# uso de variável string na url
@app.route('/hello/<name>')
def hello_name(name):
  return 'Hello World %s!' % name

# uso de variável int na url
@app.route('/blog/<int:postID>')
def show_blog(postID):
  return 'Blog Number %d' % postID

# uso de variável float na url
@app.route('/rev/<float:revNo>')
def revision(revNo):
  return 'Revision Number %f' % revNo

# uso de url_for
@app.route('/admin')
def hello_admin():
  return "Hello, this is your admin page!"
  
@app.route('/guest/<guest>')
def hello_guest(guest):
  return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
     return redirect(url_for('hello_admin'))
   else:
     return redirect(url_for('hello_guest',guest = name))
      
if __name__ == '__main__':
  app.run()