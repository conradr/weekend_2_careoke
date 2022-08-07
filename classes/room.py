from classes.guest import Guest
class Room:
    def __init__(self, name, till, capacity, entrance_fee):
        self.name = name
        self.songs = []
        self.till = till
        self.guests_in_room = []
        self.capacity = capacity
        self.entrance_fee = entrance_fee
        self.bar_tab = []
        self.bar_stock = []
    
    def check_in_guest(self, room, guest):
        self.add_guest_to_room(guest)
        self.add_guest_to_bar_tab(guest)
        guest.pay_entrance_fee_deduct_guest_wallet(room, guest)
        self.add_money_to_till(room)

    def add_money_to_till(self, room):
        till_total = room.till + room.entrance_fee
        room.till = till_total
        return till_total

    def return_till_total(self, room):
        return room.till
    
    def guest_count(self):
        return len(self.guests_in_room)
    
    def add_guest_to_room(self,guest_checking_in):
        if self.room_has_capacity():
            self.guests_in_room.append(guest_checking_in)

    def remove_guest_from_room(self, guest_checking_out):
        self.guests_in_room.remove(guest_checking_out)

    def add_guest_to_bar_tab(self, guest_checking_in):
        self.bar_tab.append(guest_checking_in)

    def bar_tab_count(self):
        return len(self.bar_tab)
    
    def song_count(self):
        return len(self.songs)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def room_has_capacity(self):
        if self.guest_count() < 4:
            return True
        else:
            return False


