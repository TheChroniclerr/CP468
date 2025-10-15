import math
from copy import deepcopy
from typing import Literal

ActionsType = Literal["U", "D", "L", "R"]

class Actions:
    def __init__(self, s: list) -> None:
        """Class constructor.

        Args:
            s (list): State to perform action to.
        """
        assert s and isinstance(s, list) and math.sqrt(len(s)).is_integer(), "Invalid puzzle size."
        
        self.s = s
        self.width: int = int(math.sqrt(len(s)))    # get the n of n-puzzle (n by n)
        self.blankPos: int | None = self._findBlankTileIndex()  # index of blank tile
        assert self.blankPos != -1, "Invalid puzzle, no blank tile."
        self.validActions: list[str] = self._findValidActions()      # list of valid actions
    
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

        return actionsMap[a]()
    
    def up(self) -> list | None:
        """Action - Move the tile below the blank tile upwards.

        Returns:
            list | None: Return list if move successful, else None.
        """
        if "U" in self.validActions:
            newS: list = deepcopy(self.s)
            self._shiftTile(newS, self.blankPos + self.width)
            return newS
        return None
    
    def down(self) -> list | None:
        """Action - Move the tile above the blank tile downward.

        Returns:
            list | None: Return list if move successful, else None.
        """
        if "D" in self.validActions:
            newS: list = deepcopy(self.s)
            self._shiftTile(newS, self.blankPos - self.width)
            return newS
        return None
    
    def left(self) -> list | None:
        """Action - Move the tile right of the blank tile leftward.

        Returns:
            list | None: Return list if move successful, else None.
        """
        if "L" in self.validActions:
            newS: list = deepcopy(self.s)
            self._shiftTile(newS, self.blankPos + 1)
            return newS
        return None
    
    def right(self) -> list | None:
        """Action - Move the tile left of the blank tile rightward.

        Returns:
            list | None: Return list if move successful, else None.
        """
        if "R" in self.validActions:
            newS: list = deepcopy(self.s)
            self._shiftTile(newS, self.blankPos - 1)
            return newS
        return None

    def _shiftTile(self, newS: list, srcPos: int) -> list:
        """Shift the tile in the desired direction.
        Shift from a copy of the puzzle.

        Args:
            newS (list): A copy to shift from.
            srcPos (int): Index of tile to be shifted.

        Returns:
            list: Final state.
        """
        newS[self.blankPos], newS[srcPos] = newS[srcPos], None
        return newS

    # Configuration functions
    def _findBlankTileIndex(self) -> int:
        """Find the blank tile in the n-puzzle.

        Returns:
            int: Index of the blank tile.
        """
        for i, tile in enumerate(self.s):
            if tile is None:
                return i
        return -1

    def _findValidActions(self) -> list:
        """Check if it is possible to move up/down/left/right.

        Returns:
            list: All valid actions.
        """
        validActions: list = [];
        
        if 0 <= self.blankPos + self.width < len(self.s): validActions.append("U")     # check bottom
        if 0 <= self.blankPos - self.width < len(self.s): validActions.append("D")     # check top
        if (self.blankPos % self.width) != 0: validActions.append("R")   # check left
        if (self.blankPos % self.width) != (self.width - 1): validActions.append("L")   # check right
        
        return validActions