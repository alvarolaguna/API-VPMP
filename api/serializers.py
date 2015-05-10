from django.forms import widgets
from django.db import models
from rest_framework import serializers
from api.models import User, Report, ImageReport, Comment


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100, default='')
    email = serializers.EmailField(max_length = 100, default='')
    password = serializers.CharField(max_length = 100, default='')
    profile_picture = serializers.CharField(max_length = 100, default = 'api/media/default/profile_default.png')

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `user` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()
        return instance

class ReportSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    user_fk = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    name_subject = serializers.CharField(max_length = 100, default='')
    status = serializers.CharField(max_length = 100, default='')
    gender = serializers.CharField(max_length = 20, default='')
    birth_date = serializers.CharField(max_length = 50, default='')
    state = serializers.CharField(max_length = 100, default='')
    city = serializers.CharField(max_length = 100, default='')
    missing_date = serializers.CharField(max_length = 50, default='')
    description = serializers.CharField(max_length = 500, default='')

    def create(self, validated_data):
        """
        Create and return a new `Report` instance, given the validated data.
        """
        return Report.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Report` instance, given the validated data.
        """
        instance.name_subject = validated_data.get('name_subject', instance.name_subject)
        instance.status = validated_data.get('status', instance.status)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)
        instance.missing_date = validated_data.get('missing_date', instance.missing_date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class ImageReportSerializer(serializers.Serializer):
    report_fk = serializers.PrimaryKeyRelatedField(queryset=Report.objects.all())
    image = serializers.CharField(max_length = 100, default = 'api/media/default/profile_default.png')

    def create(self, validated_data):
        """
        Create and return a new `Image` instance, given the validated data.
        """
        return ImageReport.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Image` instance, given the validated data.
        """
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

class CommentSerializer(serializers.Serializer):
    report_fk = serializers.PrimaryKeyRelatedField(queryset=Report.objects.all())
    comment_date = serializers.CharField(max_length = 20, default='')
    content = serializers.CharField(max_length = 500, default='')

    def create(self, validated_data):
        """
        Create and return a new `Comment` instance, given the validated data.
        """
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Comment` instance, given the validated data.
        """
        instance.comment_date = validated_data.get('comment_date', instance.comment_date)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
