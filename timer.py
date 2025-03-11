try:
    from inspect import Traceback
    try:
        minutes_left = 0
        seconds_left = 0
        import numpy as np
        import sounddevice as sd
        import time

        def beep(frequency=1000, duration=10, volume=1.0, sample_rate=44100):
            t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
            wave = volume * np.sin(2 * np.pi * frequency * t)
            sd.play(wave, sample_rate)
            sd.wait() # this def will play a beep

        # this code will play a timer
        def alarm(second):
            time_gone = 0
            while int(time_gone) < int(second):
                time.sleep(1)
                time_gone = time_gone +1
                time_left = int(second) - time_gone
                minutes_left = time_left // 60
                seconds_left = time_left % 60
                print(f'{minutes_left}:{seconds_left}')
        # this code will check if there is no time left:
                if minutes_left == 0 and seconds_left == 0:
                    beep()
                    exit()

        if time == str:
            print('please enter valid seconds')

        else:
            try:
                v_time = input('enter seconds: ')
                alarm(second=v_time)
            except ValueError:
                print('please enter an int')

    except Traceback or TypeError or KeyboardInterrupt:
        exit()

except Traceback or SystemExit or TypeError:
    exit()

repeat = input('do you want to repeat the code? ')
repeat = repeat.lower()
if repeat == 'yes':
    import os
    import sys
    python = sys.executable
    os.execl(python, python, *sys.argv)
else:
    exit()

