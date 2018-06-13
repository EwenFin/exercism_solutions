import java.util.Collections;
import java.util.ArrayList;

final class HandshakeCalculator {

     ArrayList<Signal> calculateHandshake(int number) {
    	ArrayList<Signal> handshake = new ArrayList<Signal>();
    	Boolean reverse = true;
    	String binary = Integer.toBinaryString(number);
    	String padding = "";

    	for(int i=0; i < 5-binary.length(); i++){
    		padding += '0';
    	}

    	binary = padding + binary;
    	
		for(int i=0; i<5; i++){
			if(binary.charAt(i)=='1'){
				switch(i){
					case 4: handshake.add(Signal.WINK);
					break;
					case 3: handshake.add(Signal.DOUBLE_BLINK);
					break;
					case 2: handshake.add(Signal.CLOSE_YOUR_EYES);
					break;
					case 1: handshake.add(Signal.JUMP);
					break;
					case 0: reverse = false;
					break;
				}
			}

		}
		if(reverse){
			Collections.reverse(handshake);
			}
    	return handshake;    
    }
}
