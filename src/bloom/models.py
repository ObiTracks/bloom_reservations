from django.db import models
from slotclass import Slot
# Create your models here.

class Slots(models.Model):
    slot1 = Slot()
    slot2 = Slot()
    slot3 = Slot()
    slots = [slot1,slot2,slot3]
    

    #Things to check for:
    #Is the party size able to fit in the pool?
    #Is there another reservation under that person?
    #Is the reservation being made the day before

    def insert_reservation(slot, slots, person, party_size):
        can_insert = False
        already_exists = False
        capacity = 13

        #Figuring out the current slot size
        slot_values = slot.values()
        slot_status = sum(slot_values)

        if party_size < (capacity - slot_status):
            n = 0
            can_insert = True

            while n < len(slots) and already_exists:
                if slots[0].get("{}".format(person))

        return

    def reservation_exists(slots, person):
        already_exists = False
        n = 0

        while n < len(slots) and already_exists == False:
            in_slot = slots[n].get("{}".format(person), default = None)

            if in_slot != None:
                already_exists = True
            
            n += 1
        n = 0

        if already_exists == False:
            slot[str(person)] = party_size