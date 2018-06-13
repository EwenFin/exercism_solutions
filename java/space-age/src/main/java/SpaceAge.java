class SpaceAge {

    double ageSeconds;
    double earthAge;

    SpaceAge(double seconds) {
        this.ageSeconds = seconds;
        this.earthAge = this.ageSeconds/31557600;
    }

    double getSeconds() {
        return this.ageSeconds;
    }

    double onEarth() {
        return this.earthAge;
    }

    double onMercury() {
        return this.earthAge / 0.2408467; 
        
    }

    double onVenus() {
        return this.earthAge / 0.61519726;
    }

    double onMars() {
        return this.earthAge / 1.8808158;
    }

    double onJupiter() {
        return this.earthAge / 11.862615;
    }

    double onSaturn() {
        return this.earthAge / 29.447498;
    }

    double onUranus() {
        return this.earthAge / 84.016846;
    }

    double onNeptune() {
        return this.earthAge / 164.79132;
    }

}
