from typing import Literal
from copy import deepcopy
import math


ActionsType = Literal["U", "D", "L", "R"]

class Actions:
    def __init__(self, s: list) -> None:
        assert type(s) != list or not(math.sqrt(len(self.s)).is_integer()) , "Invalid size of puzzle."
        
        self.s = s
        self.width: int = int(math.sqrt(len(s)))     # get the n of n-puzzle (n by n)
        self.blankPos: int | None = self._findBlankTileIndex(self)   # index of blank tile
        assert self.blankPos, "Invalid puzzle."
        self.validActions: list = self._findValidActions(self)  # list of valid actions
    
    def result(self, a: ActionsType) -> list | None:
        """Transition Model - Alternative method of action call using ActionType keys.

        Args:
            a (ActionsType): A valid type of action.

        Returns:
            list | None: Return list if move successful, else None.
        """
        actionsMap: dict = {
            "U": self.up,
            "D": self.down,
            "L": self.left,
            "R": self.right
        }
        newS: list = deepcopy(self.s)
        
        return actionsMap[a]
    
    def up(self) -> list | None:
        """Action - Move the tile below the blank tile upwards.

        Returns:
            list | None: Return list if move successful, else None.
        """
        newS: list = deepcopy(self.s)   # prevent shifting argument list
        
        if "U" in self.validActions:
            self._shiftTile(newS, self.blankPos + self.width)
            return newS
        return None
    
    def down(self) -> list | None:
        """Action - Move the tile above the blank tile downward.

        Returns:
            list | None: Return list if move successful, else None.
        """
        newS: list = deepcopy(self.s)   # prevent shifting argument list
        
        if "D" in self.validActions:
            self._shiftTile(newS, self.blankPos - self.width)
            return newS
        return None
    
    def right(self) -> list | None:
        """Action - Move the tile left of the blank tile rightward.

        Returns:
            list | None: Return list if move successful, else None.
        """
        newS: list = deepcopy(self.s)   # prevent shifting argument list
        
        if "D" in self.validActions:
            self._shiftTile(newS, self.blankPos - 1)
            return newS
        return None
    
    def left(self) -> list | None:
        """Action - Move the tile right of the blank tile leftward.

        Returns:
            list | None: Return list if move successful, else None.
        """
        newS: list = deepcopy(self.s)   # prevent shifting argument list
        
        if "D" in self.validActions:
            self._shiftTile(newS, self.blankPos + 1)
            return newS
        return None

    def _shiftTile(self, newS: list, srcPos: int) -> list:
        newS[self.blankPos - 1] = newS[srcPos - 1]     # move number from source tile to blank tile
        newS[srcPos - 1] = None                # clear the original source tile number
        
        return newS

    # Configuration functions
    def _findBlankTileIndex(self) -> int:
        i: int = 1
        
        for tile in self.s:
            if tile == None or tile == 0:
                return i
            i += 1

        return -1

    def _findValidActions(self) -> list:
        validActions: list = [];
        
        if 1 <= self.blankPos + self.width <= len(self.s) + 1: validActions.append("U")    # check bottom
        if 1 <= self.blankPos - self.width <= len(self.s) + 1: validActions.append("D")    # check top
        if not(self.blankPos % self.width == 1): validActions.append("R")             # check left
        if not(self.blankPos % self.width == 0): validActions.append("L")             # check right
        
        return validActions