from django.test import TestCase

from review_site.models import Business, Review


class ApprovedReviewsTest(TestCase):
    def test_with_prefetch(self):
        business = Business()
        business.save()

        review = Review()
        review.business = business
        review.save()

        businesses = Business.objects.prefetch_related('review_set').all()

        business = businesses[0]
        approved_reviews = business.review_set(manager='approved_reviews').all()

        self.assertEqual(len(approved_reviews), 0)

    def test_without_prefetch(self):
        business = Business()
        business.save()

        review = Review()
        review.business = business
        review.save()

        businesses = Business.objects.all()

        business = businesses[0]
        approved_reviews = business.review_set(manager='approved_reviews').all()

        self.assertEqual(len(approved_reviews), 0)
