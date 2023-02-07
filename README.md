# RAT_Framework
**REST API TESTING FRAMEWORK**

The goal of RAT Framework is to easily create base model files and feature files from json schema files.

This version of the framework is dedicated to not experienced test automation engineers in python coding - a mixed solution between DRY and DUMP to make code easily understood and implement, based on the PyTest library.

Another version will be on a separate branch additionally providing behave library for using gherkin for test scenarios.

## Structure:

**1. Generators:**

a) json_schema_to_rest_object.py - the file responsible for creating a base model file and feature file from json schema file (similar to CRUD generators)


**2. Helpers - directory for helpers files (ex. other data conversion like time format from-to)**


**3. Http_mock_server**

a) http_mock_sample_server.py - sample mock server can be used for TDD. You can easily implement other endpoints as mock server responses


**4. Res** - res is a directory dedicated to resource files

a) /json_schema_files/sample_model.json - you can use json schema file to validate json responses


**5. Rest_object_models** - directory for REST object models files. This solution is focused on converting responses to python objects and python object to requests(including json body if exist). The goal is to make assertions on objects, not data.

a) rest_object_interface.py - base interface inherited by other models

b) sample_model.py - sample model as an example HOW TO (the draft file should be also generated by json_schema_to_rest_object.py script) 


**6. Test_features** - directory for test features files

a) test_sample.py - sample file with test scenarios (the draft file should be also generated by json_schema_to_rest_object.py script)


**7. pytest.ini** - the config file for pytest


**8. conftest.py** - the conftest.py file can provide fixtures


## TODO:
1. Add Authorisation option
2. Create a generator in the json_schema_to_rest_object.py file