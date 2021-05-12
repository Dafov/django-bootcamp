from django import forms

from .models import InventoryWaitList


class InventoryWaitListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        product = kwargs.pop("product") or None
        super().__init__(*args, **kwargs)
        self.product = product

    class Meta:
        model = InventoryWaitList
        fields = [
            'email',
        ]


    def clean(self, *args, **kwargs):
        cleaned_data = super().clean(*args, **kwargs)
        # check product inventory
        email = cleaned_data.get("email")
        qs = InventoryWaitList.objects.filter(
            product=self.product, email__iexact=email)
        if qs.count() > 5:
            eror_msg = "10-4 we have your waitlist entry for this product"
            #raise self.add_error("email", eror_msg)
            raise forms.ValidationError(eror_msg)

        return cleaned_data
