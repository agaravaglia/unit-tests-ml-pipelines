# import shutil

# import pytest
# from pytest import TempdirFactory


# @pytest.fixture(scope="session")
# def pytest_directory(tmpdir_factory: TempdirFactory):
#     """
#     Configure mocktest directory
#     """
#     # Create directory
#     mock_data_directory = tmpdir_factory.mktemp("pytest_data")

#     yield mock_data_directory

#     # Destroy files
#     shutil.rmtree(str(mock_data_directory))
