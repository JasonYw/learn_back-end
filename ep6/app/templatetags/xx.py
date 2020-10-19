from django import template
register =template.Library() #写死的



'''
    自定义模版函数
'''
# @register.filter
# def my_upper(value):
#     return value.uppper()

@register.filter
def pinjie(x,y):
    return x+y

# @register.simple_tag
# def my_lower(value):
#     return value.lower()


@register.simple_tag
def my_pinjie(a1,a2,a3):
    return a1+a2+a3

@register.filter
def my_bool():
    pass
