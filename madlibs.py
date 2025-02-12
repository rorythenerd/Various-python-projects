import turtle as trtl

adj1 = str(input("Enter an adjective: "))
noun1 = str(input("Enter a noun: "))
verbed = str(input("Enter a verb ending in -ed: "))
noun2 = str(input("Enter a noun: "))
noun3 = str(input("Enter a noun: "))
number = str(input("Enter a number: "))
animal1 = str(input("Enter an animal: "))
anObject = str(input("Enter an object: "))
adj2 = str(input("Enter an adjective: "))
famousPerson = str(input("Enter a famous person's name: "))
communityArea = str(input("Enter an area in your community: "))
largeNumber = str(input("Enter in a large number: "))
animal2 = str(input("Enter an animal: "))
vehicle = str(input("Enter a vehicle: "))
emotion = str(input("Enter an emotion: "))
exclamation = str(input("Enter an exclamation: "))

#Ask the user if they want to follow the animal's advice
follow_advice = str(input("Do you want to follow the animal's advice? (yes/no): ")).lower()

#Today was a very <adj> day. Firstly, I had <noun> and <noun> for breakfast.
#I quickly grabbed my <noun> and decided to go for a walk.
#But when I <verb -ed> outside, I was greeted by a <number> foot tall <animal> who handed me a(n) <object>.
#"You need this for your <adj> journey." it said.
#Then I ran into <famous person> at the <community area>.
#I took <large number> pictures with them.
#Later on, I saw a(n) <animal> riding a <vehicle>. 
#I was so <emotion>, I yelled "<exclamation>!"

wn = trtl.Screen()
display = trtl.Turtle()
display.hideturtle()
display.penup()

#Starting position for the turtle to write text
display.setposition(-500, 250)

#Bouncing for movement
def move_turtle():
    display.setposition(display.xcor() +20, display.ycor() -20)
    display.right(10)
    display.forward(20)
    display.left(10)

story_lines = [
    f'Today was a very {adj1} day. Firstly, I had {noun1} and {noun2} for breakfast.',
    f'I quickly grabbed my {noun1} and decided to go for a walk.',
    f'But when I {verbed} outside, I was greeted by a {number} foot tall {animal1} who handed me a(n) {anObject}.',
    f'"You need this for your {adj2} journey." it said.',
    f'Then I ran into {famousPerson} at the {communityArea}.',
    f'I took {largeNumber} pictures with them.',
    f'Later on, I saw a(n) {animal2} riding a {vehicle}.',
    f'I was so {emotion}, I yelled "{exclamation}"!' ]

#Add the conditional part to the story
if follow_advice == "yes":
    story_lines.append(f'I decided to follow the animal\'s advice and embarked on a grand adventure!')
else:
    story_lines.append(f'I decided not to follow the animal\'s advice and went back home to rest.')

#Function to write a line and move the turtle down
def write_line(text, text_color):
    display.color(text_color)
    display.write(text, align = "left", font = ("Arial", 14, "normal"))
    move_turtle()

#ITERATION
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "brown", "magenta"]
for i, line in enumerate(story_lines):
    write_line(line, colors[i])

#Keep the window open
wn.mainloop()
