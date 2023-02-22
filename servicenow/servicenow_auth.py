from pysnc import ServiceNowClient, ServiceNowOAuth2

user_name = 'admin'
passwd = 'LrmsjVJB@8^3'

client = ServiceNowClient(
    'https://dev109438.service-now.com/', (user_name, passwd))
