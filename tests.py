import unittesting


class TestNEAT(unittesting.TestCase):
    def test_compatibility_distance(self):
        parent_1 = []
        parent_2 = []

        cd = compatibility_distance(parent_1, parent_2)

        self.assertEqual(cd, 0)
        self.assertEqual(cd, 0)
