# from this code we will know the current time which will help while making the alarm
# beep sound:
try:
     import numpy as np
     import sounddevice as sd

     def beep(frequency=1000, duration=10, volume=1.0, sample_rate=44100):
         t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
         wave = volume * np.sin(2 * np.pi * frequency * t)
         sd.play(wave, sample_rate)
         sd.wait()

except KeyboardInterrupt:
    pass

# alarm code:
try:
    import datetime
    import time
    alarm_time = input('enter alarm time: ')
    print(f'alarm set to {alarm_time}')


    while True:
        time.sleep(1)
        now = datetime.datetime.now()
        now1  = now.strftime('%H:%M:%S')
        # this also checks if the current time = alarm time
        if str(alarm_time)==str(now1):
            beep(1000, 10)
            exit()
        #print(now1)

except KeyboardInterrupt:
    exit()