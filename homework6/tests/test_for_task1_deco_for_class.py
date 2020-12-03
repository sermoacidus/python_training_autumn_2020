from tasks_hw6.task1_deco_for_class import User, instances_counter


def test_if_class_new_method_not_overwritten_by_deco(capsys):
    @instances_counter
    class test_User:
        def __new__(cls):
            print("test_text")
            instance = super().__new__(cls)
            return instance

    user = test_User()
    captured = capsys.readouterr()
    assert captured.out == "test_text\n"
    assert user.amount_of_instances == 1


def test_add_isntances_method():
    a, b = User(), User()
    assert a.amount_of_instances == 2
    assert b.amount_of_instances == 2
    assert User.amount_of_instances == 2


def test_reset_isntances_method():
    a, b = User(), User()
    a.reset_instances_counter()
    assert a.amount_of_instances == 0
    assert User.amount_of_instances == 0
