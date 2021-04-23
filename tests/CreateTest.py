from json import dumps, loads

from database.models import Song, Podcast, Audiobook
from tests.BaseTest import BaseCase
from tools.manipulate_data import parse_date, remove_metadata


class CreateTest(BaseCase):
    def assert_post(self, url, post_data, Audio):
        response = self.app.post(url, headers={"Content-Type": "application/json"}, data=dumps(post_data))
        expected_status_code = 200
        expected_content = {
            "id": post_data['audioFileMetadata']['ID'],
            "message": "Successfully created!"
        }
        self.assert_response(response, expected_status_code, expected_content)

        data = post_data['audioFileMetadata']
        d = parse_date(data['uploaded_time']).timestamp()
        data['uploaded_time'] = {'$date': int(d * 1000)}
        data_saved = remove_metadata(Audio.objects.get(ID=data['ID']).to_json())
        self.assertEqual(data, loads(data_saved))

    def test_create_song(self):
        url = '/api/audios/'
        post_data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "ID": 1,
                "name": "Fix You",
                "duration": 257,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            }
        }
        self.assert_post(url, post_data, Song)

    def test_create_podcast(self):
        url = '/api/audios/'
        post_data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "ID": 2,
                "name": "12 Rules",
                "host": "Jordan Perterson",
                "participants": ["m1", "m2", "w1", "w2", "w3"],
                "duration": 3967,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            }
        }
        self.assert_post(url, post_data, Podcast)

    def test_create_audiobook(self):
        url = '/api/audios/'
        post_data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "ID": 3,
                "title": "Blink",
                "author": "Malcom Gladwell",
                "narrator": "Malcom",
                "duration": 129657,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            }
        }
        self.assert_post(url, post_data, Audiobook)

    def test_create_exist_song(self):
        url = '/api/audios/'
        data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "ID": 1,
                "name": "Radioactive",
                "duration": 216,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            }
        }
        data['audioFileMetadata']['uploaded_time'] = parse_date(data['audioFileMetadata']['uploaded_time'])
        Song(**data['audioFileMetadata']).save()

        expected_status_code = 400
        expected_content = {
            "message": "Audio file with given id already exists",
            "status": 400
        }
        data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "ID": 1,
                "name": "Fix You",
                "duration": 257,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            }
        }
        response = self.app.post(url, headers={"Content-Type": "application/json"}, data=dumps(data))
        self.assert_response(response, expected_status_code, expected_content)

    def test_create_exist_podcast(self):
        url = '/api/audios/'
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "ID": 2,
                "name": "12 Rules",
                "host": "Jordan Perterson",
                "participants": ["m1", "m2", "w1", "w2", "w3"],
                "duration": 3967,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            }
        }
        data['audioFileMetadata']['uploaded_time'] = parse_date(data['audioFileMetadata']['uploaded_time'])
        Podcast(**data['audioFileMetadata']).save()

        expected_status_code = 400
        expected_content = {
            "message": "Audio file with given id already exists",
            "status": 400
        }
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "ID": 2,
                "name": "12 Rules",
                "host": "Jordan Perterson",
                "participants": ["m1", "m2", "w1", "w2", "w3"],
                "duration": 3967,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            }
        }
        response = self.app.post(url, headers={"Content-Type": "application/json"}, data=dumps(data))
        self.assert_response(response, expected_status_code, expected_content)

    def test_create_exist_audiobook(self):
        url = '/api/audios/'
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "ID": 3,
                "title": "Blink",
                "author": "Malcom Gladwell",
                "narrator": "Malcom",
                "duration": 129657,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            }
        }
        data['audioFileMetadata']['uploaded_time'] = parse_date(data['audioFileMetadata']['uploaded_time'])
        Audiobook(**data['audioFileMetadata']).save()

        expected_status_code = 400
        expected_content = {
            "message": "Audio file with given id already exists",
            "status": 400
        }
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "ID": 3,
                "title": "Code",
                "author": "Charles Petzold",
                "narrator": "Charles",
                "duration": 229657,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            }
        }
        response = self.app.post(url, headers={"Content-Type": "application/json"}, data=dumps(data))
        self.assert_response(response, expected_status_code, expected_content)
