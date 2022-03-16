
forth_lines = ["","suck his thumb", "tie her shoe", "climb a tree",
               "shut the door", "take a dive", "pick up sticks",
               "pray to heaven", "check the gate", "check the time",
               'say “The End!”']

def sing_verse(verse_num):
    print(f"The ants go marching {verse_num} by {verse_num}, hurrah, hurrah.")
    print(f"The ants go marching {verse_num} by {verse_num}, hurrah, hurrah.")
    print(f"The ants go marching {verse_num} by {verse_num},")
    current_forth_line = forth_lines[verse_num]
    print(f"The little one stops to {current_forth_line}.")
    print("""And they all go marching down,
To the ground, to get out of the rain.
BOOM! BOOM! BOOM!
    """)


def main():
    for verse in range(1,11):
        sing_verse(verse)


main()