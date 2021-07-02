resource "aws_api_gateway_rest_api" "apigw" {
    name        = "WeatherTimeTF"
    description = "Get current weather and time for a city or capital."
    api_key_source = "HEADER"
}

resource "aws_api_gateway_request_validator" "validator" {
    name                        = "validator"
    rest_api_id                 = aws_api_gateway_rest_api.apigw.id
    validate_request_body       = true
    validate_request_parameters = true
}


resource "aws_api_gateway_method_settings" "all" {
    rest_api_id = aws_api_gateway_rest_api.apigw.id
    stage_name  = aws_api_gateway_stage.stage.stage_name
    method_path = "*/*"

    settings {
        metrics_enabled = true
        logging_level   = "INFO"
        caching_enabled = false
        cache_ttl_in_seconds = 300
    }
}


resource "aws_lambda_permission" "apigw_permission" {
    statement_id  = "AllowAPIGatewayInvoke"
    action        = "lambda:InvokeFunction"
    function_name = aws_lambda_function.lambda.function_name
    principal     = "apigateway.amazonaws.com"

    # The "/*/*" portion grants access from any method on any resource
    # within the API Gateway REST API.
    source_arn = "${aws_api_gateway_rest_api.apigw.execution_arn}/*/*"
}
