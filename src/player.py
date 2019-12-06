# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
  def __init__(self, name, current_room):
    super().__init__()
    self.name = name
    self.current_room = current_room
    self.inventory = []

  def add_item(self, item):
    self.inventory.append(item)

  def remove_item(self, item):
    self.inventory.remove(item)
