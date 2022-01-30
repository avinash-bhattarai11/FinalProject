from django.db import models
from django.shortcuts import redirect, render,get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Product,Comment
from datetime import datetime
from accounts.forms import CommentForm
import pickle
import numpy as np
model=pickle.load(open("classifier_model.save","rb"))
vectorizer=pickle.load(open("vectorizer.save","rb"))
# Create your views here.

def home(request):
    products =Product.objects
    comments =Comment.objects
    return render(request,'products/home.html',{'products':products,'comments':comments})

def predict_category(s, model=model,vectorizer=vectorizer):
    categories =['negative','positive']
    pred =model.predict(vectorizer.transform(np.array([s])))
    return categories[pred[0]-1]
@login_required
def add_comment(request,product_id):
    eachProduct=Product.objects.get(pk=product_id)
    form=CommentForm(instance=eachProduct)
    if request.method== 'POST': 
        form= CommentForm(request.POST,instance=eachProduct)      
        if form.is_valid():  
         name=request.user.username
         body=form.cleaned_data['body']
         c =Comment(post=eachProduct, name=name,body=body, date_added=datetime.now,remark=predict_category(body))
         c.save()
         return redirect('products-home')
        else:
            print('form is invalid')
    else:
        form=CommentForm()
    context={
        'form':form
    }
          
    return render(request,'products/add_comment.html',context)

@login_required
def create(request):
    if request.method == 'POST':
        if  request.POST['title'] and  request.POST['body'] and  request.FILES['image']:
            product =Product()
            product.title= request.POST['title']
            product.body= request.POST['body']
            product.image= request.FILES['image']
            product.pub_date=timezone.datetime.now()
            product.author=request.user
            product.save()
            return redirect('/products/' +str(product.id))

        else:
            return render(request,'products/product.html')   
    else:
       return render(request,'products/product.html')
@login_required
def detail(request,product_id):
    product =get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'product':product})

