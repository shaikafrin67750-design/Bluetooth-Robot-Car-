# Bluetooth Robot Car using Python

def move_robot(command):
command = command.upper()

```
if command == "F":
    print("Robot Car: Moving FORWARD")

elif command == "B":
    print("Robot Car: Moving BACKWARD")

elif command == "L":
    print("Robot Car: Turning LEFT")

elif command == "R":
    print("Robot Car: Turning RIGHT")

elif command == "S":
    print("Robot Car: STOPPED")

else:
    print("Invalid command!")
```

while True:
print("\n===== BLUETOOTH ROBOT CAR =====")
print("F - Forward")
print("B - Backward")
print("L - Left")
print("R - Right")
print("S - Stop")
print("Q - Exit")

```
command = input("Enter Bluetooth command: ")

if command.upper() == "Q":
    print("Bluetooth Robot Car Closed.")
    break

move_robot(command)
```
