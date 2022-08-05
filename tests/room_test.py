import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    
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
        self.room = Room("Dollywood", 1000, 4, 50)
    
    def test_room_has_name(self):
        self.assertEqual("Dollywood", self.room.name)
    
    def test_room__has_till(self):
        self.assertEqual(1000, self.room.till)
    
    def test_add_money_to_till(self):
        till_total = self.room.add_money_to_till(self.room)
        self.assertEqual(1050, till_total)

    def test_pay_entrance_fee_check_wallet_and_till(self):
        self.room.pay_entrance_fee_deduct_guest_wallet(self.room, self.guest_andy)
        self.assertEqual(50, self.guest_andy.wallet)
    
    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest_andy)
        self.assertEqual(1, self.room.guest_count())

    def test_remove_guest_from_room(self):
        #add 3 guests to the room
        self.room.add_guest_to_room(self.guest_andy)
        self.room.add_guest_to_room(self.guest_fiona)
        self.room.add_guest_to_room(self.guest_jane)
        #guest count = 3
        #remove jane
        self.room.remove_guest_from_room(self.guest_jane)
        #2 people left in the room
        self.assertEqual(2, self.room.guest_count())
    
    # def test_add_songs_to_room(self):
    #     self.room.add_song_to_room(self.guest_andy)
    #     self.assertEqual(1, self.room.songs_count())

    def test_remove_money_to_till(self):
        pass
    
    def test_room__has_capacity(self):
        self.assertEqual(4, self.room.capacity)

    def test_room_is_over_capacity(self):
        pass
    
    def test_room_has_entrance_fee(self):
        self.assertEqual(50.00, self.room.entrance_fee)
    
    def test_customer_cant_afford_room(self):
        pass

    def test_add_to_bar_tab(self):
        pass 

    

    def test_check_in_guest(self):
        #add guest to room list
        #pay entrance fee
        #check customer wallet
        #check
        pass
