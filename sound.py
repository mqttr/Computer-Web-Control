import keyboard

class Sound:
    def volume_up(amount: int):
        '''
        Takes an amount of volume increase and presses the volume up key amount // 2 times.

        :param amount: Twice the presses of the volume up media button 
        '''
        for x in range(amount//2):
            keyboard.press_and_release('B')
    
    def volume_down(amount: int):
        '''
        Takes an amount of volume decrease and presses the volume down key amount // 2 times.

        :param amount: Twice the presses of the volume down media button 
        '''

        for x in range(amount//2):
            keyboard.press_and_release('C')

    def mute():
        keyboard.press_and_release('D')