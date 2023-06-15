*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board N   0             0             1                     NORTH         0           1           2
Move on bottom edge of the board S  0             0             5                     SOUTH         0           0           6
Move on bottom edge of the board S2 0             0             20                    SOUTH         0           0           21
Move on left edge of the board W    0             6             4                     WEST          0           6           5
Move on bottom edge of the board S3 4             0             35                    SOUTH         4           0           36
Move in the middle of the board N2  5             5             0                     NORTH         5           6           1
Move in the middle of the board E   5             6             1                     EAST          6           6           2
Move in the middle of the board W   3             7             32                    WEST          2           7           33
Move on top edge of the board N     6             9             5                     NORTH         6           9           6
Move on right edge of the board E   9             9             10                    EAST          9           9           11
Move in the middle of the board S   0             9             20                    SOUTH         0           8           21





*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}