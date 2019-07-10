import django.contrib.auth.mixins as mixins
from django.shortcuts import redirect


class SuperuserRequiredMixin(mixins.UserPassesTestMixin):
    login_url = '/accounts/superuser_required'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect(self.login_url + '/?next=' + self.request.path)
