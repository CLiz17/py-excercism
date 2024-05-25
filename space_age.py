class SpaceAge:
    EARTH_YEAR_SECONDS = 31557600
    
    def __init__(self, seconds):
        self.sec = seconds

    def on_earth(self):
        return round(self.sec / self.EARTH_YEAR_SECONDS, 2)

    def on_mercury(self):
        return round(self.sec / (0.2408467 * self.EARTH_YEAR_SECONDS), 2)

    def on_venus(self):
        return round(self.sec / (0.61519726 * self.EARTH_YEAR_SECONDS), 2)

    def on_mars(self):
        return round(self.sec / (1.8808158 * self.EARTH_YEAR_SECONDS), 2)

    def on_jupiter(self):
        return round(self.sec / (11.862615 * self.EARTH_YEAR_SECONDS), 2)

    def on_saturn(self):
        return round(self.sec / (29.447498 * self.EARTH_YEAR_SECONDS), 2)

    def on_uranus(self):
        return round(self.sec / (84.016846 * self.EARTH_YEAR_SECONDS), 2)

    def on_neptune(self):
        return round(self.sec / (164.79132 * self.EARTH_YEAR_SECONDS), 2)