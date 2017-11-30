class ErrorHistory:
    def __init__(self, f):
        self.f = f
        self.errors = []

    def __call__(self, *args, **kwargs):
        R = None
        try:
            R = self.f(*args, **kwargs)
        except Exception as err:
            self.errors.append((type(err), str(err)))
        return R

    def reset(self):
        self.errors = []

    def show_errors(self):
        if len(self.errors) > 0:
            for i,(t,e) in enumerate(self.errors):
                print('{:>3}: {}: {}'.format(i, t, e))
        else:
            print('No errors in {}'.format(self.f.__name__))