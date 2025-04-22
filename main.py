# Vek Unbound Main Launcher
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from core import VekCore

if __name__ == "__main__":
    vek = VekCore()
    print(vek.startup())

    while True:
        try:
            user_input = input("\nYou: ")
            response = vek.process(user_input)
            print(f"Vek: {response}")
        except KeyboardInterrupt:
            print("\nSession ended.")
            break
