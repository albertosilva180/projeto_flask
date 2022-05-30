from flask import Flask, redirect, url_for, request

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
# aqui cai direto na página do admin
@app.route('/admin')
def hello_admin():
  return "Hello, this is your admin page!"

# aqui cai direto na pagina do guest  
@app.route('/guest/<guest>')
def hello_guest(guest):
  return 'Hello %s as Guest' % guest

#aqui checa name, caso admin -> vai para admin
# caso outro nome -> vai para guest
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
     return redirect(url_for('hello_admin'))
   else:
     return redirect(url_for('hello_guest',guest = name))
    
@app.route('/success/<name>')
def success(name):
   return 'Welcome %s, well done!' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
      
if __name__ == '__main__':
  app.run( debug = True)
