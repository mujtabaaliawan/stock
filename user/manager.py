from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, first_name, last_name, role, **extra_fields):

        if not email or not password:
            raise ValueError('Enter Email and Password')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role=role,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, user_data, **extra_fields):
        email = user_data.get('email')
        first_name = user_data.get('first_name')
        last_name = user_data.get('last_name')
        password = user_data.get('password')
        role = user_data.get('role')
        return self._create_user(email=email, password=password, first_name=first_name,
                                 last_name=last_name, role=role, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        role = "superuser"
        return self._create_user(email=email, password=password, first_name=first_name,
                                 last_name=last_name, role=role, **extra_fields)
