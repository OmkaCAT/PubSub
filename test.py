from Bus import Bus


def test_local_bus():
    bus = Bus()
    results = {'a': 0, 'b': 0}
    expected = {'a', 'b'}

    def sub_func_a(add=0, **kwargs):
        results['a'] += add

    def sub_func_b(add=0, **kwargs):
        results['b'] += add

    bus.subscribe("test", sub_func_a)
    bus.publish("test", add=3)

    assert results == {'a': 3, 'b': 0}

    bus.subscribe("test", sub_func_b)
    bus.publish("test", add=2)

    assert results == {'a': 5, 'b': 2}
