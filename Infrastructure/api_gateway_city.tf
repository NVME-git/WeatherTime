resource "aws_api_gateway_resource" "city" {
    rest_api_id = aws_api_gateway_rest_api.apigw.id
    parent_id   = aws_api_gateway_rest_api.apigw.root_resource_id
    path_part   = "cityweather"
}

resource "aws_api_gateway_method" "get_city" {
    http_method   = "GET"
    authorization = "NONE"
    rest_api_id   = aws_api_gateway_rest_api.apigw.id
    resource_id   = aws_api_gateway_resource.city.id
    api_key_required = true
    request_validator_id = aws_api_gateway_request_validator.validator.id
    request_parameters = {
        "method.request.querystring.City" = true,
        "method.request.querystring.UserTimeZone" = true,
        "method.request.querystring.Units" = false,
    }
}

resource "aws_api_gateway_integration" "city_integration" {
    http_method = aws_api_gateway_method.get_city.http_method
    resource_id = aws_api_gateway_resource.city.id
    rest_api_id = aws_api_gateway_rest_api.apigw.id
    type        = "AWS"
    integration_http_method = "POST"
    uri = aws_lambda_function.lambda.invoke_arn
    passthrough_behavior = "WHEN_NO_TEMPLATES"
    request_templates = {
        "application/json" = <<EOF
{
    "City": "$input.params('City')",
    "UserTimeZone": "$input.params('UserTimeZone')",
    "Units": "$input.params('Units')"
}
EOF
    }
}

resource "aws_api_gateway_method_response" "city_response_200" {
    rest_api_id = aws_api_gateway_rest_api.apigw.id
    resource_id = aws_api_gateway_resource.city.id
    http_method = aws_api_gateway_method.get_city.http_method
    status_code = "200"
    response_models = {
        "application/json" = "Empty"
    }
}

resource "aws_api_gateway_integration_response" "city_integration_response_200" {
    rest_api_id = aws_api_gateway_rest_api.apigw.id
    resource_id = aws_api_gateway_resource.city.id
    http_method = aws_api_gateway_method.get_city.http_method
    status_code = aws_api_gateway_method_response.city_response_200.status_code
    response_templates = {
        "application/json" = ""
    }
}

resource "aws_api_gateway_method_response" "city_response_400" {
    rest_api_id = aws_api_gateway_rest_api.apigw.id
    resource_id = aws_api_gateway_resource.city.id
    http_method = aws_api_gateway_method.get_city.http_method
    status_code = "400"
}

resource "aws_api_gateway_integration_response" "city_integration_response_400" {
    rest_api_id = aws_api_gateway_rest_api.apigw.id
    resource_id = aws_api_gateway_resource.city.id
    http_method = aws_api_gateway_method.get_city.http_method
    status_code = aws_api_gateway_method_response.city_response_400.status_code
    selection_pattern = ".*Invalid.*"
    response_templates = {
        "application/json" = <<EOF
{
    "errorMessage": $input.path('$.errorMessage')
}
EOF
    }
}