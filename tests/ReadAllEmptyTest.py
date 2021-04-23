from tests.BaseTest import BaseCase


class ReadAllEmptyTest(BaseCase):
    def test_empty_response_song(self):
        url = '/api/audios/song/'
        expected_status_code = 200
        expected_content = []
        response = self.app.get(url)
        self.assert_response(response, expected_status_code, expected_content)

    def test_empty_response_podcast(self):
        url = '/api/audios/podcast/'
        expected_status_code = 200
        expected_content = []
        response = self.app.get(url)
        self.assert_response(response, expected_status_code, expected_content)

    def test_empty_response_audiobook(self):
        url = '/api/audios/audiobook/'
        expected_status_code = 200
        expected_content = []
        response = self.app.get(url)
        self.assert_response(response, expected_status_code, expected_content)
