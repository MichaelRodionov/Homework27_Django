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
    # fill_database()
    return JsonResponse({'status': 'OK'}, status=200)


# ----------------------------------------------------------------
# CBV
@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request) -> JsonResponse:
        """
        View to handle GET request to show categories
        :param request: request
        :return: JsonResponse
        """
        categories = Category.objects.all()
        return JsonResponse([self._create_response(category) for category in categories], safe=False, status=200)

    def post(self, request) -> JsonResponse:
        """
        View to handle POST request to create new category
        :param request: request
        :return: JsonResponse
        """
        try:
            category_data = json.loads(request.body)
            category = Category.objects.create(name=category_data['name'])
        except Exception:
            return JsonResponse({'error': 'Invalid request'}, status=400)
        return JsonResponse(self._create_response(category), status=201)

    @staticmethod
    def _create_response(category: Category) -> dict:
        return {'id': category.pk, 'name': category.name}


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
    def get(self, request) -> JsonResponse:
        """
        View to handle GET request to show advertisements
        :param request: request
        :return: JsonResponse
        """
        advertisements = Advertisement.objects.all()
        return JsonResponse([self._create_response(advertisement) for advertisement in advertisements], safe=False, status=200)

    def post(self, request) -> JsonResponse:
        """
        View to handle GET request to create new advertisement
        :param request: request
        :return: JsonResponse
        """
        try:
            advertisement_data = json.loads(request.body)
            advertisement = Advertisement.objects.create(name=advertisement_data['name'])
        except Exception:
            return JsonResponse({'error': 'Invalid request'}, status=400)
        return JsonResponse(self._create_response(advertisement), status=201)

    @staticmethod
    def _create_response(advertisement: Advertisement) -> dict:
        return {
            'id': advertisement.pk,
            'name': advertisement.name,
            'author': advertisement.author,
            'price': advertisement.price,
            'description': advertisement.description,
            'address': advertisement.address,
            'is_published': advertisement.is_published
        }


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
