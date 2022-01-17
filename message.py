from twilio.rest import Client 

#define ID numbers for the API 
account_sid = 'AC6ec3d570c5c56f1816fdba57143b9d78' 
auth_token = '9966883b761f16545ba548f020ce0041' 

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
                              to=['whatsapp:+32479629590', 'whatsapp:+447802443161', 'whatsapp:+32493027791', 'whatsapp:+33658318365', 'whatsapp:+447516059551', 'whatsapp:+447542504944'] 
                          ) 

#for testing and demonstration
send_message()