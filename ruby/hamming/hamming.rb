class Hamming

    def self.compute(string1, string2)
      unless string1.length == string2.length
        raise ArgumentError
      end        
        count = 0
        letter_index = 0

          for i in 0..string1.length
          
          if string1[letter_index] != string2[letter_index]
            letter_index += 1
            count += 1

          else
            letter_index += 1
            
          end
      
    end
    return count
  end
end

module BookKeeping
  VERSION = 3 # Where the version number matches the one in the test.
end