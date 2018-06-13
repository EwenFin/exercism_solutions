import java.util.*;

public class PangramChecker {

    public boolean isPangram(String input) {
      for(char letter = 'a'; letter <= 'z'; letter++){
        if(input.toLowerCase().indexOf(letter) == -1){
            return false;
          }
      }
    return true;
  }
}
