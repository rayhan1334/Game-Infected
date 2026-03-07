from game import Game
from auth import login_or_signup

def main():

    username = login_or_signup()

    game = Game(username)
    game.run()

if __name__ == "__main__":
    main()
