from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchlistPagination(PageNumberPagination):
    page_size = 7
    page_query_param = 'p'
    

class WatchlistOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'


class WatchlistCPagination(CursorPagination):
    page_size = 5
    ordering = 'created'
    cursor_query_param = 'record'