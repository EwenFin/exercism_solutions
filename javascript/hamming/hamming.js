var Hamming = function(){

}

Hamming.prototype = {
  compute: function(dna, rna){
    if(dna.length !== rna.length){
      throw new Error('DNA strands must be of equal length.')
    }
    var errorCount = 0;
    var letterIndex = 0;
    for(var i = 0; i < dna.length; i++){
      if(dna.charAt(letterIndex) !== rna.charAt(letterIndex)){
        letterIndex ++;
        errorCount ++;
        }
      else{ 
        letterIndex ++;
      }
    }
    return errorCount;
  }
}


module.exports = Hamming;