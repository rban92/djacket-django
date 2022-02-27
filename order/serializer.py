from rest_framework import serializers

from .models import Order, OrderItem

from product.serializers import ProductsSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        field = ('price', 'product', 'quantity',)
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        field = ('id', 'first_name','last_name', 'email', 'address','zipcode','pladce', 'phone', 'stripe_token','items',)
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order