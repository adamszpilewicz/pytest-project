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


pytest_help:
	@echo "see help of pytest"
	@pytest --help

python_install_requirements:
	@echo "Installing requirements..."
	@./venv_pytest/bin/python3.12 -m pip install -r requirements.txt

test_intro:
	@echo "Running tests..."
	@./venv_pytest/bin/python3.12 -m pytest ./tests/unit/utils/test_db_utils.py

test_intro_verbose:
	@echo "Running tests verbose..."
	@./venv_pytest/bin/python3.12 -m pytest -v ./tests/unit/utils/test_db_utils.py

test_intro_discover:
	@echo "Running tests..."
	@./venv_pytest/bin/python3.12 -m pytest -v ./tests/unit/utils

test_collect_only:
	@echo "Collecting tests without running them..."
	@./venv_pytest/bin/python3.12 -m pytest --collect-only ./tests/unit/utils

test_by_name:
	@echo "Running tests that match the given expression..."
	@./venv_pytest/bin/python3.12 -m pytest -v -k  "generate_insert_query or email" ./tests/unit/utils

test_by_marker:
	@echo "Running tests with a specific marker... (slow)"
	@./venv_pytest/bin/python3.12 -m pytest -v -m "slow" ./tests/unit/utils

test_exit_first:
	@echo "Stopping at first failure..."
	@./venv_pytest/bin/python3.12 -m pytest -v -x ./tests/unit/utils

test_max_fail:
	@echo "Stopping after N failures..."
	@./venv_pytest/bin/python3.12 -m pytest -v --maxfail=2 ./tests/unit/utils

test_no_capture:
	@echo "Disabling output capturing..."
	@./venv_pytest/bin/python3.12 -m pytest -v -s ./tests/unit/utils

test_last_failed:
	@echo "Running only the last failed tests..."
	@./venv_pytest/bin/python3.12 -m pytest --lf ./tests/unit/utils

test_failed_first:
	@echo "Running failed tests first..."
	@./venv_pytest/bin/python3.12 -m pytest --ff ./tests/unit/utils

test_quiet:
	@echo "Running tests in quiet mode..."
	@./venv_pytest/bin/python3.12 -m pytest -q ./app/tests/unit/utils

test_show_locals:
	@echo "Showing local variables in tracebacks..."
	@./venv_pytest/bin/python3.12 -m pytest -l ./tests/unit/utils

test_traceback_style:
	@echo "Setting traceback style..."
	@./venv_pytest/bin/python3.12 -m pytest --tb=long ./tests/unit/utils

test_durations:
	@echo "Showing the durations of tests..."
	@./venv_pytest/bin/python3.12 -m pytest --durations=5 ./tests/unit/utils

test_run_marked:
	@echo "Running tests with marker..."
	@./venv_pytest/bin/python3.12 -m pytest -v -m "slow or error" ./tests/unit/utils

test_built_in_markers:
	@echo "Running tests with built-in markers..."
	@./venv_pytest/bin/python3.12 -m pytest -v -m "not slow" ./tests/unit/utils

test_validate_email_param:
	@echo "Running tests with parameterized tests..."
	@./venv_pytest/bin/python3.12 -m pytest -v ./tests/unit/utils/test_db_utils.py::test_validate_email

# Different ways to run tests
test_single_directory:
	@echo "Running tests in a single directory..."
	@./venv_pytest/bin/python3.12 -m pytest -v ./tests/unit/

test_single_file:
	@echo "Running tests in a single file..."
	@./venv_pytest/bin/python3.12 -m pytest -v ./tests/unit/utils/test_db_utils.py

test_single_test_function:
	@echo "Running a single test..."
	@./venv_pytest/bin/python3.12 -m pytest -v ./tests/unit/utils/test_db_utils.py::test_validate_email

test_single_test_function_param:
	@echo "Running a single test with parameter..."
	@./venv_pytest/bin/python3.12 -m pytest -v ./tests/unit/utils/test_db_utils.py::test_validate_email["Missing @ symbol and domain"]

test_single_class:
	@echo "Running tests in a single class..."
	@./venv_pytest/bin/python3.12 -m pytest -v ./tests/unit/services/test_user_service.py::TestUserService

test_single_class_method:
	@echo "Running a single test in a class..."
	@./venv_pytest/bin/python3.12 -m pytest -v ./tests/unit/services/test_user_service.py::TestUserService::test_register_user_with_valid_email

test_based_on_names:
	@echo "Running tests based on names..."
	@./venv_pytest/bin/python3.12 -m pytest -v -k "fails or invalid" ./tests/unit/utils/test_db_utils.py

test_fixtures_setup:
	@echo "Running tests with setup..."
	@./venv_pytest/bin/python3.12 -m pytest --setup-show ./tests/unit/exporters/test_csv_exporter.py::test_save_to_csv_with_valid_data

test_fixtures_scope:
	@echo "Running tests with setup..."
	@./venv_pytest/bin/python3.12 -m pytest -v --setup-show -k "test_save_to_csv_with_module_scope or test_fetch_data_with_function_scope or test_no_data_message_with_session_scope"  ./tests/unit/exporters/test_csv_exporter.py

test_fixture_autouse:
	@echo "Running tests with autouse..."
	@./venv_pytest/bin/python3.12 -m pytest -v -s ./tests/unit/exporters/test_json_exporter.py

test_fixture_parametrized:
	@echo "Running tests with parameters..."
	@./venv_pytest/bin/python3.12 -m pytest -v ./tests/unit/db/test_mysqldb.py

test_tmpdir:
	@echo "Running tests with tmpdir..."
	@./venv_pytest/bin/python3.12 -m pytest -v --setup-show ./tests/unit/exporters/test_parquet_exporter.py

test_capsys:
	@echo "Running tests with capsys..."
	@./venv_pytest/bin/python3.12 -m pytest -v  ./tests/unit/exporters/test_parquet_exporter.py::test_save_to_parquet_with_empty_data

test_mock_mysql:
	@echo "Running tests with mock..."
	@./venv_pytest/bin/python3.12 -m pytest -v ./tests/unit/db/test_mysqldb.py

test_warn:
	@echo "Running tests with warnings..."
	@./venv_pytest/bin/python3.12 -m pytest -v  ./tests/unit/utils/test_db_utils.py::test_validate_email_with_warning

test_doctest:
	@echo "Running tests with doctest..."
	@./venv_pytest/bin/python3.12  -m doctest -v ./utils/db_utils.py

test_coverage_utils:
	@echo "Running tests with coverage..."
	@./venv_pytest/bin/python3.12 -m pytest -v --cov=utils --cov-report html ./tests/unit/utils

test_coverage_services:
	@echo "Running tests with coverage..."
	@./venv_pytest/bin/python3.12 -m pytest -v --cov=services --cov-report html ./tests/unit/services

test_coverage_exporters:
	@echo "Running tests with coverage..."
	@./venv_pytest/bin/python3.12 -m pytest -v --cov=exporters --cov-report html ./tests/unit/exporters

test_all:
	@echo "Running all tests..."
	@./venv_pytest/bin/python3.12 -m pytest -s -v ./tests/unit
