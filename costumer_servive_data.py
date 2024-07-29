
service_tickets = {
    "001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


ticket_count = 2


def ticket_counter():
    global ticket_count
    ticket_count += 1
    return f"{ticket_count:03d}"


def open():
    try:
        global ticket_count
        new_ticket = input("What is the name for your new ticket? ")
        new_issue = input("What issue are you having? ")
   
        ticket_count = ticket_counter()
        service_tickets[ticket_count] = {"Customer":new_ticket,"Issue":new_issue,"Status":"open"}
   
        print(f"Your ticket has been opened successfully, your ticket number is {ticket_count}")
    except ValueError:
         print("Please use the correct input")
         
def update():
     ticket_id = input("Enter the ticket ID to update: ")
     info = service_tickets[ticket_id]["Status"]
     if ticket_id in service_tickets:
         new_status = input(f"Current status is {info} Enter the new status (open/closed): ").lower()
         if new_status in ["open", "closed"]:
                service_tickets[ticket_id]["Status"] = new_status
                print(f"Ticket {ticket_id} status updated to {new_status}.")
         else:
                print("Invalid status. Status must be 'open' or 'closed'.")
     else:
        print(f"Ticket ID {ticket_id} not found.")
       


def display():
    global ticket_count
    status =input("Which status ID's did you want to look at?(open/closed)").lower()




    if status not in ["open","closed"]:
        print("Please enter open or closed")


    for ticket_id, details in service_tickets.items():
           
            if details["Status"] == status:
               
                print(f"Ticket ID: {ticket_id}")
                print(f"  Customer: {details['Customer']}")
                print(f"  Issue: {details['Issue']}")
                print(f"  Status: {details['Status']}")
                print()


def main():
    while True:
        print("Customer Service Ticket Tracker")
        print("1. Open a new ticket")
        print("2. Update ticket status")
        print("3. Display tickets")
        print("4. Exit")
       
        choice = input("What would you like to do?(1/2/3/4): ")
        
        if choice == "1":
            open()
        if choice == "2":
            update()
        if choice == "3":
            display()
        if choice == "4":
            break
        else:
             print("Please enter a valid input(1/2/3/4)")
main()