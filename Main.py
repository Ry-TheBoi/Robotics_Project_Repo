#region VEXcode Generated Robot Configuration
import math
import random
from vexcode_vr_robot import *

drivetrain = Drivetrain()
magnet = Electromagnet("magnet", 0)
pen = Pen()
brain = Brain()
left_bumper = Bumper("leftBumper", 1)
right_bumper = Bumper("rightBumper", 2)
distance = Distance()
front_eye = EyeSensor("fronteye", 3)
down_eye = EyeSensor("downeye", 4)
location = Location()
#endregion VEXcode Generated Robot Configuration
# ------------------------------------------
# 
#     Project:      VEXcode Project
#    Author:       Annonymous
#    Created:
#    Description:  VEXcode VR Python Project
# 
# ------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"

artMatrix = []

def main():
    
    global artMatrix

#matrix = [[4, 5, 3, 9],
#          [7, 1, 8, 2],
#          [5, 6, 4, 7]]
#    brain.print(matrix)


    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    
    #sets up art matrix 8x8
    for row in range(8):
        newRow = [] #This is a new row that's being instantiated
        #newRow.append(1)
        artMatrix.append(newRow)
    
    brain.print(artMatrix)
    brain.new_line()

    for i in range(8):
        drawColumn(1)
        wait(2, MSEC)

    #Showing Results

    brain.print("----------------")
    brain.new_line()
    brain.print("SHOWING RESULTS:")
    brain.new_line()
    brain.print("----------------")
    brain.new_line()

    wait(1, SECONDS)
    showResults()
    
    

def showResults():
    global artMatrix

    count = 0
    maxItems = 7

    for i in range(8):
        for row in range(8):
            if (row % 2 == 0):

                lastTargetIndex = maxItems - count

                if (artMatrix[row][lastTargetIndex] == 1):
                    brain.set_print_color(GREEN)
                    brain.print("1")
                else:
                    brain.set_print_color(BLUE)
                    brain.print("0")
            else:
                if (artMatrix[row][count] == 1):
                    brain.set_print_color(GREEN)
                    brain.print("1")
                else:
                    brain.set_print_color(BLUE)
                    brain.print("0")
        count += 1
        brain.new_line()


counter = 1       
def drawColumn(row):
    global counter
    global artMatrix
    for i in range(9):
        drivetrain.drive_for(FORWARD, 200, MM)
        if (down_eye.detect(GREEN)):
            index = counter - 1
            artMatrix[index].append(1)
        else:
            index = counter - 1
            artMatrix[index].append(0)
        
        if front_eye.near_object():

            #see what the row prints out
            brain.print(artMatrix)
            brain.new_line()

            #Sort out counter
            counter += 1

            #do actual thing..
            drivetrain.stop()

            #sort out turns
            if (counter % 2 == 0):
                drivetrain.turn_for(RIGHT, 90, DEGREES)
            else:
                drivetrain.turn_for(LEFT, 90, DEGREES)

            
            drivetrain.drive_for(FORWARD, 200, MM)
            wait(2, MSEC)
            drivetrain.stop()
            wait(2, MSEC)


            if (counter % 2 == 0):
                drivetrain.turn_for(RIGHT, 90, DEGREES)
            else:
                drivetrain.turn_for(LEFT, 90, DEGREES)    

        wait(2, MSEC)
        
    drivetrain.stop()



# VR threads — Do not delete
vr_thread(main())
