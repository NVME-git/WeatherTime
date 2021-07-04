resource "aws_api_gateway_resource" "capital" {
    rest_api_id = aws_api_gateway_rest_api.apigw.id
    parent_id   = aws_api_gateway_rest_api.apigw.root_resource_id
    path_part   = "capitalweather"
}

resource "aws_api_gateway_method" "get_capital" {
    http_method   = "GET"
    authorization = "NONE"
    rest_api_id   = aws_api_gateway_rest_api.apigw.id
    resource_id   = aws_api_gateway_resource.capital.id
    api_key_required = true
    request_validator_id = aws_api_gateway_request_validator.validator.id
    request_parameters = {
        "method.request.querystring.Country" = true,
        "method.request.querystring.UserTimeZone" = true,
        "method.request.querystring.Units" = false,
    }
}

resource "aws_api_gateway_integration" "capital_integration" {
    http_method = aws_api_gateway_method.get_capital.http_method
    resource_id = aws_api_gateway_resource.capital.id
    rest_api_id = aws_api_gateway_rest_api.apigw.id
    type        = "AWS"
    integration_http_method = "POST"
    uri = aws_lambda_function.lambda.invoke_arn
    passthrough_behavior = "WHEN_NO_TEMPLATES"
    request_templates = {
        "application/json" = <<EOF
{
    "Country": "$input.params('Country')",
    "UserTimeZone": "$input.params('UserTimeZone')",
    "Units": "$input.params('Units')"
}
EOF
    }
}

resource "aws_api_gateway_method_response" "capital_response_200" {
    rest_api_id = aws_api_gateway_rest_api.apigw.id
    resource_id = aws_api_gateway_resource.capital.id
    http_method = aws_api_gateway_method.get_capital.http_method
    status_code = "200"
    response_models = {
        "application/json" = "Empty"
    }
    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = true,
        "method.response.header.Access-Control-Allow-Methods" = true,
        "method.response.header.Access-Control-Allow-Origin" = true
    }
}

resource "aws_api_gateway_integration_response" "capital_integration_response_200" {
    rest_api_id = aws_api_gateway_rest_api.apigw.id
    resource_id = aws_api_gateway_resource.capital.id
    http_method = aws_api_gateway_method.get_capital.http_method
    status_code = aws_api_gateway_method_response.capital_response_200.status_code
    response_templates = {
        "application/json" = ""
    }
    response_parameters = {
        "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
        "method.response.header.Access-Control-Allow-Origin" = "'*'"
    }
}

resource "aws_api_gateway_method_response" "capital_response_400" {
    rest_api_id = aws_api_gateway_rest_api.apigw.id
    resource_id = aws_api_gateway_resource.capital.id
    http_method = aws_api_gateway_method.get_capital.http_method
    status_code = "400"
}

resource "aws_api_gateway_integration_response" "capital_integration_response_400" {
    rest_api_id = aws_api_gateway_rest_api.apigw.id
    resource_id = aws_api_gateway_resource.capital.id
    http_method = aws_api_gateway_method.get_capital.http_method
    status_code = aws_api_gateway_method_response.capital_response_400.status_code
    selection_pattern = ".*Invalid.*"
    response_templates = {
        "application/json" = <<EOF
{
    "errorMessage": $input.path('$.errorMessage')
}
EOF
    }
}


# resource "aws_api_gateway_method" "options_capital" {
#     http_method   = "OPTIONS"
#     authorization = "NONE"
#     rest_api_id   = aws_api_gateway_rest_api.apigw.id
#     resource_id   = aws_api_gateway_resource.capital.id
#     api_key_required = true
# }

# resource "aws_api_gateway_integration" "capital_options_integration" {
#     http_method = aws_api_gateway_method.options_capital.http_method
#     resource_id = aws_api_gateway_resource.capital.id
#     rest_api_id = aws_api_gateway_rest_api.apigw.id
#     type        = "MOCK"
# }

# resource "aws_api_gateway_method_response" "capital_options_response_200" {
#     rest_api_id = aws_api_gateway_rest_api.apigw.id
#     resource_id = aws_api_gateway_resource.capital.id
#     http_method = aws_api_gateway_method.options_capital.http_method
#     status_code = "200"
#     response_models = {
#         "application/json" = "Empty"
#     }
#     response_parameters = {
#         "method.response.header.Access-Control-Allow-Headers" = true,
#         "method.response.header.Access-Control-Allow-Methods" = true,
#         "method.response.header.Access-Control-Allow-Origin" = true
#     }
# }


# resource "aws_api_gateway_integration_response" "capital_options_integration_response_200" {
#     rest_api_id = aws_api_gateway_rest_api.apigw.id
#     resource_id = aws_api_gateway_resource.capital.id
#     http_method = aws_api_gateway_method.options_capital.http_method
#     status_code = aws_api_gateway_method_response.capital_options_response_200.status_code
#     response_templates = {
#         "application/json" = ""
#     }
#     response_parameters = {
#         "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
#         "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
#         "method.response.header.Access-Control-Allow-Origin" = "'*'"
#     }
# }


