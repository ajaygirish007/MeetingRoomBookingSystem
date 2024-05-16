from datetime import datetime
from collections import defaultdict

class Room:
    def __init__(self, room_id, capacity):
        self.id = room_id
        self.capacity = capacity
        self.bookings = defaultdict(list)

    def is_available(self, date, duration):
        bookings_on_date = self.bookings[date]
        if not bookings_on_date:
            return True

        requested_start_time = date.timestamp()
        requested_end_time = requested_start_time + duration * 60

        for booking in bookings_on_date:
            existing_start_time = booking.date.timestamp()
            existing_end_time = existing_start_time + booking.duration * 60

            if (requested_start_time >= existing_start_time and requested_start_time < existing_end_time) or \
                    (requested_end_time > existing_start_time and requested_end_time <= existing_end_time) or \
                    (requested_start_time <= existing_start_time and requested_end_time >= existing_end_time):
                return False

            if (existing_start_time >= requested_start_time and existing_start_time < requested_end_time) or \
                    (existing_end_time > requested_start_time and existing_end_time <= requested_end_time) or \
                    (existing_start_time <= requested_start_time and existing_end_time >= requested_end_time):
                return False

        return True

    def add_booking(self, date, duration, user_name):
        self.bookings[date].append(Booking(date, duration, user_name))

    def get_bookings(self, date):
        return self.bookings[date]

class Booking:
    def __init__(self, date, duration, user_name):
        self.date = date
        self.duration = duration
        self.user_name = user_name

class Database:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room_id, capacity):
        self.rooms[room_id] = Room(room_id, capacity)

    def book_room(self, room_id, date, duration, user_name):
        room = self.rooms.get(room_id)
        if room is None:
            return False

        if room.is_available(date, duration):
            room.add_booking(date, duration, user_name)
            return True
        return False

    def get_bookings_for_room(self, room_id, date):
        room = self.rooms.get(room_id)
        if room:
            return room.get_bookings(date)
        return None

class MeetingRoomBookingSystem:
    def __init__(self, database):
        self.database = database

    def book_room(self, room_id, date, duration, user_name):
        booking_result = self.database.book_room(room_id, date, duration, user_name)
        if booking_result:
            print("Room booked successfully!")
        else:
            print("Booking failed. Room is not available.")
        return booking_result

    def get_bookings_for_room(self, room_id, date):
        return self.database.get_bookings_for_room(room_id, date)

if __name__ == "__main__":
    database = Database()
    database.add_room("Room1", 10)
    database.add_room("Room2", 8)

    system = MeetingRoomBookingSystem(database)

    while True:
        command = input("Enter command (book/view/exit): ")

        if command.lower() == "exit":
            break
        elif command.lower() == "book":
            room_id = input("Enter room ID: ")
            date_str = input("Enter date and time (yyyy-MM-dd HH:mm): ")
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                duration = int(input("Enter duration (in minutes): "))
                user_name = input("Enter your name: ")

                system.book_room(room_id, date, duration, user_name)
            except ValueError:
                print("Invalid input. Please try again.")
                continue
        elif command.lower() == "view":
            room_id = input("Enter room ID: ")
            date_str = input("Enter date (yyyy-MM-dd): ")
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                bookings = system.get_bookings_for_room(room_id, date)
                if bookings:
                    print(f"Bookings for {room_id} on {date}:")
                    for booking in bookings:
                        print(f"- {booking.user_name} from {booking.date} for {booking.duration} minutes")
                else:
                    print(f"No bookings found for {room_id} on {date}")
            except ValueError:
                print("Invalid input. Please try again.")
                continue
        else:
            print("Invalid command. Please try again.")

