from json import dumps, loads

from database.models import Audiobook, Podcast, Song
from tests.BaseTest import BaseCase
from tools.manipulate_data import parse_date, remove_metadata


class UpdateTest(BaseCase):
    def assert_put(self, url, data, Audio):
        response = self.app.put(url, headers={"Content-Type": "application/json"}, data=dumps(data))
        expected_status_code = 200
        expected_content = {
            "id": data['ID'],
            "message": "Successfully updated!"
        }
        self.assert_response(response, expected_status_code, expected_content)

        d = parse_date(data['uploaded_time']).timestamp()
        data['uploaded_time'] = {'$date': int(d * 1000)}
        data_saved = remove_metadata(Audio.objects.get(ID=data['ID']).to_json())
        self.assertEqual(data, loads(data_saved))

    def test_song(self):
        audio_id = 1
        url = '/api/audios/song/' + str(audio_id)
        expected_content = {
            "ID": 1,
            "name": "Fix You",
            "duration": 257,
            "uploaded_time": "2021-05-04T16:41:24+0200"
        }
        expected_content['uploaded_time'] = parse_date(expected_content['uploaded_time'])
        Song(**expected_content).save()

        expected_content = {
            "ID": 1,
            "name": "Radioactive",
            "duration": 216,
            "uploaded_time": "2021-05-04T16:41:24+0200"
        }

        self.assert_put(url, expected_content, Song)

    def test_podcast(self):
        audio_id = 2
        url = '/api/audios/podcast/' + str(audio_id)
        expected_content = {
            "ID": 2,
            "name": "12 Rules",
            "host": "Jordan Perterson",
            "participants": ["m1", "m2", "w1", "w2", "w3"],
            "duration": 3967,
            "uploaded_time": "2021-05-04T16:41:24+0200"
        }
        expected_content['uploaded_time'] = parse_date(expected_content['uploaded_time'])
        Podcast(**expected_content).save()

        expected_content = {
            "ID": 2,
            "name": "Art of Manliness",
            "host": "John Doe",
            "participants": ["m1", "m2", "w1", "w2", "w3"],
            "duration": 4444,
            "uploaded_time": "2021-05-04T16:41:24+0200"
        }

        self.assert_put(url, expected_content, Podcast)

    def test_audiobook(self):
        audio_id = 3
        url = '/api/audios/audiobook/' + str(audio_id)
        expected_content = {
            "ID": 3,
            "title": "Blink",
            "author": "Malcom Gladwell",
            "narrator": "Malcom",
            "duration": 129657,
            "uploaded_time": "2021-05-04T16:41:24+0200"
        }
        expected_content['uploaded_time'] = parse_date(expected_content['uploaded_time'])
        Audiobook(**expected_content).save()

        expected_content = {
            "ID": 3,
            "title": "Code",
            "author": "Charles Petzold",
            "narrator": "Charles",
            "duration": 229657,
            "uploaded_time": "2021-05-04T16:41:24+0200"
        }

        self.assert_put(url, expected_content, Audiobook)

    def test_song_not_found(self):
        audio_id = 1
        data = {
            "ID": 1,
            "name": "Fix You",
            "duration": 257,
            "uploaded_time": "2021-05-04T16:41:24+0200"
        }
        url = '/api/audios/song/' + str(audio_id)
        expected_status_code = 400
        expected_content = {
            "message": "Audio with given id doesn't exists",
            "status": 400
        }
        response = self.app.put(url, headers={"Content-Type": "application/json"}, data=dumps(data))
        self.assert_response(response, expected_status_code, expected_content)

    def test_podcast_not_found(self):
        audio_id = 2
        data = {
            "ID": 2,
            "name": "Art of Manliness",
            "host": "John Doe",
            "participants": ["m1", "m2", "w1", "w2", "w3"],
            "duration": 4444,
            "uploaded_time": "2021-05-04T16:41:24+0200"
        }
        url = '/api/audios/podcast/' + str(audio_id)
        expected_status_code = 400
        expected_content = {
            "message": "Audio with given id doesn't exists",
            "status": 400
        }
        response = self.app.put(url, headers={"Content-Type": "application/json"}, data=dumps(data))
        self.assert_response(response, expected_status_code, expected_content)

    def test_audiobook_not_found(self):
        audio_id = 3
        data = {
            "ID": 3,
            "title": "Blink",
            "author": "Malcom Gladwell",
            "narrator": "Malcom",
            "duration": 129657,
            "uploaded_time": "2021-05-04T16:41:24+0200"
        }
        url = '/api/audios/audiobook/' + str(audio_id)
        expected_status_code = 400
        expected_content = {
            "message": "Audio with given id doesn't exists",
            "status": 400
        }
        response = self.app.put(url, headers={"Content-Type": "application/json"}, data=dumps(data))
        self.assert_response(response, expected_status_code, expected_content)