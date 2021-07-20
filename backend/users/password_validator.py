import re
from difflib import SequenceMatcher

from icecream import ic
from rest_framework import serializers


class PasswordValidatorSer(serializers.ModelSerializer):

    def validate(self, data):
        password = data.get('password')
        username = data.get('username')
        errors = []
        if password:
            if not re.search(r'\d', password):
                errors.append('Password must contain at least one number')

            if not re.search(r'\w', password):
                errors.append('Password must contain at least one letter')

            if not re.search(r'[!@#$%^&*()_+\-=]', password):
                errors.append('Password must contain at least one special character.')

            for i in [{'username': username}]:
                key = list(i.keys())[0]
                if SequenceMatcher(None, password, i[key]).ratio() > 0.5:
                    errors.append(f'Password is too similar to the {key}')

            if len(password) < 8:
                errors.append('Password must contain at least 8 characters.')
            ic(errors)

            if len(errors) > 0:
                raise serializers.ValidationError(errors)

        return super(PasswordValidatorSer, self).validate(data)
