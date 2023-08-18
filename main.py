# import logic_web
import keyboard
if __name__ == "__main__":
    # logic_web.run_web()

    recorded = keyboard.record(until='esc')
    print(recorded)