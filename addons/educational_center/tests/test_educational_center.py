from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from datetime import timedelta
from odoo import fields


class TestEducationalCenter(TransactionCase):

    def setUp(self):
        super(TestEducationalCenter, self).setUp()
        self.Course = self.env['educational_center.course']
        self.Teacher = self.env['educational_center.teacher']
        self.Student = self.env['educational_center.student']
        self.Group = self.env['educational_center.group']
        self.Payment = self.env['educational_center.payment']
        self.BulkPaymentConfirm = self.env['educational_center.bulk_payment_confirm']

    def test_create_course(self):
        course = self.Course.create({
            'name': 'Endurance Piloting',
            'description': 'Learn to pilot the Endurance spacecraft through wormholes.'
        })
        self.assertEqual(course.name, 'Endurance Piloting')

    def test_create_teacher(self):
        teacher = self.Teacher.create({
            'name': 'Dr. Brand',
            'email': 'brand@nasa.gov',
            'phone': '1234567890'
        })
        self.assertEqual(teacher.name, 'Dr. Brand')

    def test_create_student(self):
        student = self.Student.create({
            'name': 'Murphy Cooper',
            'email': 'murph@nasa.gov',
            'phone': '9876543210'
        })
        self.assertEqual(student.name, 'Murphy Cooper')

    def test_create_group(self):
        course = self.Course.create({'name': 'Wormhole Navigation'})
        group = self.Group.create({
            'name': 'Lazarus Mission Team',
            'course_id': course.id,
            'start_date': fields.Date.today(),
            'end_date': fields.Date.today() + timedelta(days=23*365)
        })
        self.assertEqual(group.name, 'Lazarus Mission Team')
        self.assertEqual(group.course_id, course)

    def test_payment_confirmation(self):
        student = self.Student.create({'name': 'Cooper'})
        payment = self.Payment.create({
            'student_id': student.id,
            'amount': 1000000,
            'note': 'Tuition for Interstellar Travel course'
        })
        self.assertEqual(payment.state, 'draft')
        payment.action_confirm()
        self.assertEqual(payment.state, 'confirmed')

    def test_recent_payment_computation(self):
        student = self.Student.create({'name': 'TARS'})
        payment = self.Payment.create({
            'student_id': student.id,
            'amount': 500000,
            'date': fields.Date.today()
        })
        self.assertTrue(payment.is_recent, "Payment should be marked as recent")

    def test_bulk_payment_confirmation(self):
        student = self.Student.create({'name': 'CASE'})
        payments = self.Payment.create([
            {
                'student_id': student.id,
                'amount': 100000,
                'note': f'Payment {i} for space mission'
            } for i in range(5)
        ])

        wizard = self.BulkPaymentConfirm.create({'payment_ids': [(6, 0, payments.ids)]})
        wizard.confirm_payments()

        for payment in payments:
            self.assertEqual(payment.state, 'confirmed', "All payments should be confirmed")

    def test_time_dilation_on_payment_dates(self):
        student = self.Student.create({'name': 'Romilly'})

        pre_blackhole_payment = self.Payment.create({
            'student_id': student.id,
            'amount': 50000,
            'date': fields.Date.today() - timedelta(days=1000),
            'note': 'Pre-black hole payment'
        })

        post_blackhole_payment = self.Payment.create({
            'student_id': student.id,
            'amount': 50000,
            'date': fields.Date.today(),
            'note': 'Post-black hole payment'
        })

        self.assertLess(pre_blackhole_payment.date, post_blackhole_payment.date,
                        "Time should flow normally despite relativistic effects")

    def test_payment_amount_validation(self):
        student = self.Student.create({'name': 'Doyle'})

        # Test valid amount
        payment = self.Payment.create({
            'student_id': student.id,
            'amount': 100,
        })
        self.assertEqual(payment.state, 'draft')

        # Test negative amount
        with self.assertRaises(ValidationError):
            self.Payment.create({
                'student_id': student.id,
                'amount': -100,
            })

        # Test zero amount
        with self.assertRaises(ValidationError):
            self.Payment.create({
                'student_id': student.id,
                'amount': 0,
            })

    def test_get_last_week_payments(self):
        student = self.Student.create({'name': 'Mann'})

        # Create 10 payments, one for each of the last 10 days
        for i in range(10):
            self.Payment.create({
                'student_id': student.id,
                'amount': 10000,
                'date': fields.Date.today() - timedelta(days=i),
                'note': f'Payment made {i} days ago'
            })

        last_week_payments = self.Payment.get_last_week_payments()
        self.assertEqual(len(last_week_payments), 7,
                         "Should return 7 payments from the last week")
