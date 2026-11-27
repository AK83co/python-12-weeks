# Week 10: Inheritance and special methods

Build families of classes and make your objects feel built-in.

**Goals:** Inheritance · super() · Overriding methods · Dunder methods like __add__ and __len__

## Exercises

Open each file, write your code, then check it in the terminal:

| File | Check it with |
|---|---|
| `ex1_animal_sounds.py` | `python check.py 10 animal_sounds` |
| `ex2_2d_vectors.py` | `python check.py 10 2d_vectors` |
| `ex3_playlist.py` | `python check.py 10 playlist` |
| `ex4_shapes.py` | `python check.py 10 shapes` |

Check the whole week at once: `python check.py 10`

## Project: Text adventure engine

Build a small world of connected rooms using classes, with items to pick up and a goal to reach.

Run it with `python weeks/week10_inheritance_and_special/project.py`

- [ ] Write a Room class with a name, description and exits (a dict like {'north': other_room})
- [ ] Create at least 4 rooms and connect them
- [ ] Write a Player class that tracks the current room and an inventory list
- [ ] Read commands like 'go north', 'take key' and 'look'
- [ ] Add a locked room that needs an item to enter
- [ ] Add a way to win

**Stretch goal:** Give some rooms a subclass, like DarkRoom, that needs a lamp to see the description.
