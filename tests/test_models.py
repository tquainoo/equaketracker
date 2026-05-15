from app.models import Country, Region, Earthquake

def test_models_exist():
    assert Country is not None
    assert Region is not None
    assert Earthquake is not None