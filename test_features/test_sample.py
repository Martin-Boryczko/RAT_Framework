import pytest

from http import HTTPStatus
from rest_object_models.sample_model import SampleModel


class TestSample:
    def test_just_sample_for_get(self):
        # GIVEN
        expected_SM = SampleModel()
        response_SM = SampleModel()

        # WHEN
        response = response_SM.get(get_to_model=True)

        # THEN
        assert response.status_code == HTTPStatus.OK
        assert response_SM == expected_SM

    def test_just_sample_for_post(self):
        assert False
