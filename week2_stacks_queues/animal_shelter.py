from collections import deque

class Shelter:

    def __init__(self):
        self.dog_q = deque()
        self.cat_q = deque()
        self.all_q = deque()

    def enqueue(self, animal_type: str, animal_name: str) -> None:
        # add animal to appropriate queue
        return 0

    def dequeue_any(self):
        # returns oldest animal regardless of animal_type
        return 0

    def dequeue_dog(self):
        # returns oldest dog
        return 0


    def dequeue_cat(self):
        # returns oldest cat
        return 0

my_shelter = Shelter()

my_shelter.dog_q.append(5)
