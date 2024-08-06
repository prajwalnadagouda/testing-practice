# Designing music taste

from enum import Enum

class Status(Enum):
    LIKE=1
    NEUTRAL=0
    DISLIKE=-1


class Taste:
    def __init__(self):
        self.taste_status=Status.NEUTRAL


        self.like_action={
            Status.NEUTRAL : Status.LIKE,
            Status.LIKE : Status.NEUTRAL,
            Status.DISLIKE : Status.LIKE
        }

        self.dislike_action={
            Status.NEUTRAL : Status.DISLIKE,
            Status.LIKE : Status.DISLIKE,
            Status.DISLIKE : Status.NEUTRAL
        }

    def like_button(self):
        self.taste_status= self.like_action[self.taste_status]

    def dislike_button(self):
        self.taste_status= self.dislike_action[self.taste_status]

    def current_taste(self):
        return self.taste_status
    

    def sequence(ops):
        t=Taste()
        for i in ops:
            if i.lower() == "l":
                t.like_button()
            if i.lower() == "d":
                t.dislike_button()
        return(t.current_taste())