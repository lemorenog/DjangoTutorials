from django import forms
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 
 
     
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Felipe Castro", 
        }) 
 
        return context 
    
class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact us - Online Store",
            "subtitle": "Contact us",
            "description": "This is the contact page ...",
            "author": "Developed by: Felipe Castro",
            "email": "Email: contactus@email.com",
            "number": "Number: +123456789",
            "address": "Address: 123 Main St, City, Country",
        })

        return context
    
class Product: 
    products = [ 
        {"id":"1", "name":"TV", "description":"Best TV", "price": 1000}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 1200}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 50}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 100}, 
    ] 
 
class ProductIndexView(View): 
    template_name = 'products/index.html' 
 
    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 
 
        return render(request, self.template_name, viewData) 
 
class ProductShowView(View): 
    template_name = 'products/show.html' 
 
 
    def get(self, request, id): 
        viewData = {} 
        
        # Validar si el ID es válido
        try:
            index = int(id) - 1
            if index < 0 or index >= len(Product.products):
                return HttpResponseRedirect(reverse('home'))  # redirige a 'home'

            product = Product.products[index]
        except (ValueError, TypeError):
            return HttpResponseRedirect(reverse('home'))  # redirige si id no es entero
        
        viewData["title"] = product["name"] + " - Online Store" 
        viewData["subtitle"] =  product["name"] + " - Product information" 
        viewData["product"] = product 
 
        return render(request, self.template_name, viewData)


 
class ProductForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    # description = forms.CharField(label="Description", max_length=500, widget=forms.Textarea)
    price = forms.FloatField(label="Price")

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("The price must be greater than zero.")
        return price
 
 
class ProductCreateView(View): 
    template_name = 'products/create.html' 
 
    def get(self, request): 
        form = ProductForm() 
        viewData = {} 
        viewData["title"] = "Create product" 
        viewData["form"] = form 
        return render(request, self.template_name, viewData) 
 
    def post(self, request): 
        form = ProductForm(request.POST) 
        if form.is_valid(): 
             
            return render(request, 'products/created.html')  # Redirect to a success page or render a success template
        else: 
            viewData = {} 
            viewData["title"] = "Create product" 
            viewData["form"] = form 
            return render(request, self.template_name, viewData)