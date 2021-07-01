#!/bin/bash
pip3 install --target ./Package requests --upgrade
cd Package/
zip -r ../lambda-deployment-package.zip .
cd ../Logic
zip -g ../lambda-deployment-package.zip *.py -x *_test.py