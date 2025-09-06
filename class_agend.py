from twilio.rest import Client

class sms:
    def __init__(self, person):
        self.person = person
        
    
    def alerta(self, mnsg,):
        self.mnsg = mnsg
        ##account_sid = "Your account sid"
        ##auth_token = "Your auth token"
        cliente = Client(account_sid, auth_token)
        mensagem = cliente.messages.create(
            ##from_="Your number (in twilio)",
            to= self.person,
            body=f"{self.mnsg}"
        )

        print(mensagem.body)
