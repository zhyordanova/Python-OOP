from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    name = 'Student name'

    def setUp(self):
        self.student = Student(self.name)

    def test_check_instance_attr_are_set(self):
        self.assertEqual('Student name', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll__new_course_without_saving_notes__expect_to_add_course(self):
        result = self.student.enroll('Python OOP', ['Inheritance', 'SOLID'], "N")
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(0, len(self.student.courses['Python OOP']))
        self.assertEqual('Course has been added.', result)

    def test_enroll__new_course_with_y_added_notes__expect_to_add_course_and_notes(self):
        result = self.student.enroll('Python OOP', ['Inheritance', 'SOLID'], 'Y')
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(2, len(self.student.courses['Python OOP']))
        self.assertEqual('Course and course notes have been added.', result)

    def test_enroll__new_course_with_empty_list_add_notes__expect_to_add_course_and_notes(self):
        result = self.student.enroll('Python OOP', ['Inheritance', 'SOLID'], '')
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(2, len(self.student.courses['Python OOP']))
        self.assertEqual('Course and course notes have been added.', result)

    def test_enroll__notes_to_existing_course__expect_to_add_notes(self):
        """Add some course and notes to the student """
        self.student.enroll('Python OOP', ['Inheritance', 'SOLID'], '')

        """Test if new notes are appended to the existing course"""
        result = self.student.enroll('Python OOP', ['Abstraction', 'Testing'], '')
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(4, len(self.student.courses['Python OOP']))
        self.assertEqual('Course already added. Notes have been updated.', result)

    def test_add_notes__when_course_not_exist__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Python OOP', ['1', 2])
        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_add_notes_to_existing_course__expect_to_add_notes(self):
        """Add some course and notes to the student """
        self.student.enroll('Python OOP', ['Inheritance', 'SOLID'])

        """Test notes are appended"""
        result = self.student.add_notes('Python OOP', 'Testing')
        self.assertEqual('Notes have been updated', result)
        self.assertEqual(3, len(self.student.courses['Python OOP']))
        self.assertIn('Testing', self.student.courses['Python OOP'])

    def test_leave_not_existing_course__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Python OOP')
        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))

    def test_leave_existing_course(self):
        self.student.enroll('Python OOP', ['Inheritance', 'SOLID'], '')

        result = self.student.leave_course('Python OOP')
        self.assertEqual('Course has been removed', result)
        self.assertEqual(0, len(self.student.courses))


if __name__ == '__main__':
    main()