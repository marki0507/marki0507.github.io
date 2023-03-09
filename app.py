import os
import time
import web
import hashlib

web.config.debug = False

URLS = (
 '/', 'times',
 '/index', 'dex',
 '/sales', 'sales',
 '/purchase', 'purchase',
 '/accounting', 'accounting',
 '/login', 'login',
 '/logout', 'logout',
 '/home', 'home',
  '/learn/get', 'learn_get',
 '/learn/post', 'learn_post',
 '/hello', 'hello',
'/waktu', 'index',
 '/hello/world', 'hello_world',
)

app = web.application(URLS, globals())
application = app.wsgifunc()

def test_func():
 return 'ini fungsi yang tersedia untuk template'

template_keren = {
 'test_func': test_func
}

curdir = os.path.dirname(__file__)
template = os.path.join(curdir, 'template')
raider = web.template.render(template, globals=template_keren)

#SOAL PERTAMA
class index:
    def GET(self):
       local_time = time.localtime()
       time1 = time.gmtime(time.mktime(local_time))
       formatted_time = time.strftime('%A, %Y-%m-%d %H:%M:%S',time1)
       time2 = time.gmtime(time.mktime(local_time)+25200)
       ttime = time.strftime('%A, %Y-%m-%d %H:%M:%S', time2)
       
       
       data = {
       'a': formatted_time,
       'b': ttime,
       }
       
       return raider.index(data)

# SOAL KEDUA
class learn_get:
 def GET(self):
     inp = web.input(name=None, status=None, age=None)
     name = inp.get('name')
     status = inp.get('status')
     age = inp.get('age')

     # Validasi input
     if not name:
         raise web.badrequest("Masukkan nama")
    #  elif not name:
    #      raise web.badrequest("Masukkan Nama")
     elif not status:
         raise web.badrequest("Masukkan Status")
     elif not age:
         raise web.badrequest("Masukkan Umur yang harus lebih dari 0 dan kurang dari 200")

     # Validasi umur
     try:
         age = int(age)
         if age <= 0 or age >=200:
             raise ValueError
     except ValueError:
         raise web.badrequest("Umur harus lebih dari nol dan dibawah 200")
     
     data = {
        'a':name,
        'b':status,
        'c':age,
    }
     return raider.get(data)

class learn_post:
 def GET(self):
     data ={
        'a':learn_post,
     }
     return raider.learn(data)
 
 def POST(self):
    inp = web.input(name='', status='', age=0)
    name = inp.name.strip()
    status = inp.status.strip()
    age = inp.age

    # validate inputs
    if not name:
        return "Nama Harus Diisi"
    if not status or status == 'Pilih Status':
        return "Pilih Status A atau B"
    if not age or int(age) <= 0 or int(age) >=200:
        return "Umur harus diisi dan harus lebih dari 0 dan kurang dari 200"

    redirect_url = '/hello?name={}&status={}&age={}'.format(name, status, age)
    web.seeother(redirect_url)

class hello:
    def GET(self):
        name = web.input().get('name')
        status = web.input().get('status')
        age = web.input().get('age')

        data = {
           'a': name,
           'b': status,
           'c': age,
        }
        return raider.hello(data)

# SOAL KEEMPAT
class hello_world:
 def GET(self):
  data = {
   'a': 'ini adalah contoh string yang dilewatkan ke template',
   'b': [1,2,3],
   'c': '<b>Kode HTML</b>',
   'd': 'HELLO',
   'e': 'WORLD',
   }
  return raider.hello_world(data)


# SOAL KELIMA dan KEENAM
db = web.database(dbn='postgres',db='muhikram',user='muhikram', password='glccikram05')
sess = web.session.Session(app, web.session.DBStore(db, 'sessions'),
                           initializer={'user': ''}
                          )

def app_menu():
 return [
  ['times', 'Time', '/'],
  ['sales', 'Sales Order', '/sales'],
  ['purchase', 'Purchase Order', '/purchase'],
  ['accounting', 'Accounting', '/accounting'],
  ['home', 'Home', '/home'],
  ['login', 'Login', '/login'],
  ['logout', 'Logout', '/logout'],
  ]

template_globals = {
 'app_menu': app_menu,
 }


curdir = os.path.dirname(__file__)
template = os.path.join(curdir, 'template')
render = web.template.render(template, base='layout', globals=template_globals)

class times:
    def GET(self):
       
       local_time = time.localtime() #waktu local saat ini 
       time2 = time.strftime('%A, %Y-%m-%d %H:%M:%S', local_time)
       
       data = {
        'title': 'Time',
        'menu': 'time',
        'a': time2,
       }
       
       return render.time(data)

class dex:
  def GET(self):
   raise web.seeother('/sales')
  
  
class sales:
  def GET(self):
   data = {
    'title': 'Sales Order',
    'menu': 'sales',
    }
   sales = '<h3>ini adalah isi database sales</h3>'
   records = list(db.query('select * from sales order by sales_id asc'))
   return render.sales(data, sales, records)
  #  return render.sales(data)
  

class purchase:
 def GET(self):
  data = {
   'title': 'Purchase Order',
   'menu': 'purchase',
   }
  purchase = '<h3>ini adalah isi database purchase</h3>'
  records = list(db.query('select * from purchase order by purchase_id asc'))
  return render.purchase(data, purchase, records)
  # return render.purchase(data)
 
 
class accounting:
 def GET(self):
  data = {
   'title': 'Accounting',
   'menu': 'accounting',
   }
  accounting = '<h3>ini adalah isi database accounting</h3>'
  records = list(db.query('select * from accounting order by accounting_id asc'))
  return render.accounting(data, accounting, records)
  # return render.accounting(data)


# SOAL KETIGA dan PROJECT
class login:
    def GET(self):
        # web.header('Content-Type', 'text/html')
        data = {
           'title': 'Login',
           'menu': 'login',
           }
        if sess.user:
            raise web.seeother('/home')
        return render.login(data)

    def POST(self):
        inp = web.input(name='', password='')
        name = inp.name.strip()
        password = inp.password.strip()
        
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        login = db.query("SELECT name, passwd FROM accounts WHERE name=$name AND passwd=$passwd", vars={'name': name, 'passwd':hashed_password})

        if not name:
            return 'Masukkan Nama'
        elif not password:
            return 'Masukkan Password'
        elif login:
            sess.user = name
            raise web.seeother('/home')
        else:
            return "Username atau Password yang dimasukkan salah"
    
class home:
    def GET(self):
        data = {
           'title': 'Home',
           'menu': 'home',
           'a':sess.user,
           }

        if not sess.user:
            raise web.seeother('/login')
        else:
            # return 'Hello ( %s )' %(sess.user)
            return render.home(data)

class logout:
    def GET(self):
        sess.kill()
        raise web.seeother('/login')


 

if __name__ == '__main__':
 app.run()
