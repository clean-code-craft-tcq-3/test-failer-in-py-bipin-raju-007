alert_failure_count = 0
is_network_down = False


def network_alert_stub(celsius):
    print(f'ALERT: Temperature is {celsius} celsius')
    if is_network_down:
        return 500
    return 200


def alert_in_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return_code = network_alert_stub(celsius)
    if return_code != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0


alert_in_celsius(400.5)
is_network_down = True
alert_in_celsius(303.6)

print(f'{alert_failure_count} alerts failed.')
assert(alert_failure_count == 1)
print('All is well (maybe!)')
