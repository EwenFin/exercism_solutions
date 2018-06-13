var DnaTranscriber = function(){

}


DnaTranscriber.prototype = {
  toRna: function(string){
    var rna = ""
    string.forEach(character){
      switch(character){
        case "C": rna += "G";
        break;
        case "G": rna += "C";
        break;
        case "T": rna += "A";
        break;
        case "A": rna += "U";
      }

    }

  }

}

module.exports = DnaTranscriber;