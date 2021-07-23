""""
11. Interview Questions

Question (1) Write a function with single loop to iterate through 2 lists of equal length. 
x = [10, 20, 30] and y = [100, 90, 80] and output should print [(100, 10), (90, 20), (80, 30)]

Question (2) Write a function to find the spike in the set of number x = [50, 60, 55, 45, 40, 90, 100, 110, 5, 6, 7, 6]. 
Hence expect answer to be [60, 110, 7].

Question (3) Pharmacies and patients. Appointment with Pharmacies.
python -m venv penv
pip install django ...
python startproject pharmacy
....

-->settings.py
PostgreSQL

Terminal
python manage.py startapp appointment

appointment
--> models.py
class Pharmacy(models.Model):
    name = models.CharField(max_length=521, blank=True, null=True)

class Patient(models.Model):
    name = models.CharField(max_length=521, blank=True, null=True)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.SET_NULL, null=True)

class Appointment(models.Model):
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    patient = models.ForeignKey(Patient, ond_)
    pharmacy = models.ForeignKey(Pharmacy)


-->serializers.py
class AppointmentSerializer(serializers.ModelSErializer):
    class Meta:
        model = Appointment
        fields = '__all__'

-->views.py
class BookAppointmentView(generics.GenericsAPIView):
    serializer_class = serializers.AppointmentSerializer
    permissions = [permissions.AllowAny]
    def post(self, request):
        request.data 
        from django.utils import timezone
        appointment = Appointment.object.create(start_time, end_time, patient, pharmacy)
        return self.serializer_class(appointment).data

-->urls.py
path ('/bookappointment', views.BookAppointmentView.as_view(), name="post-appointment")


-->tests.py
class TestAppoint(TestCase)

    def test_appointment(self):
        Appointment.object.create(start_time, end_time, patient, pharmacy)

"""


def interview():
    
    # question 1
    a = [10, 20, 30]
    b = [100, 90, 80]
    c = []
    a = [(b[i], a[i]) for i in range(len(a))]
    for i in range(len(a)):
        c.append((b[i], a[i]))

    # question 2
    x = [60, 50, 55, 45, 40, 90, 100, 110, 5, 6, 6, 7]
    y = []
    for i in range(1, len(x)-1):
        if x[i] >= x[i-1] and x[i] >= x[i+1]:
            y.append(x[i])
    if x[0] >= y[0]:
        y[0] = x[0]
    if x[-1] >= y[-1]:
        y[-1] = x[-1]
    return y


if __name__ == "__main__":
    print(interview())

