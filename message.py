dfrom twilio.rest import Client 

#define ID numbers for the API 
account_sid = '<redacted>' 
auth_token = '<redacted>' 

#Initialize the client
client = Client(account_sid, auth_token) 

#function that sends the messages
# "from" is twilio's number for the whatsapp service
# "body" is the text that will be sent to everyone
# "to" is the list of numbers of all the flatmates
def send_message():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Close the window!',      
                              to=['whatsapp:<redacted>'] 
                          ) 

#for testing and demonstration
send_message()
