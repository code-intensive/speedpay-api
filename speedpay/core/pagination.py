from rest_framework.pagination import LimitOffsetPagination


class SpeedPayWalletPaginator(LimitOffsetPagination):
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
                    "example": f"http://api.speedpay.ng/wallets/?{self.offset_query_param}=400&{self.limit_query_param}=100",
                },
                "previous": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": f"http://api.speedpay.ng/wallets/?{self.offset_query_param}=200&{self.limit_query_param}=100",
                },
                "results": schema,
            },
        }


class SpeedPayUserPaginator(LimitOffsetPagination):
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
                    "example": f"http://api.speedpay.ng/users/?{self.offset_query_param}=400&{self.limit_query_param}=100",
                },
                "previous": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": f"http://api.speedpay.ng/users/?{self.offset_query_param}=200&{self.limit_query_param}=100",
                },
                "results": schema,
            },
        }
