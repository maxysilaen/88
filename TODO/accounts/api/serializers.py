from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)
from tasks.api.serializers import TaskListSerializer
from tasks.models import TasksList

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")

        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


user_detail_url = HyperlinkedIdentityField(
        view_name='user-detail',
        lookup_field='pk'
        )

class UserListSerializer(ModelSerializer):
    url = user_detail_url
    taskslist_set = TaskListSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'first_name',
            'last_name',
            'taskslist_set',
        ]


class UserDetailSerializer(ModelSerializer):
    taskslist_set = TaskListSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'taskslist_set',
        ]
