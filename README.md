It is a simple webserver for adding two numbers by the user and using both GET and POST methods with these abilities:
1. using redis database as cash for some calculations.
2. using session of the web browser.
3. creating admin. 


For deploying:
  -create virtual environment 
  -Active the virtual environment and install libraries in the requirement.txt file. (pip install -r requirements.txt)
  -Convert the .env_template file to the .env file and change your database's parameters.
  -Creating admin. using these code in terminal:
    flask run shell
    from mod_users.models import User
    from app import db
    admin = User()
    admin.name = "admin"
    admin.password =User.generate_password('123')
    db.session.add(admin)
    db.session.commit()
