def cashed(func):
    cash = dict()

    def cashed_func(*args):
        if cash.get(args) is None:
            cash[args] = func(args)
        return cash[args]
    return cashed_func

