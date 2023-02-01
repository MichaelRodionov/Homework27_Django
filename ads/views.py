import json

from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Advertisement
# from ads.data.utils import fill_database


# ----------------------------------------------------------------
# FBV
def check_response(request) -> JsonResponse:
    """
    Function to give status OK response
    :param request: request
    :return: JsonResponse
    """
    if request.method == 'GET':
        # fill_database()
        return JsonResponse({'status': 'OK'}, status=200)


# ----------------------------------------------------------------
# CBV
@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    @staticmethod
    def get(request) -> JsonResponse:
        """
        View to handle GET request to show categories
        :param request: request
        :return: JsonResponse
        """
        if request.method == 'GET':
            categories = Category.objects.all()
            return JsonResponse([{
                'id': category.id,
                'name': category.name
            } for category in categories], safe=False, status=200)

    @staticmethod
    def post(request) -> JsonResponse:
        """
        View to handle POST request to create new category
        :param request: request
        :return: JsonResponse
        """
        category_data = json.loads(request.body)
        category = Category.objects.create(name=category_data['name'])
        return JsonResponse({
            'id': category.id,
            'name': category.name
        }, safe=False, status=201)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """
        View to handle GET request to show one category
        :param request: request
        :return: JsonResponse
        """
        if request.method == 'GET':
            try:
                category = self.get_object()
            except Http404:
                return JsonResponse({'error': 'Not Found'}, status=404)
            return JsonResponse({
                'id': category.id,
                'name': category.name
            }, safe=False, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementView(View):
    @staticmethod
    def get(request) -> JsonResponse:
        """
        View to handle GET request to show advertisements
        :param request: request
        :return: JsonResponse
        """
        if request.method == 'GET':
            advertisements = Advertisement.objects.all()
            return JsonResponse([{
                'id': advertisement.id,
                'name': advertisement.name,
                'author': advertisement.author,
                'price': advertisement.price,
                'description': advertisement.description,
                'address': advertisement.address,
                'is_published': advertisement.is_published,
            } for advertisement in advertisements], safe=False, status=200)

    @staticmethod
    def post(request) -> JsonResponse:
        """
        View to handle GET request to create new advertisement
        :param request: request
        :return: JsonResponse
        """
        advertisement_data = json.loads(request.body)
        advertisement = Advertisement.objects.create(name=advertisement_data['name'],
                                                     author=advertisement_data['author'],
                                                     price=advertisement_data['price'],
                                                     description=advertisement_data['description'],
                                                     address=advertisement_data['address'],
                                                     is_published=advertisement_data['is_published'])
        return JsonResponse({
            'id': advertisement.id,
            'name': advertisement.name,
            'author': advertisement.author,
            'price': advertisement.price,
            'description': advertisement.description,
            'address': advertisement.address,
            'is_published': advertisement.is_published,
        }, safe=False, status=201)


class AdvertisementDetailView(DetailView):
    model = Advertisement

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """
        View to handle GET request to show one advertisement
        :param request: request
        :return: JsonResponse
        """
        if request.method == 'GET':
            try:
                advertisement = self.get_object()
            except Http404:
                return JsonResponse({'error': 'Not Found'}, status=404)
            return JsonResponse({
                'id': advertisement.id,
                'name': advertisement.name,
                'author': advertisement.author,
                'price': advertisement.price,
                'description': advertisement.description,
                'address': advertisement.address,
                'is_published': advertisement.is_published
            }, safe=False, status=200)
