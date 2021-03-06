from django.urls import reverse
from rest_framework.test import APITestCase

from core.models import Apartment, ApartmentSensor, Sensor, User


class DigitaTest(APITestCase):
    url = reverse('digita-gw')

    def setUp(self):
        User.objects.create_user(username="nkha", password="123456")
        self.client.login(username="nkha", password="123456")

    def test_invalid_gw_data(self):
        # No sensor
        data = {
            "DevEUI_uplink": {
                "Time": "2018-05-16T08:51:30.438+02:00",
                "DevEUI": "A81758FFFE030CF6",
                "FPort": "5",
                "FCntUp": "272806",
                "ADRbit": "1",
                "MType": "2",
                "FCntDn": "208640",
                "payload_hex": "0100f3022204008c0500062710070e21",
                "mic_hex": "531d3b5d",
                "Lrcid": "00000201",
                "LrrRSSI": "-101.000000",
                "LrrSNR": "0.000000",
                "SpFact": "7",
                "SubBand": "G2",
                "Channel": "LC5",
                "DevLrrCnt": "1",
                "Lrrid": "FF017EB7",
                "Late": "0",
                "LrrLAT": "60.183590",
                "LrrLON": "24.971569",
                "Lrrs": {
                    "Lrr": [
                        {
                            "Lrrid": "FF017EB7",
                            "Chain": "0",
                            "LrrRSSI": "-101.000000",
                            "LrrSNR": "0.000000",
                            "LrrESP": "-104.010300",
                        }
                    ]
                },
                "CustomerID": "100002581",
                "CustomerData": {"alr": {"pro": "LORA/Generic", "ver": "1"}},
                "ModelCfg": "0",
                "BatteryLevel": "254",
                "BatteryTime": "2018-05-16T08:51:30.438+02:00",
                "Margin": "239",
                "DevAddr": "FE030CF6",
            }
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(404, response.status_code)

    def test_valid_gw_data(self):
        sensor = Sensor.objects.create(name="T-800")
        apartment = Apartment.objects.create(user=User.objects.get(username="nkha"))
        ApartmentSensor.objects.create(
            apartment=apartment, sensor=sensor, identifier="A81758FFFE030CF6"
        )

        data = {
            "DevEUI_uplink": {
                "Time": "2018-05-16T08:51:30.438+02:00",
                "DevEUI": "A81758FFFE030CF6",
                "FPort": "5",
                "FCntUp": "272806",
                "ADRbit": "1",
                "MType": "2",
                "FCntDn": "208640",
                "payload_hex": "0100f3022204008c0500062710070e21",
                "mic_hex": "531d3b5d",
                "Lrcid": "00000201",
                "LrrRSSI": "-101.000000",
                "LrrSNR": "0.000000",
                "SpFact": "7",
                "SubBand": "G2",
                "Channel": "LC5",
                "DevLrrCnt": "1",
                "Lrrid": "FF017EB7",
                "Late": "0",
                "LrrLAT": "60.183590",
                "LrrLON": "24.971569",
                "Lrrs": {
                    "Lrr": [
                        {
                            "Lrrid": "FF017EB7",
                            "Chain": "0",
                            "LrrRSSI": "-101.000000",
                            "LrrSNR": "0.000000",
                            "LrrESP": "-104.010300",
                        }
                    ]
                },
                "CustomerID": "100002581",
                "CustomerData": {"alr": {"pro": "LORA/Generic", "ver": "1"}},
                "ModelCfg": "0",
                "BatteryLevel": "254",
                "BatteryTime": "2018-05-16T08:51:30.438+02:00",
                "Margin": "239",
                "DevAddr": "FE030CF6",
            }
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(200, response.status_code)
