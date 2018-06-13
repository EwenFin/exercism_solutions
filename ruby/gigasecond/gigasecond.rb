# frozen_string_literal: true
module BookKeeping
  VERSION = 5
end

# Calculates the moment when someone has lived for 10^9 seconds
class Gigasecond
  def self.from(birth)
    birth + 10**9
  end
end