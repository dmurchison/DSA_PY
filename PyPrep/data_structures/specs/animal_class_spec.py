import pytest

@pytest.mark.describe('AnimalClass')
class TestAnimalClass:
    @pytest.fixture
    def animal(self):
        return AnimalClass(height=100, weight=100)

    @pytest.mark.describe('get_friends')
    def test_get_friends(self, animal):
        assert animal.get_friends() == ['Clark', 'Frank', 'Jessica']

    @pytest.mark.describe('set_height')
    def test_set_height(self, animal):
        animal.set_height(200)
        assert animal.height == 200

    @pytest.mark.describe('get_height')
    def test_get_height(self, animal):
        assert animal.get_height() == 100

    @pytest.mark.describe('get_private')
    def test_get_private(self, animal):
        assert animal._AnimalClass__very_private_weight == 1000

    @pytest.mark.describe('greet')
    def test_greet(self, animal):
        assert animal.greet() == "This animal makes no sound"
