from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['name','email','username','password','designation','department','role']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name'],
            designation=validated_data['designation'],
            department=validated_data['department'],

        )
        user.set_password(validated_data['password'])
        user.save()
        return user    


from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    role = serializers.CharField(read_only=True)

   

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            

            

            validation = {
             
                'email': user.email,
                'password':user.password,
                'role': user.role,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
