from enum import Enum


class Actions(Enum):
    
    PrintAll = 1
    PrintAt = 2
    AddBook = 3
    UpdateAt = 4   
    RemoveBook = 5
    FindByAuthor = 6
    FindByYear = 7  
    FindByTitle = 8
    Exit = 9
    Back = 0
