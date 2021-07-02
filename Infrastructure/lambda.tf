resource "aws_iam_role" "iam_for_lambda" {
    name = "WeatherTime_IAM"
    assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Action": "sts:AssumeRole",
        "Principal": {
            "Service": "lambda.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
        }
    ]
}
EOF
}

resource "aws_cloudwatch_log_group" "lambda_log_group" {
    name              = "/aws/lambda/WeatherTimeLogs"
    retention_in_days = 14
}

resource "aws_iam_policy" "lambda_logging" {
    name        = "lambda_logging"
    path        = "/"
    description = "IAM policy for logging from a lambda"

    policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Action": [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
        ],
        "Resource": "arn:aws:logs:*:*:*",
        "Effect": "Allow"
        }
    ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
    role       = aws_iam_role.iam_for_lambda.name
    policy_arn = aws_iam_policy.lambda_logging.arn
}

resource "aws_lambda_function" "lambda" {
    filename      = "../lambda-deployment-package.zip"
    function_name = "WeatherTimeTF"
    role          = aws_iam_role.iam_for_lambda.arn
    handler       = "lambdaFunction.main"

    # The filebase64sha256() function is available in Terraform 0.11.12 and later
    # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
    # source_code_hash = "${base64sha256(file("lambda_function_payload.zip"))}"
    source_code_hash = filebase64sha256("../lambda-deployment-package.zip")

    runtime = "python3.8"

    depends_on = [
        aws_iam_role_policy_attachment.lambda_logs,
        aws_cloudwatch_log_group.lambda_log_group
    ]
}
