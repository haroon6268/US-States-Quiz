import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

img = "blank_states_img.gif"
screen.addshape(img)
screen.tracer(0)

turtle.shape(img)
data = pandas.read_csv("50_states.csv")
state_data = data.state.to_list()
screen.update()
states_list = []

while len(states_list) < 50:
    state_answer = screen.textinput(title=f"{len(states_list)}/50", prompt="What's another state's name?")
    if state_answer is None:
        break
    state_answer = state_answer.title()
    screen.update()
    if state_answer in state_data:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        sd = data[data.state == state_answer]
        t.goto(int(sd.x), int(sd.y))
        t.write(sd.state.item(), font=("Arial", 24, "normal"))
        states_list.append(sd.state.item())

missed_states = [state for state in state_data if state not in states_list]
df = pandas.DataFrame(missed_states)
df.to_csv("missed states")

if len(states_list) >= 50:
    print("You Win!")
