"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: An artist name and the number of tickets wanted.
# 2. Process: The program asks the user for both values and uses them in a sentence.
# 3. Out: A sentence showing the artist name the number of tickets.
# 4. My two fields, and what I would do with them: I chose the artist name and number of tickets because they could be used in a concert booking form.


# Your code below
artist = input("Enter the artist name: ")
tickets = int(input("Enter the number of tickets: "))

extra_ticket = tickets + 1

print("You want", tickets, "tickets for", artist + ".")
print("With one extra ticket, you would need", extra_ticket, "tickets.")