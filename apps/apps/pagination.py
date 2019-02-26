from rest_framework import pagination


class MyNumberPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    last_page_strings = ['-1']
