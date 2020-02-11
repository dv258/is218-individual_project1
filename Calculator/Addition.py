class Addition:
    @staticmethod
    def sum(augend, addend=None):
        if type(augend) == list:
            return sum(augend)

        return augend + addend
