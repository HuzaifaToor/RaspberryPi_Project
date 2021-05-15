from gpio import GPIO

# Right set mode for this project
GPIO.setmode(GPIO.BCM)

# Wrong mode set
GPIO.setmode(13)
GPIO.setmode("BCM")
GPIO.setmode("Board")

# Right setups
GPIO.setup(GPIO.PIN_ECHO_ULTRASONIC, GPIO.IN)
GPIO.setup(GPIO.PIN_DIR_MOTOR, GPIO.OUT)

# Wrong setups
GPIO.setup(GPIO.PIN_ECHO_ULTRASONIC, 3)
GPIO.setup(37, GPIO.IN)

# Right output
GPIO.output(GPIO.PIN_TRIGGER_ULTRASONIC, GPIO.HIGH)

# Wrong output
GPIO.output(GPIO.PIN_TRIGGER_ULTRASONIC, 3)
GPIO.output(37, GPIO.HIGH)

# Right input
print(GPIO.input(GPIO.PIN_ECHO_ULTRASONIC))

# Wrong input
GPIO.input(37)

# Clean up
GPIO.cleanup()