"""
Changes made:
    in class Filter:
        - "__init__(functions)" to "__init__(*functions)", so it can take several separate functions

    in method make_filter:
        - "keyword_filter_func(value)" to "keyword_filter_func(key, value)"
        - "return value[key] == value" to "return lambda data_set: value == data_set[key]"
        - "filter_funcs.append(keyword_filter_func)" to "filter_funcs.append(keyword_filter_func(key, value))"
        - "return Filter(filter_funcs)" to "return Filter(*filter_funcs)"
"""


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(key, value):
            return lambda data_set: value == data_set[key]

        filter_funcs.append(keyword_filter_func(key, value))
    return Filter(*filter_funcs)
