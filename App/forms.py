from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        field = ('name', 'description')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'type': 'text', 'class': 'form-control', 'id': 'recipient-name'}),
            'description': forms.TextInput(
                attrs={
                    'type': 'text', 'class': 'form-control', 'id': 'recipient-name'}),            
        }

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        field = ('name')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'type': 'text', 'class': 'form-control', 'id': 'recipient-name'}),
        }

class UrgencyForm(forms.ModelForm):
    class Meta:
        model = Urgency
        field = ('description')
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'type': 'text', 'class': 'form-control', 'id': 'recipient-name'}),
        }

class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        field = ('sector')
        widgets = {
            'sector': forms.TextInput(
                attrs={
                    'type': 'text', 'class': 'form-control', 'id': 'recipient-name'}),
        }

class RequisitionForm(forms.ModelForm):
    class Meta:
        model = Requestion
        field = ('title', 'description', 'anexo', 'category', 'status', 'applicant', 'assigned', 'urgency', 'sector', 'published_date', 'final_date')
        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'id': 'recipient-name'}),
            'description': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'message-text'}),
            'anexo': forms.TextInput(
                attrs={'type': 'file', 'class': 'form-control-file', 'id': 'exampleFormControlFile1'}),
            'category': forms.TextInput(
                attrs={'class': 'form-control'}),
            'status': forms.TextInput(
                attrs={'class': 'form-control'}),
            'applicant': forms.TextInput(
                attrs={'class': 'form-control'}),
            'assigned': forms.TextInput(
                attrs={'class': 'form-control'}),
            'urgency': forms.TextInput(
                attrs={'class': 'form-control'}),
            'sector': forms.TextInput(
                attrs={'class': 'form-control'}),
            'published_date': forms.TextInput(
                attrs={'type': 'date', 'id': 'date', 'name': 'date'}),
            'final_date': forms.TextInput(
                attrs={'type': 'date', 'id': 'date', 'name': 'date'}),
        }