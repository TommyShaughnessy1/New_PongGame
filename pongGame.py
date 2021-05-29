import turtle
import random

global score_a 
global score_b
score_a = 0
score_b = 0

num_balls = int(input("Enter the number of balls: "))
 # Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  CPU: 0", align="center", font=("Courier", 24, "normal"))

def create_paddle(x_axis):
    
    paddle= turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5,stretch_len=1)
    paddle.penup()
    paddle.goto(x_axis, 0)
    return paddle
    
paddle_a = create_paddle(-350)
paddle_b = create_paddle(350)




# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# moves paddle A down by subtracting 20 to the ycor
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# moves paddle B up by adding 20 to the ycor
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# moves paddle B down by subtracting 20 to the ycor
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def create_ball():
     # Ball
    y_position = random.randint(-300, 300) 

     
    ball = turtle.Turtle()
    ball.speed(20)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0,y_position)
    ball.dx = 0.5
    ball.dy = 0.5
    return ball

def open_window():
    wn = turtle.Screen()
    wn.title(" Pong By @Tommy Shaughnessy")
    wn.bgcolor("red")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    
    # Keyboard bindings
    wn.listen()

    # when player press w on keyboard the paddle_a_up function invoked
    # moving paddle A up
    wn.onkeypress(paddle_a_up, "w")

        # when player press s on keyboard the paddle_a_down function invoked
    # moving paddle A down
    wn.onkeypress(paddle_a_down, "s")

    # when player press up arrow on keyboard the paddle_b_up function invoked
    # moving paddle B up
    wn.onkeypress(paddle_b_up, "Up")

    # when player press down arrow on keyboard the paddle_b_down function invoked
    # moving paddle B down
    wn.onkeypress(paddle_b_down, "Down")
    return wn

def move_ball(ball):
  
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    #Allows for the ball to bounce off the top and bottom 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -0.3
        
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -0.3

def register_score(ball):
    global score_a
    global score_b

    y_position = random.randint(-300, 300) 

    if ball.xcor() > 350:
       

        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, y_position)
        #ball.dx *= -0.6

    elif ball.xcor() < -350:
            
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, y_position)
       # ball.dx *= -0.6

def detect_collision(ball,paddle_a,paddle_b):
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        
        
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
    
def main_game_functionality():
    balls = []
    t = turtle.Turtle()

    wn = open_window()
   
    # for x in num_balls:
    #     print(x)
    counter = 0
    while counter < num_balls:
        ball = create_ball()
        # balls[counter] = ball
        balls.append(ball)
        


        counter +=1
       

  
    # Create amount of balls that user input specifies.
    # All balls need to move the same way
    # All balls have the same collsion detection 

    # for x in num_balls:
       
    #     ball = create_ball()
        
       
    #     move_ball(ball)
    #     balls.append(ball)

    #print(balls)
           
   
    
    # Main game loop
    while True:

        wn.update()
        counter = 0
        while counter < num_balls:
            for ball in balls:
                move_ball(ball)
                register_score(ball)
                detect_collision(ball,paddle_a,paddle_b)

            counter += 1

        

        
     
main_game_functionality()

    

# If user input is 2
# elif userchoice == "2":
    

#     while True:
        
       
#         #Second ball in play 
#         # moving in opposing direction to first ball
#         ball2 = turtle.Turtle()
#         ball2.speed(20)
#         ball2.shape("square")
#         ball2.color("green")
#         ball2.penup()
#         ball2.goto(0, 0)
#         ball2.dx = -0.5
#         ball2.dy = -0.5

        
#         ball2.setx(ball2.xcor() + ball2.dx)
#         ball2.sety(ball2.ycor() + ball2.dy)

#         if ball2.ycor() > 290:
#             ball2.sety(290)
#             ball2.dy *= -0.3
            
#         elif ball2.ycor() < -290:
#             ball2.sety(-290)
#             ball2.dy *= -0.3
            
#             # Left and right
#             # if the ball goes past 350 or -350 (off the screen)
#             # registers a score for opposing player
#         if ball2.xcor() > 350:
        

#             score_a += 1
#             pen.clear()
#             pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
#             ball2.goto(0, 0)
#             ball2.dx *= -0.6

#         elif ball2.xcor() < -350:
        
#             score_b += 1
#             pen.clear()
#             pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
#             ball2.goto(0, 0)
#             ball2.dx *= -0.6

#         # Paddle and ball collisions
#             # Allows for ball to bounce of paddles 
#         if ball2.xcor() < -340 and ball2.ycor() < paddle_a.ycor() + 50 and ball2.ycor() > paddle_a.ycor() - 50:
#             ball2.dx *= -1
            
#         elif ball2.xcor() > 340 and ball2.ycor() < paddle_b.ycor() + 50 and ball2.ycor() > paddle_b.ycor() - 50:
#             ball2.dx *= -1
    
        
