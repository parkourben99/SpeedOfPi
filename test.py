from lib.main import SpeedOfPi


if __name__ == '__main__':
    speedOfPi = SpeedOfPi()
    speedOfPi.load_config()

    nodes = list(speedOfPi.nodes.keys())
    node = speedOfPi.nodes[nodes[0]]

    button = node.get_button()

    value = button.bus.read_byte(button.address)

    if value == 4:
        node.activate()

    print(value)