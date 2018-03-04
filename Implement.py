from Bus import Bus


def subscriber(data=None, **kwargs):
    print(data)

bus = Bus()

bus.subscribe("1", subscriber)

bus.publish("1", data="1")
bus.publish("1", data="2")
bus.publish("2", data="2")
bus.publish("3", data="3")
