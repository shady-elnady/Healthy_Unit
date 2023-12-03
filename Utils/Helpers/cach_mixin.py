class CachedMixin:
    def foo(self, *args, **kwargs):
        result = super().foo(*args, **kwargs)
        self.foo = lambda *args, **kwargs: result
        return result
