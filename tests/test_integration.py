from fast_module import fast_add
from src import main

def test_main(capsys):
    main.main()
    captured = capsys.readouterr().out
    assert "3 + 5 = 8" in captured