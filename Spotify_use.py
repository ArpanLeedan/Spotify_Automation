def spotify(emotion):
    import pyautogui
    import os
    import time
    print(emotion)
    os.system("Spotify")
    time.sleep(5)
    if(emotion.lower()=="frustrated"):
        pyautogui.hotkey('ctrl','l')
        pyautogui.write('\tfrustration remover', interval=0.2)

        for key in ['enter', 'pagedown', 'tab', 'tab', 'enter']:
            time.sleep(2)
            pyautogui.press(key)
    elif(emotion.lower()=="joyful")or(emotion.lower()=="happy"):
        pyautogui.hotkey('ctrl','l')
        pyautogui.write('\thappy english songs', interval=0.2)

        for key in ['enter', 'pagedown', 'tab', 'tab', 'enter']:
            time.sleep(2)
            pyautogui.press(key)
    elif(emotion.lower()=="sad"):
        pyautogui.hotkey('ctrl','l')
        pyautogui.write('\tsad english songs', interval=0.2)

        for key in ['enter', 'pagedown', 'tab', 'tab', 'enter']:
            time.sleep(2)
            pyautogui.press(key)
    elif(emotion.lower()=="angry"):
        pyautogui.hotkey('ctrl','l')
        pyautogui.write('\tangry english', interval=0.2)

        for key in ['enter', 'pagedown', 'tab', 'tab', 'enter']:
            time.sleep(2)
            pyautogui.press(key)
