import cv2
from Solver import Solve_Sudoku
from make_puzzle import make
from image_processing import change_color_and_get_perspective as process
from image_processing import get_digits
from ocr import OCR_digits


img=cv2.imread(r"resources/Sudoku_puzzle.jpeg")
img2=img.copy()
image=process(img2)
image2=image.copy()
numbers=get_digits(image2)
flattened_puzzle=OCR_digits(numbers)
puzzle=make(flattened_puzzle)
s=set()
for i in range(9):
    for j in range(9):
        if puzzle[i][j]!=0:
            s.add((i,j))

istrue=Solve_Sudoku(puzzle)


if istrue:
    print('Puzzle Solved!!!')
else:
    print('Puzzle Not solved :( \nplease try to get a clearer picture(keep the puzzle on a flat surface and place the camera right on top of the surface instead of taking it from an angle ')

colour=(0,0,0)
for i in range(9):
    for j in range(9):
        if (i,j) not in s:
            cv2.putText(image,str(puzzle[i][j]),(int((j+0.5)*84),int((i+0.5)*84)),cv2.FONT_HERSHEY_COMPLEX,1,color=colour,lineType=cv2.LINE_AA, thickness=2)

cv2.imshow('solved_puzzle',image)
cv2.waitKey(0)
