resource "aws_api_gateway_deployment" "deploy" {
    rest_api_id = aws_api_gateway_rest_api.apigw.id

    triggers = {
        redeployment = sha1(jsonencode([
        aws_api_gateway_resource.capital.id,
        aws_api_gateway_method.get_capital.id,
        aws_api_gateway_integration.capital_integration.id,
        aws_api_gateway_resource.city.id,
        aws_api_gateway_method.get_city.id,
        aws_api_gateway_integration.city_integration.id,
        ]))
    }

    lifecycle {
        create_before_destroy = true
    }
}

resource "aws_api_gateway_stage" "stage" {
    deployment_id = aws_api_gateway_deployment.deploy.id
    rest_api_id   = aws_api_gateway_rest_api.apigw.id
    stage_name    = "accenture"
    cache_cluster_enabled = false
    cache_cluster_size = 0.5
}

resource "aws_api_gateway_api_key" "api_key" {
    name = "AccentureDemoKey"
}

resource "aws_api_gateway_usage_plan" "usage_plan" {
    name = "usage_plan"
    quota_settings {
        limit = 300
        period = "DAY"
    }
    throttle_settings {
        burst_limit = 5
        rate_limit = 1
    } 

    api_stages {
        api_id = aws_api_gateway_rest_api.apigw.id
        stage  = aws_api_gateway_stage.stage.stage_name
    }
}

resource "aws_api_gateway_usage_plan_key" "usage_plan_key" {
    key_id        = aws_api_gateway_api_key.api_key.id
    key_type      = "API_KEY"
    usage_plan_id = aws_api_gateway_usage_plan.usage_plan.id
}