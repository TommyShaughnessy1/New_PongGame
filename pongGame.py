import turtle

score_a = 0
score_b = 0
userchoice = input("Select 1 for one ball or 2 for two balls")
 # Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  CPU: 0", align="center", font=("Courier", 24, "normal"))

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

def main_game_functionality():

    wn = turtle.Screen()
    t = turtle.Turtle()

    wn.title(" Pong By @Tommy Shaughnessy")
    wn.bgcolor("red")
    wn.setup(width=800, height=600)
    wn.tracer(0)

        # sets the initial Score of the game to 0-0
    # Ball
    ball = turtle.Turtle()
    ball.speed(20)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.5
    ball.dy = 0.5

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

    # moves paddle A up by adding 20 to the ycor

        # Main game loop
    while True:
            score_a =0
            score_b =0
            
            wn.update()
            
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
            

            # Left and right
            # if the ball goes past 350 or -350 (off the screen)
            # registers a score for opposing player
            if ball.xcor() > 350:
                
                score_a += 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                ball.goto(0, 0)
                ball.dx *= -0.6

            elif ball.xcor() < -350:
               
                score_b += 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                ball.goto(0, 0)
                ball.dx *= -0.6

            # Paddle and ball collisions
            # Allows for ball to bounce of paddles 
            if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
                ball.dx *= -1
            
            
            elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
                ball.dx *= -1


# If user selects one 
if userchoice == "1": 
  main_game_functionality()

    

# If user input is 2
elif userchoice == "2":
    

    while True:
        
       
        #Second ball in play 
        # moving in opposing direction to first ball
        ball2 = turtle.Turtle()
        ball2.speed(20)
        ball2.shape("square")
        ball2.color("green")
        ball2.penup()
        ball2.goto(0, 0)
        ball2.dx = -0.5
        ball2.dy = -0.5

        
        ball2.setx(ball2.xcor() + ball2.dx)
        ball2.sety(ball2.ycor() + ball2.dy)

        if ball2.ycor() > 290:
            ball2.sety(290)
            ball2.dy *= -0.3
            
        elif ball2.ycor() < -290:
            ball2.sety(-290)
            ball2.dy *= -0.3
            
            # Left and right
            # if the ball goes past 350 or -350 (off the screen)
            # registers a score for opposing player
        if ball2.xcor() > 350:
        

            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            ball2.goto(0, 0)
            ball2.dx *= -0.6

        elif ball2.xcor() < -350:
        
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            ball2.goto(0, 0)
            ball2.dx *= -0.6

        # Paddle and ball collisions
            # Allows for ball to bounce of paddles 
        if ball2.xcor() < -340 and ball2.ycor() < paddle_a.ycor() + 50 and ball2.ycor() > paddle_a.ycor() - 50:
            ball2.dx *= -1
            
        elif ball2.xcor() > 340 and ball2.ycor() < paddle_b.ycor() + 50 and ball2.ycor() > paddle_b.ycor() - 50:
            ball2.dx *= -1
    
        
