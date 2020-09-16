from rest_framework.generics import (
	ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView,
)
from datetime import datetime

from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer, BookingDetailsSerializer, UpdateBookingSerializer


class BookFlight(CreateAPIView):
	serializer_class = UpdateBookingSerializer

	def perform_create(self, serializer):
		flight_id = self.kwargs['flight_id']
		serializer.save(
			user=self.request.user,
			flight= Flight.objects.get(id=flight_id),
		)


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class CreateBooking(CreateAPIView):
	serializer_class = UpdateBookingSerializer
	def perform_create(self, serializer):
	    flight_id = self.kwargs['flight_id']
	    serializer.save(user=self.request.user, flight = Flight.objects.get(id=flight_id))


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer


class BookingDetails(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class UpdateBooking(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = UpdateBookingSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class CancelBooking(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'
