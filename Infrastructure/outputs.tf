output "base_url" {
    value = aws_api_gateway_deployment.deploy.invoke_url
}

output "api_key" {
    value = aws_api_gateway_usage_plan_key.usage_plan_key.value
}
