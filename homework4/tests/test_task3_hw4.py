from tasks_hw4.task3_get_print_output import my_precious_logger


def test_output(capsys):
    my_precious_logger("error")
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.out == "OK\n"
    assert captured.err == "error\n"
