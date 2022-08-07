class Song:
    def __init__(self, name, artist, times_favourited):
        self.name = name
        self.artist = artist
        self.times_favourited = times_favourited

    def pay_entrance_fee_deduct_guest_wallet(self, room, guest):
        guest.wallet -= room.entrance_fee
