# from dataclasses import dataclass
# from drone import Drone
# from zone import Zone
# from zone_type import ZoneRole


# @dataclass
# class ZoneState:
#     def __init__(self, zone: Zone):
#         self.zone = zone
#         self.current_drones: list[Drone]

#     def exceed_drone_capacity(self) -> bool:
#         if self.zone.zone_role in [ZoneRole.START, ZoneRole.END]:
#             return False
#         return len(self.current_drones) > self.zone.max_drones
