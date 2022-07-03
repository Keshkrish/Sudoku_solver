# Sudoku_solver
Given an image of a sudoku puzzle, solve the puzzle

High Level Details:

1. Given image is preprocessed and a bird's eye view of the same is generated using the findContours() method and the getWarpPerspective() method in OpenCV.

2. The digits are extracted by cropping the image further and by using a pre trained neural network to classify the digits.

3. Once the puzzle is generated, backtrackking algorithm is used to solve the same. The solution is projected back on the image using putText() method.

  
