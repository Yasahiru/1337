class AsteroidAnalyzer:
    def __init__(self, data: dict):
        self.name = data["name"]
        self.type = data["type"]
        self.dist = data["dist"]
        self.density = data["density"]
        self.vel = data["vel"]
        self.diam = data["diam"]

    def calculate_time(self):
        if self.vel <= 0:
            return None, None

        dist_km = self.dist * 149597870.7
        time_sec = dist_km / self.vel
        time_hours = time_sec / 3600
        time_days = time_hours / 24

        return round(time_hours, 2), round(time_days, 2)

    def time_score(self):
        time_hours, time_days = self.calculate_time()

        if time_hours is None:
            return 0
        if time_hours < 24:
            return 3
        elif time_days < 7:
            return 2
        return 1

    def diameter_score(self):
        if self.diam > 5:
            return 3
        elif self.diam >= 1:
            return 2
        return 1

    def type_score(self):
        asteroid_type = self.type.lower()

        if "metallic" in asteroid_type:
            return 3
        elif "stony" in asteroid_type or "siliceous" in asteroid_type:
            return 2
        return 1

    def risk_level(self, score):
        if score >= 8:
            return "High Risk 🚨"
        elif score >= 5:
            return "Medium Risk ⚠️"
        return "Low Risk ✅"

    def analyze_asteroid(self):
        time_hours, time_days = self.calculate_time()

        t_score = self.time_score()
        d_score = self.diameter_score()
        ty_score = self.type_score()

        total_score = t_score + d_score + ty_score
        risk = self.risk_level(total_score)

        return {
            "name": self.name,
            "type": self.type,
            "density": self.density,
            "dist": self.dist,
            "vel": self.vel,
            "diam": self.diam,
            "time_hours": time_hours,
            "time_days": time_days,
            "time_score": t_score,
            "diameter_score": d_score,
            "type_score": ty_score,
            "total_score": total_score,
            "risk": risk,
        }


# test example
if __name__ == "__main__":
    data = {
        "name": "AX-12",
        "type": "M-type (metallic)",
        "dist": 0.5,
        "density": 5320,
        "vel": 20,
        "diam": 3.2,
    }

    asteroid = AsteroidAnalyzer(data)
    result = asteroid.analyze_asteroid()

    for key, value in result.items():
        print(f"{key}: {value}")