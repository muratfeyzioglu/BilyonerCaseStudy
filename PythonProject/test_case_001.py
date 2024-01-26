import unittest
from utilities.request_builder import RequestBuilder
from utilities.response_validator import ResponseValidator

class TestAPIEmployees(unittest.TestCase):
    def test_api_employees(self):
        # Prepare request url
        request_builder = RequestBuilder()
        request_url = request_builder.build_get_request_url("/api/v1/employees")

        # Send request
        response = request_builder.send_request(request_url)

        # Validate response
        response_validator = ResponseValidator()
        response_validator.validate_status_code(response, 200)
        response_validator.validate_json_response_length(response, 24)
        response_validator.validate_employee_salary_and_name(response, 313500, "Haley Kennedy")


if __name__ == "__main__":
    unittest.main()
