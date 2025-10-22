start_led, loop_time = input().split()
loop_time = int(loop_time)

start_index_map = {"R": 0, "G": 1, "B": 2}
start_index = start_index_map[start_led.capitalize()]

leds = ["Red", "Green", "Blue"]

while loop_time > 0:
    print(leds[start_index], end=" ")
    start_index = (start_index + 1) % 3
    loop_time -= 1
