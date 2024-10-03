from DATABASE.Database import Database

db = Database('localhost', 'root', '', 'blog_acera')
print(db)

while True:
  print('[1] Register\n[2] Login\n[3] Logout\n[4] Create a Post\n[5] Fetch blogs\n[x] Exit ')
  choice = input()
  if choice == 'Y': break
  elif choice == '1':
    db.REGISTER(input('Name: '), input('Username: '), input('Password: '))
    
  elif choice == '2':
    has_user = db.LOGIN(input('Username: '), input('Password: '))
    if has_user: print('Login success.\n')
    else: ('Wrong username or password\n')
  elif choice == '3':
    db.LOGOUT()
  elif choice == '4':
    if db.IS_LOGIN():
      db.CREATE_BLOG(input('Post: '))
    else: print('Currently not logged in.\n')
  elif choice == '5':
    db.FETCH_BLOGS()
  elif choice == 'x': break