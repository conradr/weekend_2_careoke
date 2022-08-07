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
        self.room = Room("Dollywood", 1000, 0, 50)

    def test_room_has_name(self):
        self.assertEqual("Dollywood", self.room.name)

    def test_room__has_till(self):
        self.assertEqual(1000, self.room.till)

    def test_add_money_to_till(self):
        till_total = self.room.add_money_to_till(self.room)
        self.assertEqual(1050, till_total)

    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest_andy)
        self.assertEqual(1, self.room.guest_count())

    def test_guest_count(self):
        # try to add 5 people
        self.room.add_guest_to_room(self.guest_andy)
        self.room.add_guest_to_room(self.guest_jane)
        self.room.add_guest_to_room(self.guest_jonny)
        self.room.add_guest_to_room(self.guest_fiona)
        # the room is full - return 4
        self.room.add_guest_to_room(self.guest_rob)
        self.assertEqual(4, self.room.guest_count())

    def test_remove_guest_from_room(self):
        # add 3 guests to the room
        self.room.add_guest_to_room(self.guest_andy)
        self.room.add_guest_to_room(self.guest_fiona)
        self.room.add_guest_to_room(self.guest_jane)
        # guest count = 3
        # remove jane
        self.room.remove_guest_from_room(self.guest_jane)
        # 2 people left in the room
        self.assertEqual(2, self.room.guest_count())

    def test_add_songs_to_room(self):
        self.room.add_song_to_room(self.song1)
        self.assertEqual(1, self.room.song_count())

    def test_song_count(self):
        self.room.add_song_to_room(self.song1)
        self.room.add_song_to_room(self.song2)
        self.room.add_song_to_room(self.song3)
        self.room.add_song_to_room(self.song4)
        self.assertEqual(4, self.room.song_count())

    def test_room_is_full_over_4_pax_return_true(self):
        self.assertEqual(True, self.room.room_has_capacity())

    def test_room_is_full_return_false(self):
        self.room.add_guest_to_room(self.guest_andy)
        self.room.add_guest_to_room(self.guest_fiona)
        self.room.add_guest_to_room(self.guest_jane)
        self.room.add_guest_to_room(self.guest_rob)
        self.room.add_guest_to_room(self.guest_jonny)
        self.assertEqual(False, self.room.room_has_capacity())

    def test_check_in_guest(self):
        # add guest to room list
        self.room.add_guest_to_room(self.guest_andy)
        # add money to till
        self.room.add_guest_to_bar_tab(self.guest_andy)
        # deduct from the guest wallet
        self.guest_andy.pay_entrance_fee_deduct_guest_wallet(self.room, self.guest_andy)
        till_total = self.room.add_money_to_till(self.room)
        self.assertEqual(1050, till_total)
        self.assertEqual(50, self.guest_andy.wallet)
        self.assertEqual(1, self.room.guest_count())
        self.assertEqual(1, self.room.bar_tab_count())
    
    def test_check_in_guest_integrated(self):
        self.room.check_in_guest(self.room, self.guest_andy)
        self.assertEqual(1050, self.room.return_till_total(self.room))
        self.assertEqual(50, self.guest_andy.wallet)
        self.assertEqual(1, self.room.guest_count())
        self.assertEqual(1, self.room.bar_tab_count())
    
    def test_return_till_total(self):
        self.guest_andy.pay_entrance_fee_deduct_guest_wallet(self.room, self.guest_andy)
        self.room.add_money_to_till(self.room)
        self.assertEqual(1050, self.room.return_till_total(self.room))

    # def test_room_has_entrance_fee(self):
    #     self.assertEqual(50.00, self.room.entrance_fee)

    def test_customer_cant_afford_room(self):
        pass

    def test_add_to_bar_tab(self):
        self.room.add_guest_to_bar_tab(self.guest_andy)
        self.assertEqual(1, self.room.bar_tab_count())

    def test_spend_money(self):
        # remove money from guest wallet
        # add money to till
        # a
        # add amount to bar tab object
        #self.assertEqual(20, self.room.bar_tab[0]["spend"])
        self.room.check_in_guest(self.room, self.guest_andy)
        self.room.check_in_guest(self.room, self.guest_jane)
        self.room.spend_money(self.guest_andy, 30)
        print("\n")
        self.room.spend_money(self.guest_andy, 50)
        print("\n")
        self.room.spend_money(self.guest_jane, 100)
        print("\n")
        self.room.spend_money(self.guest_jane, 120)
    
    def test_add_spend_to_bar_tab(self):
        pass

       # self.assertEqual(50, self.room.bar_tab)
       
    def test_keep_track_of_spending(self):
        pass
        # add person to guests_in_room list - done
        #self.room.add_guest_to_bar_tab(self.guest_andy)
        # create new list for bar_tab - done
        # add person object to list
        # and spend to list
        # create new method to add person
        # update spend when ever the person spends in the room
        # need to be able to buy something