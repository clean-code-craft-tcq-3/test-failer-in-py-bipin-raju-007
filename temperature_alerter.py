alert_failure_count = 0


def alert_in_celsius(fahrenheit_temperature, network_alerter):
    celsius_temperature = (fahrenheit_temperature - 32) * 5 / 9
    return_code = network_alerter(celsius_temperature, network_down_checker=is_network_down)
    if return_code != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        global alert_failure_count
        alert_failure_count += 1


def alert_network(celsius_temperature, network_down_checker):
    print(f'ALERT: Temperature is {celsius_temperature} celsius')
    if network_down_checker():
        return 500
    else:
        # TODO: alert the temperature value over network
        return 200


def is_network_down():
    # TODO: check network connection and return True if down
    pass
