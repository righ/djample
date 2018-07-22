import factory
from django.contrib.auth.models import User


def _generate_joe_password(o):
    u = User()
    u.set_password(o.username)
    return u.password


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'username{0}'.format(n))
    email = factory.LazyAttribute(lambda a: '{0}@example.com'.format(a.username))
    password = factory.LazyAttribute(_generate_joe_password)

    is_active = True
    is_staff = True
    is_superuser = True
