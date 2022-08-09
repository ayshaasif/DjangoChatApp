from attr import field
from rest_framework import serializers 
from  .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = '__all__'
    # product_id  = serializers.IntegerField()
    # p_name = serializers.CharField()
    # p_brand = serializers.CharField()
    # production_date = serializers.DateField()
    # price = serializers.FloatField()
    # expiration_date = serializers.DateField()

    # def create(self,validate_date):

    #     return Product.objects.create(**validate_date.get)


    # def update(self,instance,validate_date):
    #     instance.p_name = validate_date.get('p_name',instance.p_name)
    #     instance.p_brand = validate_date.get('p_brand',instance.p_brand)
    #     instance.production_date = validate_date.get('production_date',instance.production_date)
    #     instance.price = validate_date.get('price',instance.price)
    #     instance.expiration_date = validate_date.get('expiration_date',instance.expiration_date)
    #     instance.save()
    #     return instance