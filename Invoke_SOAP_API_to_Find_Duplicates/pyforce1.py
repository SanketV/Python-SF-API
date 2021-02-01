from salesforce_api import Salesforce
client = Salesforce(username='sanket.vaidya.fsc@jackson.com.qa',
                    password='Jackson3!',
                    security_token='NhCgdAONzaxx0IiknUHKAQbx',
                    is_sandbox=True)

print(client.sobjects.query("SELECT Id, FirstName, LastName FROM Contact limit 2"))
print(client.)
