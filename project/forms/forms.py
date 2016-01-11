from django import forms


class SimpleForm(forms.Form):
    username = forms.CharField(label="Username", required=True)
    password = forms.CharField(
        label="Password", required=True, widget=forms.PasswordInput)
    remember = forms.BooleanField(label="Remember me?")


class CartForm(forms.Form):
    item = forms.CharField()
    quantity = forms.IntegerField(label="Qty")
    price = forms.DecimalField()


class CreditCardForm(forms.Form):
    fullname = forms.CharField(label="Full Name", required=True)
    card_number = forms.CharField(label="Card", required=True, max_length=16)
    expire = forms.DateField(label="Expire Date", input_formats=['%m/%y'])
    ccv = forms.IntegerField(label="ccv")
    notes = forms.CharField(label="Order Notes", widget=forms.Textarea())
