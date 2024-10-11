
undo_stack = []
redo_stack = []
registration_queue = []
def add_event(event):
    undo_stack.append(event) 
    print(f"Event added: {event}")
def undo():
    if undo_stack:
        event = undo_stack.pop()
        redo_stack.append(event) 
        print(f"Undid event: {event}")
    else:
        print("No events to undo.")

def redo():
    if redo_stack:
        event = redo_stack.pop()
        undo_stack.append(event) 
        print(f"Redid event: {event}")
    else:
        print("No events to redo.")
def register_attendee(attendee):
    registration_queue.append(attendee)
    print(f"Registered attendee: {attendee}")
def show_events():
    print("Available events:")
add_event("Networking Event")
add_event("Conference")
add_event("Workshop")
undo()
redo()
register_attendee("Alice")

show_events()
print(undo_stack)

