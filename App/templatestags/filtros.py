from django import template

register = template.Library()

@register.filter(name='addclassUsername')
def addclassUsername(value):
    return value.as_widget(attrs={
        'type': 'text',
        'class': 'form-control rounded-left',
        'placeholder': 'Usuário'
    })

@register.filter(name='addclassPassword')
def addclassPassword(value):
    return value.as_widget(attrs={
        'type': 'password',
        'class': 'form-control rounded-left',
        'placeholder': 'Senha'
    })
