from django.test import TestCase
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password
from nose.tools import eq_, ok_
from .factories import AdminFactory, FlightFactory, DeckFactory, DroneFactory
from ..serializers import CreateAdminSerializer, CreateDeckSerializer, CreateDroneSerializer, CreateFlightSerializer


class TestCreateAdminSerializer(TestCase):

    def setUp(self):
        self.user_data = model_to_dict(AdminFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = CreateAdminSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = CreateAdminSerializer(data=self.user_data)
        ok_(serializer.is_valid())

    def test_serializer_hashes_password(self):
        serializer = CreateAdminSerializer(data=self.user_data)
        ok_(serializer.is_valid())

        user = serializer.save()
        ok_(check_password(self.user_data.get('password'), user.password))


class TestCreateFlightSerializer(TestCase):

    def setUp(self):
        self.user_data = model_to_dict(FlightFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = CreateFlightSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = CreateFlightSerializer(data=self.user_data)
        ok_(serializer.is_valid())


class TestCreateDeckSerializer(TestCase):

    def setUp(self):
        self.user_data = model_to_dict(DeckFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = CreateDeckSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = CreateDeckSerializer(data=self.user_data)
        ok_(serializer.is_valid())
