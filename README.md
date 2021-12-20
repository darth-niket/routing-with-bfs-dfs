PART 1:

Summary: 
    The problem put forth is to identify the shortest path from agent(p) to person(@). The program must return the length of the path and the directions the agent followed to reach the destination.
    Bread First Search is used to solve this problem. Starting from position 'p' on the grid the goal is to find the next possible path 'p' can take to move towards the goal. All possible moves are appended to a list. Then each move is popped from the list and all possible next moves for the move that was popped are visited. This process is continued until we reach the goal state.

Problems Faced:
    1. The problem with the skeleton code that was given was that the states which were visited were not recorded and the same states were explored iteratively which led the code to go in an infinite loop.
    2. Directions were not part of the code given. Hence the directions were not returned along with the path

Approach:
    First part of the resolving the problems was to make a note of all states that were visited. And if a state was visited the code should not explore the state again i.e must not find successor moves and append to the fringe.
    Second part of resolving the problems was to make note of the directions that pichu takes as it moves towards the goal. An addition field called directions was added to the fringe that recorded the moves of the pichu. If the pichu moved up, down, right, left the direction string was updated accordingly with the characters 'U', 'D', 'R', 'L' respectively.

Initial state : position of 'p'
Goal state : 'position'
State space : All possible paths the pichu can move through ie. all the dots in the grid.
Successor function: All possible paths pichu can take on the next move. (Excluding 'X')
Cost: The cost for moving through one point on the grid to the neighbouring point is 1


Part 2:

Summary:
    The problem put forth is to arrange pichus in a grid such that they cannot see each other. The program must return a map of the grid such that the pichus are ideally placed.
    To solve this problem the first consideration that should be done is to make a note of all successors that were visited and were not the goal states. This eliminates any chances of the code going through an infinite loop as these successor maps are not visited again. We then have to make sure that each pichu is ideally placed in the grid and cannot see other pichus. 

Problems Faced:
    1. The problem with the skeleton code was that successor maps that were visited and were not considered were not noted down.
    2. There was no function that could check if the position of the pichu is valid. There were no checks to make sure that the pichus were invisible to each other

Approach:
    First part of the solution was to make a note of all visited successor maps in a list. If ever a map was revisited the solve function will not take it into consideration.
    Next part was to make sure to add positional checks to the pichu location. For a given position of a pichu we need to check there were no pichus in the same row, colomn, and diagonally(Pichus can be placed on either side of the wall)
    Eight functions were written to check if another pichu is present in each direction ie north, south, east, west, north-west, north-east, south-west, south-east. If all the checks were passed the pichu can be placed at the location that is under consideration.

Initial State: 1 pichu already placed in the grid 
Successor State: All possible maps for the next position where the pichu can be placed
Goal State: Pichus placed ideally in the map so that they are invisible to each other

