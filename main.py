# Press Shift+F10 to execute it from the IntelliJ IDE.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Utils:
    @staticmethod
    def above_below(numbers, val):
        above_ct = 0
        below_ct = 0
        for number in numbers:
            if number > val:
                above_ct += 1
            elif number < val:
                below_ct += 1
        return {
            'above': above_ct,
            'below': below_ct
        }

    @staticmethod
    def string_rotation(orig_str, rotation_amount):
        if rotation_amount < 0:
            raise ValueError(f'Rotation amount must be a positive integer. Given: {rotation_amount}')
        rotation_amount = rotation_amount % len(orig_str)   # Handles case where rotation amount exceeds str length
        return orig_str[len(orig_str) - rotation_amount:] + orig_str[:len(orig_str) - rotation_amount]


if __name__ == '__main__':
    test_numbers = [1, 5, 2, 1, 10]
    assert Utils.above_below(test_numbers, 6) == {"above": 1, "below": 4}

    test_result = Utils.string_rotation('MyString', 2)
    assert test_result == 'ngMyStri'

    test_result = Utils.string_rotation('MyString', 19)
    assert test_result == 'ingMyStr'
