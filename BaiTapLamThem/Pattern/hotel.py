class HotelManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.rooms = {}
        return cls._instance

    def add_room(self, room_number, room_type, price):
        if room_number not in self.rooms:
            self.rooms[room_number] = {"type": room_type, "price": price}
            print(f"Room {room_number} added successfully.")
        else:
            print(f"Room {room_number} already exists.")

    def remove_room(self, room_number):
        if room_number in self.rooms:
            del self.rooms[room_number]
            print(f"Room {room_number} removed successfully.")
        else:
            print(f"Room {room_number} does not exist.")

    def get_room_info(self, room_number):
        if room_number in self.rooms:
            return self.rooms[room_number]
        else:
            return None

def Main():
    # Sử dụng Singleton HotelManager
    hotel_manager1 = HotelManager()
    hotel_manager1.add_room(101, "Single", 50)
    hotel_manager1.add_room(102, "Double", 80)

    hotel_manager2 = HotelManager()  # không tạo ra một instance mới, sử dụng instance đã có
    print(hotel_manager1 is hotel_manager2)  # True

    hotel_manager2.remove_room(101)

    # Kiểm tra thông tin phòng
    print(hotel_manager1.get_room_info(101))  # None
    print(hotel_manager1.get_room_info(102))  # {'type': 'Double', 'price': 80}

Main()