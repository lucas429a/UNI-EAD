from rest_framework.generics import ListCreateAPIView
from .models import Account
from .serializer import AccountSerializer


class AccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
