using System.Collections.Generic;
using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(string key, out int xChange, out int yChange)
    {
      xChange = 0;
      yChange = 0;
      switch(key){
        case "LeftArrow":
          xChange -= 1;
        break;
        case "RightArrow":
          xChange += 1;
        break;
        case "UpArrow":
          yChange -= 1;
        break;
        case "DownArrow":
          yChange += 1;
        break;
        case "Spacebar":
          xChange = 0;
          yChange = 0;
        break;
        default:
          throw new Exception();
      }
    }

    
    private static Dictionary<string, char> CursorLookup = new Dictionary<string, char>()
    {
      {"LeftArrow", '←'},
      {"RightArrow", '→'},
      {"UpArrow", '↑'},
      {"DownArrow", '↓'}
    };

    public new static char UpdateCursor(string key)
    {
      return CursorLookup[key];   
    }

    public new static int KeepInBounds(int coordinate, int max)
    {
      if(coordinate < 0){
         return max -1;
      } else if (coordinate >= max){
         return 0;
      } else {
        return coordinate;
      }
    }

    public new static bool DidScore(int xFruit, int yFruit, int x, int y)
    {
    return xFruit == x &&  yFruit == y;
    }
    
  }
}