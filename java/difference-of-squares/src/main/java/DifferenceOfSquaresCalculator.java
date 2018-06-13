class DifferenceOfSquaresCalculator {

    int computeSquareOfSumTo(int input) {
        int result = 0;
    	for(int i=0; i<=input; i++){
        result = result + i;
    	}
    	int square = result * result;
    	return square;
    }

    int computeSumOfSquaresTo(int input) {
    	int result = 0;
    	for(int i=0; i<=input; i++){
    	int square = i * i;	
        result = result + square;
    	}
    	return result;
    }

    int computeDifferenceOfSquares(int input) {
        int squareTotal = computeSquareOfSumTo(input);
        int sumTotal = computeSumOfSquaresTo(input);
        int difference = squareTotal - sumTotal;
        return difference;
        
    }

}
