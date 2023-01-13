from kivy.network.urlrequest import UrlRequest
import json


class HttpClient:
    def get_pizzas(self, on_complete, on_error):
        url = "https://msypizzamama.herokuapp.com/api/GetPizzas"

        def data_received(req, result):
            data = json.loads(result)
            pizzas_dict = []
            for i in data:
                pizzas_dict.append(i["fields"])
            if on_complete:
                on_complete(pizzas_dict)

        def data_error(req, error):
            if on_error:
                on_error(error.verify_message)

        def data_failure(req, result):
            if on_error:
                on_error("Server Error: " + str(req.resp_status))

        req = UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure)
