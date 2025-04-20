def afk_bot():
    import pyautogui as pag
    from random import randint
    from time import sleep

    while True:
        x,y = randint(600,700),randint(200,700)
        pag.moveTo(x,y,0.1)
        sleep(2)





def afk_bot2(): # danger!!!!!!
    import pyautogui as pag

    while True:
        x,y = pag.position()
        pag.FAILSAFE = False
        if x != 600 and y != 600:
            pag.moveTo(600,600,0.1)




afk_bot2()