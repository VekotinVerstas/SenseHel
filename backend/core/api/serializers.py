from rest_framework import serializers

from .. import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'first_name', 'last_name', 'phone')
        read_only_fields = fields


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Service
        fields = (
            'id',
            'name',
            'description',
            'price',
            'benefit_short',
            'benefit_long',
            'eula_url',
            'img_logo_url',
            'img_service_url',
        )
        read_only_fields = fields


class SensorAttributeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SensorAttribute
        fields = ('uri', 'description', 'ui_type')
        read_only_fields = fields


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Sensor
        fields = ('id', 'name', 'description', 'provides')
        read_only_fields = fields


class BasicSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Sensor
        fields = ('id', 'name', 'description')
        read_only_fields = fields


class ApartmentSensorValueSerializer(serializers.ModelSerializer):
    description = serializers.CharField(source='attribute.description')
    uri = serializers.CharField(source='attribute.uri')
    ui_type = serializers.CharField(source='attribute.ui_type')
    sensor = serializers.IntegerField(source='apartment_sensor.sensor_id')

    class Meta:
        model = models.ApartmentSensorValue
        fields = ('sensor', 'value', 'updated_at', 'description', 'uri', 'ui_type')


class ApartmentSensorSerializer(serializers.ModelSerializer):
    apartment_sensor_values = ApartmentSensorValueSerializer(many=True, read_only=True)
    sensor = BasicSensorSerializer()

    class Meta:
        model = models.ApartmentSensor
        fields = ('id', 'apartment_sensor_values', 'identifier', 'sensor')


class ApartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Apartment
        fields = ('id', 'street', 'city', 'postal_code', 'apartment_sensors')
        read_only_fields = fields


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = models.Subscription
        fields = ('id', 'created_at', 'updated_at', 'service')
