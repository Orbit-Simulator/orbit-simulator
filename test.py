import servicenow_auth


gr = servicenow_auth.client.GlideRecord('u_orbit_simulator_users')
gr.query()
for user in gr:
    to_check = gr.get_value('u_id')