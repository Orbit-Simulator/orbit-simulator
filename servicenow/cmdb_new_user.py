import servicenow_auth
from datetime import datetime

gr = servicenow_auth.client.GlideRecord('u_orbit_simulator_users')
gr.initialize()
gr.u_user_name = input()
gr.password = input()
gr.u_email_address = input()
gr.u_date_created = datetime.today().strftime("%Y-%m-%d %H:%M:%S")


gr.insert()
