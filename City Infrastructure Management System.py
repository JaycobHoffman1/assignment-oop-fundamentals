# Task 1: Vehicle Registration System

print("Task 1: Vehicle Registration System")

class Vehicle:
    def __init__(self, registration_number, type, owner):
        self.reg_num = registration_number
        self.type = type
        self.owner = owner
    
    def update_owner(self):
        while True:
            new_owner = input("Enter new owner name: ")

            try:
                if (not new_owner) or len(new_owner) == new_owner.count(" "):
                    raise ValueError("Owner name cannot be blank.")
            except ValueError as v:
                print(v)
            else:
                break
        
        self.owner = new_owner

def process_owner(vehicle, vehicle_name):
    print(f"\n{vehicle_name} owner: {vehicle.owner}")
    vehicle.update_owner()
    print(f"New {vehicle_name} owner: {vehicle.owner}")

toyota_supra = Vehicle("ABC-123", "coupe", "Johnny") # Original owner is "Johnny"
honda_odyssey = Vehicle("DEF-456", "minivan", "Gina") # Original owner is "Gina"
nissan_leaf = Vehicle("GHI-789", "EV", "David") # Original owner is "David"

process_owner(toyota_supra, "Toyota Supra")
process_owner(honda_odyssey, "Honda Odyssey")
process_owner(nissan_leaf, "Nissan Leaf")

# Task 2: Event Management System Enhancement

print("\nTask 2: Event Management System Enhancement")

class Event:
    def __init__(self, name, date, participants = 0):
        self.name = name
        self.date = date
        self.participants = participants

    def add_participant(self):
        self.participants += 1

        print("Participant added!")

    def get_participant_count(self):
        print(f"The current number of participants is: {self.participants}")

def process_participants(event):
    print(f"\n{event.name}:")
    event.get_participant_count()
    event.add_participant()
    event.get_participant_count()

conference = Event("Tech Conference", "2024-07-14") # 0 participants
summit = Event("Tech Summit", "2024-07-15", 100) # 100 participants

process_participants(conference)
process_participants(summit)