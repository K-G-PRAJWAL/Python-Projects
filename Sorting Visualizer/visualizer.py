import algorithms
import time
import os
import sys
import pygame

 # Set the window length and breadth  (Make sure that the breadth is equal to size of array. [512])
dimensions = [1024, 512]
# List all the algorithms available in the project in dictionary and call the necessary functions from algorithms.py
algorithms = {"SelectionSort": algorithms.SelectionSort(), "BubbleSort": algorithms.BubbleSort(), "InsertionSort": algorithms.InsertionSort(), "MergeSort": algorithms.MergeSort(), "QuickSort": algorithms.QuickSort()}

# Check list of all the available sorting techniques using 'list'
if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        for key in algorithms.keys(): print(key, end=" ") # Display the available algorithms
        print("")
        sys.exit(0)

# Initalise the pygame library
pygame.init()
# Set the dimensions of the window and display it
display = pygame.display.set_mode((dimensions[0], dimensions[1]))
# Fill the window with purple hue
display.fill(pygame.Color("#a48be0"))

def check_events(): # Check if the pygame window was quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

def update(algorithm, swap1=None, swap2=None, display=display): # The function responsible for drawing the sorted array on each iteration
    display.fill(pygame.Color("#a48be0"))
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Sorting...".format(algorithm.name, time.time() - algorithm.start_time)) # Display on title bar
    k = int(dimensions[0]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        colour = (80, 0, 255)
        if swap1 == algorithm.array[i]:
            colour = (0,255,0)
        elif swap2 == algorithm.array[i]:
            colour = (255,0,0)
        # The most important step that renders the rectangles to the screen that gets sorted.
        # pygame.draw.rect(dsiplay_window, color_of_rectangle, size_of_rectangle)
        pygame.draw.rect(display, colour, (i*k,dimensions[1],k,-algorithm.array[i]))
    check_events()
    pygame.display.update()

def keep_open(algorithm, display, time): # Keep the window open until sort completion
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Done!".format(algorithm.name, time))
    while True:
        check_events()
        pygame.display.update()

def main():
    if len(sys.argv) < 2:
        print("Please select a sorting algorithm.") 
    else:
        try:
            algorithm = algorithms[sys.argv[1]] # Pass the algorithm selected
            try:
                time_elapsed = algorithm.run()[1]
                keep_open(algorithm, display, time_elapsed)
                pass
            except:
                pass
        except:
            print("Error.")

if __name__ == "__main__":
    main()
