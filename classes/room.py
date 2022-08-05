class Room:
    def __init__(self, name, till, capacity, entrance_fee):
        self.name = name
        self.songs = []
        self.till = till
        self.guests_in_room = []
        self.capacity = capacity
        self.entrance_fee = entrance_fee
        self.bar_tab = 0
        self.bar_stock = []
    
    def add_money_to_till(self, room):
        till_total = room.till + room.entrance_fee
        room.till = till_total
        return till_total
    
    #might need to move this to the guest class
    def pay_entrance_fee_deduct_guest_wallet(self, room, guest):
        guest.wallet -= room.entrance_fee
    
    def guest_count(self):
        return len(self.guests_in_room)
    
    def add_guest_to_room(self, guest_checking_in):
        self.guests_in_room.append(guest_checking_in)

    def remove_guest_from_room(self, guest_checking_out):
        self.guests_in_room.remove(guest_checking_out)
    
    def song_count(self):
        return len(self.songs)



