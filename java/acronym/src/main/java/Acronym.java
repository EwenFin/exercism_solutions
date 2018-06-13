class Acronym {
  private String phrase;

    Acronym(String phrase) {
        this.phrase = phrase;
    }

    String get() {
        String[] words = phrase.split("\\W+");
        String result = "";
        for(String word : words){
          result  = result + word.charAt(0);
        }
        result = result.toUpperCase();
        return result;
    }
}
