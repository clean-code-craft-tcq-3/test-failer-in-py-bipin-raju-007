import tshirts
import color_map
import temperature_alerter as t_alerter
import color_map_in_string as color_map_stub


def test_tshirt_size():
    assert(tshirts.size(37) == 'S')
    assert(tshirts.size(38) == 'S')
    assert(tshirts.size(40) == 'M')
    assert(tshirts.size(41) == 'M')
    assert(tshirts.size(42) == 'L')
    assert(tshirts.size(43) == 'L')


def test_temperature_alerter():
    is_network_down = False

    def alert_network_stub(celsius_temperature, network_down_checker):
        if is_network_down_stub():
            return 500
        else:
            return 200

    def is_network_down_stub():
        return is_network_down

    t_alerter.alert_in_celsius(400.5, network_alerter=alert_network_stub)
    t_alerter.alert_in_celsius(303.6, network_alerter=alert_network_stub)
    is_network_down = True
    t_alerter.alert_in_celsius(401, network_alerter=alert_network_stub)
    t_alerter.alert_in_celsius(333, network_alerter=alert_network_stub)
    is_network_down = False
    t_alerter.alert_in_celsius(0, network_alerter=alert_network_stub)
    assert (t_alerter.alert_failure_count == 2)


def test_color_map():
    assert (color_map.get_color_map() == color_map_stub.correct_color_map)


def test_num_of_color_mappings():
    num_of_color_maps = color_map.get_num_of_color_mappings()
    assert (num_of_color_maps == 25)
