from django.test import SimpleTestCase

class TestNear_hundred(SimpleTestCase):
    def test_near_hundred_93(self):
        response = self.client.get('/Warmup1/near-hundred/93')
        self.assertContains(response, True)

    def test_near_hundred_90(self):
        response = self.client.get('/Warmup1/near-hundred/90')
        self.assertContains(response, True)

    def test_near_hundred_89(self):
        response = self.client.get('/Warmup1/near-hundred/89')
        self.assertContains(response, False)

class TestStringSplode(SimpleTestCase):
    def test_stringsplode_code(self):
        response = self.client.get("/Warmup2/String-Splosion/Code")
        self.assertContains(response, "CCoCodCode")

    def test_stringsplode_abs(self):
        response = self.client.get("/Warmup2/String-Splosion/abc")
        self.assertContains(response, "aababc")

    def test_stringsplode_ab(self):
        response = self.client.get("/Warmup2/String-Splosion/ab")
        self.assertContains(response, "aab")

class TestCatDog(SimpleTestCase):
    def test_cat_dog_catdog(self):
        response = self.client.get("/String2/cat-dog/catdog")
        self.assertContains(response, True)

    def test_cat_dog_catcat(self):
        response = self.client.get("/String2/cat-dog/catcat")
        self.assertContains(response, False)

    def test_cat_dog_1cat1cadodog(self):
        response = self.client.get("/String2/cat-dog/1cat1cadodog")
        self.assertContains(response, True)



class TestLoneSum(SimpleTestCase):
    def test_lone_1_2_3(self):
        response = self.client.get("/Logic2/lone-sum/1/2/3")
        self.assertContains(response, 6)

    def test_lone_3_2_3(self):
        response = self.client.get("/Logic2/lone-sum/3/2/3")
        self.assertContains(response, 2)
    def test_lone_3_2_3(self):
        response = self.client.get("/Logic2/lone-sum/3/3/3")
        self.assertContains(response, 0)
