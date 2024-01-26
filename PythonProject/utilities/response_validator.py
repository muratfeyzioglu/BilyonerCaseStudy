from Model.json_model import JsonModel
class ResponseValidator:
    def validate_status_code(self, response, expected_status_code):
        assert response.status_code == expected_status_code, f"Expected status code: {expected_status_code}, Actual status code: {response.status_code}"

    def validate_json_response_length(self, response, expected_length):
        response_data = response.json()
        assert len(response_data[JsonModel.data]) == expected_length, f"Expected number of records: {expected_length}, Actual number of records: {len(response_data['data'])}"

    def validate_employee_salary_and_name(self, response, expected_salary, expected_name):
        response_data = response.json()
        for employee in response_data[JsonModel.data]:
            if employee[JsonModel.employee_salary] == expected_salary and employee[JsonModel.employee_name] == expected_name:
                return
        assert False, f"No record found with salary: {expected_salary} and name: {expected_name}"
