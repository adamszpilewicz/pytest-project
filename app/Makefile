## run all tests with verbose flag
#test_v_flag:
#	@echo "test_v_flag"
#	@echo "pytest -v"
#	@pytest -v ./tests
#
## run tests with verbose flag in a single file
#test_v_flag_single_file:
#	@echo "test_v_flag_pytest"
#	@echo "pytest -v tests/unit/test_db_utils.py::test_validate_email"
#	@pytest -v tests/unit/test_db_utils.py::test_validate_email
#
## run all tests with markers
#test_mark_errors:
#	@echo "test_mark_errors"
#	@echo "pytest -v -m errors"
#	@pytest -v -m errors
#
## select by class name
#test_class:
#	@echo "test_class"
#	@echo "pytest -v tests/unit/services/test_user_service.py::TestUserService"
#	@pytest -v tests/unit/services/test_user_service.py::TestUserService
#
## select by name of test
#test_select_by_name_valid:
#	@echo "test_select_by_name_valid"
#	@echo "pytest -v -k '_valid' tests/unit/utils/test_db_utils.py"
#	@pytest -v -k "tld or invalid" tests/unit/utils/test_db_utils.py
#
## select by name of subtest
#test_by_param_name:
#	@pytest -v tests/unit/utils/test_db_utils.py::test_validate_email_invalid["Missing @ symbol"]
#
## show the setup of the test
#test_exporters_setup_show:
#	@echo "test_exporters_setup_show"
#	@echo "pytest --setup-show tests/unit/exporters/test_csv_exporter.py::test_save_to_csv_with_valid_data"
#	@pytest --setup-show tests/unit/exporters/test_csv_exporter.py::test_save_to_csv_with_valid_data
#
#test_exporters_csv:
#	@echo "test_exporters_csv"
#	@echo "pytest -v tests/unit/exporters/test_csv_exporter.py"
#	@pytest -v tests/unit/exporters/test_csv_exporter.py
#
#test_name_fixtures:
#	@echo "test_name_fixtures"
#	@echo "pytest --test_name_fixtures"
#	@pytest --fixtures