

public class RomanNumeral{

	private int number;

	public RomanNumeral(int number){
		this.number = number;
	}

	public String getRomanNumeral(){

		String romanNumeral = "";

        while(number >= 1000) {
            number -= 1000;
            romanNumeral += "M";
        }
        while(number >= 900){
            number -= 900;
            romanNumeral += "CM";
        }
        while(number >= 500){
            number -= 500;
            romanNumeral += "D";
        }
        while(number >= 400){
            number -= 400;
            romanNumeral += "CD";
        }
        while(number >= 100){
            number -= 100;
            romanNumeral += "C";
        }
        while(number >= 90){
            number -= 90;
            romanNumeral +="XC";
        }
        while(number >= 50){
            number -= 50;
            romanNumeral +="L";
        }
        while(number >= 40){
            number -= 40;
            romanNumeral +="XL";
        }
        while(number >= 10){
            number -= 10;
            romanNumeral += "X";
        }
        while(number >= 9){
            number -= 9;
            romanNumeral += "IX";
        }
        while(number >= 5){
            number -= 5;
            romanNumeral += "V";
        }
        while(number >= 4){
            number -= 4;
            romanNumeral += "IV";
        }
        while(number >= 1){
            number -= 1;
            romanNumeral += "I";
        }
		return romanNumeral;
	}

}
