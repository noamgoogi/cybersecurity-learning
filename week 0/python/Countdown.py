import time

cooldown = int(input("Enter cooldown time in seconds: "))

for i in range(cooldown):
    print("Time left:", cooldown - i)
    time.sleep(1)
print("Times Up")