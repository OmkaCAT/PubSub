from bus import Bus


def subscriber(data=None, **kwargs):
    print(data)

bus = Bus()

bus.subscribe("1", subscriber)

bus.publish("1", dat="2", data="3")
