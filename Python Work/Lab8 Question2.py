#Mary Kate Sheehan
#10/31/2023
#Lab 8 Question 2


def foot_to_meter(foot):
    meter = round(0.305 * foot, 2)
    return meter

def meter_to_foot(meter):
    foot = round(meter / 0.305, 2)
    return foot


print("Feet | Meters")
print(" 0   |", foot_to_meter(0))
print(" 10  |", foot_to_meter(10))
print(" 20  |", foot_to_meter(20))
print(" 30  |", foot_to_meter(30))
print(" 40  |", foot_to_meter(40))
print(" 50  |", foot_to_meter(50))
print(" 60  |", foot_to_meter(60))
print(" 70  |", foot_to_meter(70))
print(" 80  |", foot_to_meter(80))
print(" 90  |", foot_to_meter(90))
print(" 100 |", foot_to_meter(100))

print("**************************************")

print("Meters  | Feet")
print("  0     |", meter_to_foot(0))
print("  10    |", meter_to_foot(10))
print("  20    |", meter_to_foot(20))
print("  30    |", meter_to_foot(30))
print("  40    |", meter_to_foot(40))
print("  50    |", meter_to_foot(50))
print("  60    |", meter_to_foot(60))
print("  70    |", meter_to_foot(70))
print("  80    |", meter_to_foot(80))
print("  90    |", meter_to_foot(90))
print("  100   |", meter_to_foot(100))
