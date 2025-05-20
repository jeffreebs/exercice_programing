from datetime import datetime

def appointment_register(func):
    def information(client, service, time ):
        print (f"Appointment created : [{datetime.now()}]")
        print (f"Cliente : {client}")
        print (f"Service : {service}")
        print (f"Time: {time}")



        result= func(client,service, time)

        print(f"Appointment confirmed: {result}")
        print ( "--" *40)

        return result
    return information

@appointment_register
def booked_appointment(client, service, time):
    return f"Appointment booked for : {client} at : {time} to the service: {service}"


booked_appointment("Jeffree","Fresh hair", "3:00PM")
booked_appointment("Juan", "Beard cut", "6:00PM")
