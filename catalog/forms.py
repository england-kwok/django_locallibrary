# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:00:14 2019

@author: england.kwok
"""

import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from catalog.models import BookInstance

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
            
        # Check if a ate is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_("Invalid date - renewal more than 4 weeks ahead"))
            
        #Return cleaned data
        
        return data

class RenewBookModelForm(forms.ModelForm):
    def clean_due_back(self):
        data = self.cleaned_data['due_back']
        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
            
        # Check if a ate is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_("Invalid date - renewal more than 4 weeks ahead"))
            
        #Return cleaned data
        
        return data
    
    class Meta:
        model = BookInstance
        fields = ['due_back'] #'__all__' for all fields
        labels = {'due_back': _('Renewal date')}
        help_texts = {'due_back': _('Enter a date between now and 4 weeks ( default 3 weeks)')}

'''
The class RenewBookModelForm above is now functionally equivalent to our original RenewBookForm. 
You could import and use it wherever you currently use RenewBookForm as long as you also update the 
corresponding form variable name from renewal_date to due_back as in the second form declaration: 
RenewBookModelForm(initial={'due_back': proposed_renewal_date}.
'''