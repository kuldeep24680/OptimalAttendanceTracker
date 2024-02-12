import unittest

from OptimalAttendanceTracker.main import GraduationCeremony


class TestGraduationCeremony(unittest.TestCase):

    def test_valid_cases(self):
        inputs = [4, 5, 10, 100]
        expected_results = ["7/15", "14/29", "372/773", "16643989670527436350801123256/34587793007077449264905225769"]

        for n, expected_result in zip(inputs, expected_results):
            with self.subTest(n=n):
                obj = GraduationCeremony(n)
                result = obj.solve()
                self.assertEqual(result, expected_result)

    def test_invalid_cases(self):
        invalid_inputs = [-1, 3]

        for n in invalid_inputs:
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    obj = GraduationCeremony(n)
                    obj.solve()


if __name__ == "__main__":
    unittest.main()
