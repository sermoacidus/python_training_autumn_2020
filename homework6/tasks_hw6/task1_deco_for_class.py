"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """Some code"""

    if "amount_of_instances" not in cls.__dict__:
        setattr(cls, "amount_of_instances", 0)

    source_method_save = cls.__new__

    def __new__(cls, *args, **kwargs):
        cls.amount_of_instances += 1
        return source_method_save(cls, *args, **kwargs)

    def get_created_instances(*args, **kwargs):
        amount = cls.amount_of_instances
        return amount

    def reset_instances_counter(*args, **kwargs):
        current_amount_of_instances = cls.amount_of_instances
        setattr(cls, "amount_of_instances", 0)
        return current_amount_of_instances

    cls.__new__ = __new__
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)
    return cls


@instances_counter
class User:
    pass


if __name__ == "__main__":

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
