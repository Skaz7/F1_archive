import pytest
import main



def test_one():
    main.open_file("races.csv")
    assert main.data_list[4][4] == "Spanish Grand Prix"

def test_two():
    main.open_file("circuits.csv")
    assert "catal" in main.data_list[4][2].lower()