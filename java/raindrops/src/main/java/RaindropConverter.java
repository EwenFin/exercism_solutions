class RaindropConverter {

    String convert(int number) {

    	String result = "";
    	if(number%3==0){
    		result = result + "Pling";
    	}
    	if(number%5==0){
    		result = result + "Plang";
    	}
    	if(number%7==0){
    		result = result + "Plong";
    	}
    	if(result==""){
    	return Integer.toString(number);
    	}
    	else{
    		return result;
    	}
    }
        //throw new UnsupportedOperationException("Delete this statement and write your own implementation.");
    

}
