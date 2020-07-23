class Slot:
    CAPACITY = 13

    def __init__(self):
        self._reservations = {}
        self._size = sum(self._reservations.values()) or None
        
        return
    
    def reservation_exists(self, person, slots):
        already_exists = False
        i = 0

        while i < len(slots) and already_exists == False:
            in_slot = slots[i].get("{}".format(person), default = None)

            if in_slot != None:
                already_exists = True

        return already_exists
    
    def insert_reservation(self, person, party_size):
        inserted = False
        can_insert = False

        if party_size <= (CAPACITY - self._size):
            can_insert = True
            already_exists = self.reservation_exists(person, party_size)

            if already_exists = False:
                self._reservations[str(person)] = party_size
                inserted = True
                
        print(self._reservations)
        return inserted