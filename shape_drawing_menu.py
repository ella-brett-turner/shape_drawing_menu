"""
    Date: Due June 19th, 2021
    Write a menu-driven program that allows the user to choose a shape
    or quit from a  menu and specify the location and size of the shape.
    Process user input. Output is drawing the shape. Then show menu again.
"""

#Annotate variables:

width: int = -1
length: int = -1
radius: int = -1

import turtle

def draw_rectangle(x: float, y: float, width: float, length: float) -> None:
    """Draw a rectangle at lower left corner x, y of width and length."""
    import turtle
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)

def draw_circle(x: float, y: float, radius: float) -> None:
    """Draw a circle at lower center x,y of size radius."""
    import turtle
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.circle(radius)

def menu() -> int:
    choice = 0
    if choice !=1 and choice != 2 and choice != 3:
        print("1. Draw a rectangle \n2. Draw a circle \n3. Quit")
        choice = int(input("Please enter the number of your choice: "))
        
        if choice == 3:
            exit()
        
        if choice != 1 and choice != 2:
            print("That is not a valid choice.")   
        main(choice)
     
def main(choice) -> None:
    """Choose what shape you want to draw with the turtle and specify
    size/location and present a menu of options to the user.
    Loop until the user chooses a valid menu choice."""
    
    if choice != 3:
        if choice == 1:
            x = int(input("At what x coordinate? "))
            y = int(input("At what y coordinate? "))
            width = int(input("What width?" ))
            length = int(input("What height? "))
            
            while width < 0:
                print("That value must be positive.")
                width = int(input("What width?" ))
            while length < 0:
                print("That value must be positive.")
                length = int(input("What height? "))
                
            draw_rectangle(x, y, width, length)
            
        if choice == 2:
            x = int(input("At what x coordinate? "))
            y = int(input("At what y coordinate? "))
            radius = int(input("What radius? "))
            
            while radius < 0:
                print("That value must be positive.")
                radius = int(input("What radius? "))
                    
            draw_circle(x, y, radius)
    menu()
menu()

##Testing:
#1. Draw a rectangle 
#2. Draw a circle 
#3. Quit
#Please enter the number of your choice: 0
#That is not a valid choice.
#1. Draw a rectangle 
#2. Draw a circle 
#3. Quit
#Please enter the number of your choice: 4
#That is not a valid choice.
#1. Draw a rectangle 
#2. Draw a circle 
#3. Quit
#Please enter the number of your choice: 1
#At what x coordinate? -200
#At what y coordinate? -200
#What width?100
#What height? 50
#1. Draw a rectangle 
#2. Draw a circle 
#3. Quit
#Please enter the number of your choice: 1
#At what x coordinate? 200
#At what y coordinate? 200
#What width?50
#What height? 100
#1. Draw a rectangle 
#2. Draw a circle 
#3. Quit
#Please enter the number of your choice: 2
#At what x coordinate? -200
#At what y coordinate? 200
#What radius? 50
#1. Draw a rectangle 
#2. Draw a circle 
#3. Quit
#Please enter the number of your choice: 2
#At what x coordinate? 200
#At what y coordinate? -200
#What radius? 200
#1. Draw a rectangle 
#2. Draw a circle 
#3. Quit
#Please enter the number of your choice: 3

