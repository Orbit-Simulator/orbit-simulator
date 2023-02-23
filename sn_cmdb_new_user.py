import servicenow_auth
from datetime import datetime

def create_user(user_name, passwd, email):
    gr = servicenow_auth.client.GlideRecord('u_orbit_simulator_users')
    gr.initialize()
    gr.u_user_name = user_name
    gr.u_password = passwd
    gr.u_email_address = email
    gr.u_date_created = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    gr.insert()


# create_user('TestUser', 'Password1', 'test@example.com')