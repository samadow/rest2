from rest_framework import serializers

from .models import Category, Product, User, rewiev


class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerilzers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        if data.get('price', 0) <= 0:
            raise serializers.ValidationError({'price': 'Price must be greater than 0'})
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RewievSerializers(serializers.ModelSerializer):
    class Meta:
        model = rewiev
        fields = '__all__'

    def validate(self, data):
        if not 1 <= data.get('rating', 0) <= 5:
            raise serializers.ValidationError({'rating': 'Rating must be between 1 and 5'})
        return data
