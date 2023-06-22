from discoIPC import ipc
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')

base_activity = {
    'details': 'Hardcore',
    'state' : 'Playing Duo',
    'assets': {
        'large_image': '104835983_p3',
        'large_text': 'Why you looking here?',
        'small_image': '58480164-love-and-icon',
        'small_text': 'Go away~'
    },
    'party': {
        'size': [2, 2]
    }
}

def main():
    client = ipc.DiscordIPC(config['CLIENT']['client_id'])
    # Connect to Discord Client
    client.connect()

    print('\nStarting Custom Activity...\n')
    time.sleep(5)

    try:
        client.update_activity(set_activity()) # Update Activity
        while True:
            input('\nConnected! ')
            # Do nothing   

    except KeyboardInterrupt:
        print('Disconnecting...\n')
        client.disconnect()

def set_activity():
    # Set acitivty for the player.
    activity = base_activity
    return activity

if __name__ == '__main__':
    main()
