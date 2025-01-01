from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from reviews.forms import FeedbackForm
from reviews.models import Feedback
from store.models import Item


class ReviewsIndexView(View):
    def get(self, request):
        return HttpResponse("Wecome to your reviews")

class AddProductReviewView(View):

    def get(self, request, item_description):
        return render(request, 'reviews/add_product_reviewtemplate.html', {
            'form': FeedbackForm(),
            'item_description': item_description,
        })

    def post(self, request, item_description):

        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback = Feedback(
                user=request.user,
                category="product_review",
                review=form.cleaned_data['review'],
                item=Item.items.get(description=item_description)
            )

            feedback.save()

            order = request.user.order_set.get(item__description=item_description)

            return HttpResponseRedirect(reverse('profile:order_details', args=(order.id,)))
        else:
            return render(request, 'reviews/add_reviewtemplate.html', {
                'error': form.errors,
                'item_description': item_description,
            })