from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import check_password
from django.core import exceptions
from index.models import Banner, NewsImage, News, NoticeImage, Notice, Quote
from activity.models import ActivityImage, Activity, Booking
from collection.models import CollectionImage, Collection, Order
from kenshi.models import Kenshi
from member.models import Member


# Index
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = '__all__'


class NoticeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeImage
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    images = NoticeImageSerializer(many=True, read_only=True)

    class Meta:
        model = Notice
        fields = '__all__'


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


# Activity
class ActivityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityImage
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    images = ActivityImageSerializer(many=True, read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    prefecture_display = serializers.CharField(source='get_prefecture_display', read_only=True)

    class Meta:
        model = Activity
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    activity_obj = ActivitySerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['activity_obj', 'user']


# Collection
class CollectionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionImage
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    images = CollectionImageSerializer(many=True, read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Collection
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    collection_obj = CollectionSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['collection_obj', 'user']


# Kenshi
class KenshiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kenshi
        fields = '__all__'


# Member
class MemberProfileSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Member
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
            'phone', 'payment', 'address', 'bookings', 'orders'
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Member
        fields = ['username', 'email', 'password1', 'password2']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"Confirm": "Passwords do not match."})

        try:
            validate_password(data['password1'])
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"Password": list(e.messages)})

        return data

    def create(self, validated_data):
        user = Member.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password1'],
        )
        return user


class UpdateProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'phone', 'payment', 'address', 'password']

    def validate(self, data):
        user = self.context['request'].user
        input_password = data.get('password')

        if not check_password(input_password, user.password):
            raise serializers.ValidationError({"Password": "Password is incorrect. Identity verification failed."})

        return data

    def update(self, instance, validated_data):
        validated_data.pop('password', None)
        return super().update(instance, validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True,)
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct.")
        return value

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})

        try:
            validate_password(data['new_password'])
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})

        return data
