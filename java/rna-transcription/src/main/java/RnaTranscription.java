import java.util.*;

public class RnaTranscription {
    public String ofDna(String dnaString) {
      if (dnaString == ""){
        return "";   
    }
    String rna = "";     
    
    String[] characters = dnaString.split("");

    for (String character : characters){
      switch(character){
      case "C": rna += "G";
      break;
      case "G": rna += "C";
      break;
      case "T": rna += "A";
      break;
      case "A": rna += "U";
      break;
      }

    }
    return rna;
  }
}


