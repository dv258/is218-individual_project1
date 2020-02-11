class Addition:
    @staticmethod
    def addition(augend, addend=None):
        if type(augend) == list:
            return sum(augend)

        return augend + addend