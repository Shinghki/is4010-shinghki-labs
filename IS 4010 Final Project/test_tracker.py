import pytest
import os
import json
from tracker import log_water, log_workout, get_summary, load_data, save_data

# This file name is used during tests so we don't mess with real data
TEST_FILE = "test_data.json"


@pytest.fixture(autouse=True)
def use_test_file(monkeypatch, tmp_path):
    """Redirect all data storage to a temporary file for each test."""
    test_file = tmp_path / "data.json"
    monkeypatch.setattr("tracker.DATA_FILE", str(test_file))


# --- Water tests ---

def test_log_water_basic():
    """Logging water should save the correct amount."""
    log_water(16)
    data = load_data()
    today = list(data.keys())[0]
    assert data[today]["water"] == 16


def test_log_water_accumulates():
    """Logging water twice should add up correctly."""
    log_water(8)
    log_water(24)
    data = load_data()
    today = list(data.keys())[0]
    assert data[today]["water"] == 32


def test_log_water_decimal():
    """Logging a decimal amount of water should work."""
    log_water(12.5)
    data = load_data()
    today = list(data.keys())[0]
    assert data[today]["water"] == 12.5


# --- Workout tests ---

def test_log_workout_basic():
    """Logging a workout should save the type and minutes."""
    log_workout("pilates", 50)
    data = load_data()
    today = list(data.keys())[0]
    workouts = data[today]["workouts"]
    assert len(workouts) == 1
    assert workouts[0]["type"] == "pilates"
    assert workouts[0]["minutes"] == 50


def test_log_workout_with_distance():
    """Walking workout should save distance."""
    log_workout("walking", 30, 1.8)
    data = load_data()
    today = list(data.keys())[0]
    workout = data[today]["workouts"][0]
    assert workout["distance"] == 1.8


def test_log_workout_no_distance_for_yoga():
    """Yoga workout should not save a distance field."""
    log_workout("yoga", 60)
    data = load_data()
    today = list(data.keys())[0]
    workout = data[today]["workouts"][0]
    assert "distance" not in workout


def test_log_workout_invalid_type(capsys):
    """An invalid workout type should print an error and not save."""
    log_workout("swimming", 30)
    captured = capsys.readouterr()
    assert "Unknown workout type" in captured.out
    data = load_data()
    assert data == {}


def test_log_multiple_workouts():
    """Logging two workouts should save both."""
    log_workout("tennis", 90)
    log_workout("pilates", 45)
    data = load_data()
    today = list(data.keys())[0]
    assert len(data[today]["workouts"]) == 2