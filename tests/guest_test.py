import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("9-5", "Dolly Parton", 0)
        self.song2 = Song("Jolene", "Dolly Parton", 0)
        self.song3 = Song("Islands in the stream", "Dolly Parton", 0)
        self.song4 = Song("Two doors down", "Dolly Parton", 0)
        self.guest_jane = Guest("Jane", 100, "9-5")
        self.guest_jonny = Guest("Jonny", 100, "Jolene")
        self.guest_andy = Guest("Andy", 100, "9-5")
        self.guest_rob = Guest("Rob", 100, "Two doors down")
        self.guest_fiona = Guest("Fiona", 100, "Two doors down")
        self.room = Room("Dollywood", 1000, 0, 50)
        self.guest = Guest("Mary from Accounts", 100, "Coat of many colours")
        
    def test_guest_has_name(self):
        self.assertEqual("Fiona", self.guest_fiona.name)
    
    def test_pay_entrance_fee_check_wallet_and_till(self):
        self.guest.pay_entrance_fee_deduct_guest_wallet(self.room, self.guest_andy)
        self.assertEqual(50, self.guest_andy.wallet)

    def test_check_favourite_song(self):
        self.room.add_song_to_room(self.song1)
        self.guest.check_favourite_song(self.room, self.guest_jane)
        self.assertEqual("9-5", self.guest_jane.fav_song)
        

        
