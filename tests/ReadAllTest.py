from database.models import Song, Podcast, Audiobook
from tests.BaseTest import BaseCase
from tools.manipulate_data import parse_date


class ReadAllTest(BaseCase):
    def test_song(self):
        url = '/api/audios/song/'
        expected_status_code = 200
        expected_content = [
            {
                "ID": 1,
                "name": "Fix You",
                "duration": 257,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            },
            {
                "ID": 11,
                "name": "Bad Liar",
                "duration": 257,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            },
        ]
        for data in expected_content:
            data['uploaded_time'] = parse_date(data['uploaded_time'])
            Song(**data).save()

        response = self.app.get(url)
        for data in expected_content:
            d = data['uploaded_time'].timestamp()
            data['uploaded_time'] = {'$date': int(d * 1000)}
        self.assert_response(response, expected_status_code, expected_content)

    def test_podcast(self):
        url = '/api/audios/podcast/'
        expected_status_code = 200
        expected_content = [
            {
                "ID": 2,
                "name": "Art of Manliness",
                "host": "John Doe",
                "participants": ["m1", "m2", "w1", "w2", "w3"],
                "duration": 4444,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            },
            {
                "ID": 22,
                "name": "12 Rules",
                "host": "Jordan Perterson",
                "participants": ["m1", "m2", "w1", "w2", "w3"],
                "duration": 3967,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            }
        ]
        for data in expected_content:
            data['uploaded_time'] = parse_date(data['uploaded_time'])
            Podcast(**data).save()

        response = self.app.get(url)
        for data in expected_content:
            d = data['uploaded_time'].timestamp()
            data['uploaded_time'] = {'$date': int(d * 1000)}
        self.assert_response(response, expected_status_code, expected_content)

    def test_audiobook(self):
        url = '/api/audios/audiobook/'
        expected_status_code = 200
        expected_content = [
            {
                "ID": 3,
                "title": "Blink",
                "author": "Malcom Gladwell",
                "narrator": "Malcom",
                "duration": 129657,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            },
            {
                "ID": 33,
                "title": "Code",
                "author": "Charles Petzold",
                "narrator": "Charles",
                "duration": 229657,
                "uploaded_time": "2021-05-04T16:41:24+0200"
            }
        ]
        for data in expected_content:
            data['uploaded_time'] = parse_date(data['uploaded_time'])
            Audiobook(**data).save()

        response = self.app.get(url)
        for data in expected_content:
            d = data['uploaded_time'].timestamp()
            data['uploaded_time'] = {'$date': int(d * 1000)}
        self.assert_response(response, expected_status_code, expected_content)
