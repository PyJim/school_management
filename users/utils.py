from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from datetime import datetime, timedelta
from django.utils.http import base36_to_int, int_to_base36
from django.conf import settings

class CustomTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + 
            six.text_type(timestamp) + 
            six.text_type(user.is_active)
        )
    
    def _num_seconds(self, dt):
        """Returns the number of seconds since epoch."""
        return int((dt - datetime(2001, 1, 1, 0, 0, 0)).total_seconds())

    def _num_seconds_today(self):
        """Returns the number of seconds since epoch for now."""
        return self._num_seconds(datetime.now())

    def make_token(self, user):
        return self._make_token_with_timestamp(user, self._num_seconds_today(), self.secret)

    def check_token(self, user, token):
        if not (user and token):
            return False

        # Parse the token
        try:
            ts_b36, _ = token.split("-")
            ts = base36_to_int(ts_b36)
        except ValueError:
            return False

        # Check that the timestamp in the token is within limit (15 minutes in this case)
        if (self._num_seconds_today() - ts) > 900:
            return False

        # Additional checks for token validity
        return super().check_token(user, token)

    @property
    def secret(self):
        return settings.SECRET_KEY

generate_token = CustomTokenGenerator()
