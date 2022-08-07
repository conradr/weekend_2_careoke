class Guest:
    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song

    def pay_entrance_fee_deduct_guest_wallet(self, room, guest):
        guest.wallet -= room.entrance_fee

    def check_favourite_song(self, room, persons_fav_song):
        for song in room.songs:
            if song.name == persons_fav_song.fav_song:
                print("I love this song!")
                return song.name
                
