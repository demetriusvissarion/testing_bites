from lib.gratitudes import *

def test_gratitude_health_and_security():
    gratitudes = Gratitudes()
    gratitudes.add('health')
    gratitudes.add('security')
    result = gratitudes.format()
    assert result == "Be grateful for: health, security"

