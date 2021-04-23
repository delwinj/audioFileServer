from json import dumps

from tests.BaseTest import BaseCase


class ErrorsTest(BaseCase):
    def test_past_date(self):
        url = '/api/audios/'
        post_data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "ID": 1,
                "name": "Fix You",
                "duration": 257,
                "uploaded_time": "2021-01-04T16:41:24+0200"
            }
        }

        response = self.app.post(url, headers={"Content-Type": "application/json"}, data=dumps(post_data))
        expected_status_code = 400
        expected_content = {
            "message": "Updated time provided in invalid or in an invalid format",
            "status": 400
        }
        self.assert_response(response, expected_status_code, expected_content)

    def test_invalid_date(self):
        url = '/api/audios/'
        post_data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "ID": 1,
                "name": "Fix You",
                "duration": 257,
                "uploaded_time": "04-01-2021T16:41:24+0200"
            }
        }

        response = self.app.post(url, headers={"Content-Type": "application/json"}, data=dumps(post_data))
        expected_status_code = 400
        expected_content = {
            "message": "Updated time provided in invalid or in an invalid format",
            "status": 400
        }
        self.assert_response(response, expected_status_code, expected_content)

    def test_invalid_audio_type(self):
        url = '/api/audios/voicemail/'
        response = self.app.get(url)

        expected_status_code = 400
        expected_content = {
            "message": "Audio type provided is invalid",
            "status": 400
        }
        self.assert_response(response, expected_status_code, expected_content)
