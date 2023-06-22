from conversion import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    fahr = celsius_to_fahrenheit(20)
    assert fahr == 68