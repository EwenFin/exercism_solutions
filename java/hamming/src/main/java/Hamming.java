public class Hamming {

  private String string1;
  private String string2;

  public Hamming(String string1, String string2){
    this.string1 = string1;
    this.string2 = string2;
    if(string1.length() != string2.length()){
      throw new IllegalArgumentException();
    }

  }

  public int getHammingDistance(){
        int count = 0;
    int letter_index = 0;
    for(int i = 0; i < string1.length(); i++){
      if(string1.charAt(letter_index) != string2.charAt(letter_index)){
        letter_index ++;
        count ++;
      }
      else{
        letter_index ++;
      }
    }
    return count;

  }
}
