from rest_framework import pagination


class SpeedPayWalletPaginator(pagination.LimitOffsetPagination):
    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "properties": {
                "count": {
                    "type": "integer",
                    "example": 24904981,
                },
                "next": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": "http://api.speedpay.ng/wallets/?{offset_param}=400&{limit_param}=100".format(
                        offset_param=self.offset_query_param,
                        limit_param=self.limit_query_param,
                    ),
                },
                "previous": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": "http://api.speedpay.ng/wallets/?{offset_param}=200&{limit_param}=100".format(
                        offset_param=self.offset_query_param,
                        limit_param=self.limit_query_param,
                    ),
                },
                "results": schema,
            },
        }


class SpeedPayUserPaginator(pagination.LimitOffsetPagination):
    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "properties": {
                "count": {
                    "type": "integer",
                    "example": 246754981,
                },
                "next": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": "http://api.speedpay.ng/users/?{offset_param}=400&{limit_param}=100".format(
                        offset_param=self.offset_query_param,
                        limit_param=self.limit_query_param,
                    ),
                },
                "previous": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": "http://api.speedpay.ng/users/?{offset_param}=200&{limit_param}=100".format(
                        offset_param=self.offset_query_param,
                        limit_param=self.limit_query_param,
                    ),
                },
                "results": schema,
            },
        }
